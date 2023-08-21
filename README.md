# WaterWorld E-Commerce

### Set Up:
    
    Run in terminal to run back-end:
        
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

   The idea behind the items being sold on this app is that this is an e-commerce site from the future where basic resources a scarce and are sold at a premium. In this case, water rights are purchased to do even the most basic of needs, including drinking water or taking a shower.

   On the home page, the user is given a backstory behind the store along with a button to allow users to enter the site to shop for water rights.

   On the products page the user and search through the different water right available to them or they may scroll and look at all of their options. The user can click on an item to go to the route for the item details.

   ### Technology Used

   In this project we utilized ReactJS, Tailwind CSS, Python, Flask, and SQLAlchemy.

   ### Phase 4 Flatiron School React Project
   Project by Gina, Justin and Morgan