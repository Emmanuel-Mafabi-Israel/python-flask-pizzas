/*
	GLORY BE TO GOD,
	THE PIZZA SOCIETY APP,
	BY ISRAEL MAFABI EMMANUEL
*/
import { useEffect, useState } from "react";

export default function PizzaForm({ restaurantId, onAddPizza }) {
    const [pizzas, setPizzas] = useState([]);
    const [pizzaId, setPizzaId] = useState("");
    const [price, setPrice] = useState("");
    const [formErrors, setFormErrors] = useState([]);

    useEffect(() => {
        fetch("/pizzas")
            .then((r) => r.json())
            .then(setPizzas);
    }, []);

    function handleSubmit(e) {
      e.preventDefault();

      if (!pizzaId) {
        setFormErrors(["Please select a pizza."]);
        return;
      }

      const formData = {
          pizza_id: parseInt(pizzaId),
          restaurant_id: parseInt(restaurantId),
          price: parseFloat(price),
      };


      fetch("/restaurant_pizzas", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      }).then((r) => {
        if (r.ok) {
          r.json().then((newPizzaRestaurant) => {
            onAddPizza(newPizzaRestaurant);
            setFormErrors([]);
          });
        } else {
            r.json().then((err) => setFormErrors(err.errors));
        }
      });
    }

    return (
        <form onSubmit={handleSubmit}>
            <label htmlFor="pizza_id">Pizza:</label>
            <select
                id="pizza_id"
                name="pizza_id"
                value={pizzaId}
                onChange={(e) => setPizzaId(e.target.value)}
            >
                <option value="">Select a pizza</option>
                {pizzas.map((pizza) => (
                    <option key={pizza.id} value={pizza.id}>
                        {pizza.name}
                    </option>
                ))}
            </select>
            <label htmlFor="pizza_id">Price:</label>
            <input
                id="price"
                name="price"
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
            />
            <button className="foodie-interactive-btn" type="submit">Add To Restaurant</button>
            {formErrors.length > 0
                ? formErrors.map((err) => (
                    <p className="foodie-interactive-error" key={err} style={{ color: "red" }}>
						{err}
                    </p>
                ))
                : null}
        </form>
    );
}