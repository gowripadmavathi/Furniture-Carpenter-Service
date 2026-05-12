Woody – Furniture & Carpenter Service Web Application
Project Overview
Woody is a Django-based Furniture and Carpenter Service Web Application developed to provide furniture-related services through a web platform. The application allows users to explore services, view projects, and place orders through a simple and user-friendly interface.
The project follows Django MVT (Model-View-Template) architecture and demonstrates backend development, database integration, frontend-backend communication, and web application flow.

Technologies Used


Python


Django


HTML


CSS


JavaScript


SQLite


Git & GitHub



Features


Responsive furniture service website


Multiple pages such as:


Home


About


Services


Projects


Contact




Order management functionality


Database integration using SQLite


Static files handling (CSS, JS, Images)




Project Workflow


User sends request from browser


Request goes to urls.py


Django redirects request to views.py


Views process logic and interact with database through models


Data is rendered using HTML templates


Response is displayed in browser



Database
The project uses SQLite database.
Main table:


woody_app_orders


The database stores order-related information and application data.

My Role in the Project


Backend development using Django


URL routing implementation


Views and business logic handling


Database integration using SQLite


Frontend template integration


Static files handling


Debugging and testing



How to Run the Project
Step 1 – Clone the Repository
git clone <repository_link>

Step 2 – Create Virtual Environment
python -m venv env
Activate virtual environment:
Windows
env\Scripts\activate

Step 3 – Install Dependencies
pip install -r requirements.txt

Step 4 – Run Migrations
python manage.py makemigrationspython manage.py migrate

Step 5 – Run Server
python manage.py runserver

Open in Browser
http://127.0.0.1:8000/

Learning Outcomes
Through this project, I gained knowledge in:


Django framework


Backend web development


Django MVT architecture


Database handling using SQLite


Frontend and backend integration


URL routing and views


Debugging and project structure



Future Enhancements


User authentication


Payment gateway integration


Product search and filtering


Admin dashboard improvements


Responsive UI enhancements



Conclusion
Woody is a beginner-friendly Django web application that demonstrates the complete workflow of backend web development, database integration, and frontend-backend communication using Python and Django.
