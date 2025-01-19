/*
	GLORY BE TO GOD,
	THE PIZZA SOCIETY APP,
	BY ISRAEL MAFABI EMMANUEL
*/

import { Link } from "react-router-dom";
import logo from "../components/assets/logo.png"

export default function Navbar() {
	return (
		<header className="foodie-navbar">
			<div className="foodie-logo">
				<img src={logo} alt="Pizza logo"/>
				<h1 className="foodie-title">The Pizza Society</h1>
			</div>
			<div className="foodie-links">
				<Link to="/">Home</Link>
			</div>
		</header>
	);
}