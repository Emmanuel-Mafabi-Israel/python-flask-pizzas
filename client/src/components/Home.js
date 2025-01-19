/*
	GLORY BE TO GOD,
	THE PIZZA SOCIETY APP,
	BY ISRAEL MAFABI EMMANUEL
*/

import { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";

export default function Home() {
	const [restaurants, setRestaurants] = useState([]);
	const history = useHistory(); // Initialize useHistory

	useEffect(() => {
		fetch("/restaurants")
			.then((r) => r.json())
			.then(setRestaurants);
	}, []);

	function handleDelete(id) {
		fetch(`/restaurants/${id}`, {
			method: "DELETE",
		}).then((r) => {
			if (r.ok) {
				setRestaurants((restaurants) =>
					restaurants.filter((restaurant) => restaurant.id !== id)
				);
			}
		});
	}

	function handleVisit(id) {
		history.push(`/restaurants/${id}`)
	}

	return (
		<section className="foodie-container">
			{restaurants.map((restaurant) => (
				<div key={restaurant.id} className="foodie-card">
					<h2 className="foodie-card-title">
						{restaurant.name}
					</h2>
					<p className="foodie-card-address">Address: {restaurant.address}</p>
					<div className="foodie-card-btns">
						<button className="foodie-interactive-btn visit" onClick={() => handleVisit(restaurant.id)}>Visit</button>
						<button className="foodie-interactive-btn" onClick={() => handleDelete(restaurant.id)}>Delete</button>
					</div>
				</div>
			))}
		</section>
	);
}