# Pizza Restaurant Application, 

# By Israel Mafabi Emmanuel

This project comprises a full-stack application for managing a pizza restaurant's data. 

It includes a backend API built with Python, Flask, and SQLAlchemy, and a user interface for interacting with the data.

## Key Components

*   **Backend (Python, Flask, SQLAlchemy):**
    *   Provides API endpoints for managing restaurants, pizzas, and their relationships.
    *   Uses Flask for the web framework, SQLAlchemy for database interaction, and Flask-Migrate for database migrations.
    *   Stores data in a SQLite database.
    *   Handles **Custom API** requests.
    *   Includes serialization rules to prevent recursion in JSON responses.
    *   Has data validation implemented in the models.
    *   Includes comprehensive tests written with pytest.

*   **Frontend (React):**
    *   Displays a list of restaurants with their names and addresses.
    *   Allows users to "visit" and "delete" the different restaurant cards.
    *   Provides a navigation bar with the title of "The Pizza Society" and a Home link.
    *   Has a red background color with light-tan cards.
    *   Provides a user interface to interact with the backend data.

### Data Models

*   **`Restaurant`:** Contains restaurant information (id, name, address).
*   **`Pizza`:** Contains pizza information (id, name, ingredients).
*   **`RestaurantPizza`:** Represents the association between restaurants and pizzas, also storing the price.

### API Endpoints

*   **`GET /restaurants`**: Get all restaurants.
*   **`GET /restaurants/<id>`**: Get a single restaurant by ID.
*   **`DELETE /restaurants/<id>`**: Delete a restaurant (and associated `RestaurantPizza` records).
*   **`GET /pizzas`**: Get all pizzas.
*   **`POST /restaurant_pizzas`**: Create a new association between a restaurant and a pizza.

## How to Run

1. **Clone:** Clone the repository.

2. **Backend Setup:**
   * Navigate to the `server` directory:

     ```shell
     cd server
     ```

   * Create a virtual environment:

     ```shell
     python3 -m venv venv && source venv/bin/activate
     ```

   * Install dependencies: 

     ```shell
     pip install -r requirements.txt
     ```

   * Migrate database: 

     ```shell
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

   * Seed the database: Create a `seed.py` file, fill it with seed data, and execute it with `python seed.py`.

     ```shell
     python seed.py
     ```

   * Run backend server: `python app.py`

     ```shell
     python app.py
     ```

     

3. **Frontend:**

   * The front-end is based on React.

     - So navigate to the client directory

       ```shell
       cd client
       ```

       or alternatively run it directly

       ```shell
       npm install --prefix client
       # then run
       npm start --prefix client
       ```

     - Then run the react app

       ```shell
       npm install
       # then run
       npm start
       ```

4. **Testing:** 

   Run `pytest` in the `server` folder to execute the tests.

   ```shell
   cd server # navigate to the server directory, then run pytest
   pytest
   ```

## Important Notes

*   This application uses an SQLite database.
*   The front-end is based on react and retrieves data from the server.
*   The backend server is intended to run at `http://127.0.0.1:5555`.
*   The front-end can send requests to this backend server address.

## Enjoy the Project

Feel free to reach out... 🤭😍😉

Made with Love... 😎

More so, Glory to God!!!
