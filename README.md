# WaterWorld E-Commerce

### Set Up:

    Run in terminal to run back-end:

        pipenv shell
        cd server
        export FLASK_APP=app.py
        export FLASK_RUN_PORT=5555

        flask db revision --autogenerate
        flask db upgrade
        python seed.py

        python app.py

    Run in new terminal to run front-end React:

      Run at level above server:
        npm install
        npm start --prefix client

### About WaterWorld

The objective of this project was to create a full-stack app that allows users to interact with an e-commerce website.

On the home page, the user is given a backstory behind the store along with a button to allow users to enter the site to shop for water rights.

On the products page the user and search through the different water right available to them or they may scroll and look at all of their options. The user can click on an item to go to the route for the item details. On the item details, the user can select "Purchase Water" and then be redirected back to the products page.

If a user is new to the site, they can become a member by selecting the link in the navbar and completing the form. A user can also view orders via the Orders link in the navbar. They can either search from all orders available, or they can search for their name to see only their orders. They can click on an order to change the order quantities or they may cancel the entire order.

The idea behind the items being sold on this app is that this is an e-commerce site from the future where basic resources are scarce and are sold at a premium. In this case, water rights are purchased to do even the most basic of needs, including drinking water or taking a shower.

### Technology Used

In this project we utilized ReactJS, Tailwind CSS, Python, Flask, and SQLAlchemy.

Python, Flask and SQLAlchemy were used to create and support the backend of this app.

React was used to create and display all of our routes and components.

We styled our app using Tailwind CSS.

### Phase 4 Flatiron School React Project

Project by Gina, Justin and Morgan
