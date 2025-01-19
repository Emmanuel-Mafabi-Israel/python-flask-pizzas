/*
	GLORY BE TO GOD,
	THE PIZZA SOCIETY APP,
	BY ISRAEL MAFABI EMMANUEL
*/
import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import PizzaForm from "./PizzaForm";

export default function Home() {
	const [{ data: restaurant, error, status }, setRestaurant] = useState({
		data: null,
		error: null,
		status: "pending",
	});

	const { id } = useParams();

	useEffect(() => {
		fetch(`/restaurants/${id}`).then((r) => {
			if (r.ok) {
				r.json().then((restaurant) =>
					setRestaurant({ data: restaurant, error: null, status: "resolved" })
				);
			} else {
				r.json().then((err) =>
					setRestaurant({ data: null, error: err.error, status: "rejected" })
				);
			}
		});
	}, [id]);

	function handleAddPizza(newRestaurantPizza) {
		setRestaurant({
			data: {
				...restaurant,
				restaurant_pizzas: [
					...restaurant.restaurant_pizzas,
					newRestaurantPizza,
				],
			},
			error: null,
			status: "resolved",
		});
	}

	if (status === "pending") return <div className="foodie-loading">Loading...</div>;
	if (status === "rejected") return <div className="foodie-error">Error: {error.error}, Couldn't load page.</div>;

	return (
		<section className="foodie-container">
			<div className="foodie-restaurant-info">
				<div className="foodie-restaurant-info-title-card">
					<h1 className="foodie-restaurant-info-name">{restaurant.name}</h1>
					<p className="foodie-restaurant-info-address">{restaurant.address}</p>
				</div>
				<div className="foodie-restaurant-info-menu-card">
					<h2 className="foodie-restaurant-info-menu-card-title">Pizza Menu</h2>
					{restaurant.restaurant_pizzas.map((restaurant_pizza) => (
						<div className="foodie-restaurant-info-menu-card-ingredient" key={restaurant_pizza.id}> {/* Corrected key here */}
							<h3>{restaurant_pizza.pizza.name}</h3>
							<p>
								<em>{restaurant_pizza.pizza.ingredients}</em>
							</p>
							<p className="price">
								<em>Price ${restaurant_pizza.price}</em>
							</p>
						</div>
					))}
				</div>
				<div className="foodie-restaurant-new-card">
					<h3>Add New Pizza</h3>
					<PizzaForm restaurantId={restaurant.id} onAddPizza={handleAddPizza} />
				</div>
			</div>
		</section>
	);
}