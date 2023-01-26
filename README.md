# Create environment and install all requirements
- python -m venv env
- env/Scripts/activate.ps1
- pip install -r requirements.txt

# PostgreSQL database 
- create a dotenv file
- inside .env file enter your settings :

      POSTGRESQL_USER="your_username"

      POSTGRESQL_PASSWORD="your_password"

- python manage.py migrate

# Create Admin user
- python manage.py createsuperuser 
- then you can attribute a team for all users, run server (python manage.py runserver)
- login with admin account in this url : http://127.0.0.1:8000/admin/
- go to Users and add "Groups" (sales and support)
- now you can assign this group for users 

# EpicEvent Permissions and Postman documentation 
- you can see all endpoints and permission here : https://documenter.getpostman.com/view/17797877/2s8ZDd1Lde
