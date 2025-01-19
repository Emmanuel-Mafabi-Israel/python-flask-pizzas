/*
	GLORY BE TO GOD,
	THE PIZZA SOCIETY APP,
	BY ISRAEL MAFABI EMMANUEL
*/

import { Route, Switch } from "react-router";
import Home from "./Home";
import Navbar from "./Navbar";
import Restaurant from "./Restaurant";

export default function App() {
	return (
		<>
			<Navbar />
			<Switch>
				<Route exact path="/restaurants/:id">
					<Restaurant />
				</Route>
				<Route exact path="/">
					<Home />
				</Route>
			</Switch>
		</>
	);
}