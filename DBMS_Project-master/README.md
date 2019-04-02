This is an assignment done as the part of the curriculum of the course, Database Management Systems

The project is named Delicious which acts as a bridge between users and restaurants. 

++ Objective:
i. Web based application for online browsing and search of menu aggregated from multiple restaurants e.g., the services provided by commercial websites like www.zomato.com, www.just-eat.com .
ii. Customers can order food delivery online. Orders are to be forwarded to respective restaurants, who will deliver the food and bill the customers.
Users of the System:  A. System Administrator   B. Restaurants          C. Customers

++ Functionalities:
i. The system provides an entry page which will be the home page after login. The entry page displays restaurant information, search and browse by category.
ii. The system provides a restaurant/customer registration module.
iii. The system allows customers to place orders and track their orders through different stages of delivery.
iv. The system offers billing facility.
v. The system tracks user history and suggest favorites


++ SOFTWARE TO BE INSTALLED

Django 1.10
Python 2.7, MySQL

++ RUNNING THE PROJECT ON YOUR SYSTEM

Changes that should be made in settings.py file

(i) The path of the templates folder should be set properly as in your system ('DIRS' : 'pathto/templates')
(ii) Your database credentials must be linked in the Database field

After making the changes type the following commands in your system

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
python manage.py runserver 
// Server starts running. look at the website in localhost