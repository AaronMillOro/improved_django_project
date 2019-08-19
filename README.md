# Improve a Django project

## Context 
The provided data was part of a weekend hackathon that took place a year ago or more. Certainly, the project runs kind of slow and is hard to follow. The aim was to go through the project, find where it's inefficient, and fix it. 

* The provided **requirements.txt** file was used as a reference to install needed packages for the project.

* The **django-debug-toolbar** (version 1.9) was used to inspect places where database queries run too long or hit the database too many times. Query time was optimized (less than 5 queries per view and less than 60 ms in total).

* Templates were checked to validate that **inheritance** worked properly.

* **Models** fields were inspected to validate that they are correctly set  for the type of data they store. Corresponding migrations were carried out.

* **Forms** fields were inspected to verify that use the correct fields and validation. Additional validator were added.

* Unit test were writen. By using the line code **"coverage report"** the overall coverage test is above 75%.

## Test the app on terminal
After inpecting the files, the project seems to be a restaurant/bar that displays the different **season's menus**. If the user is authenticated, the user can modify or add new menus with different items.

1. Set the root repository and install the requirements.

		 pipenv install
		 pipenv shell
		 pip install -r requirements.txt
		

2. Run the application.
		
		 python3 manage.py runserver 0.0.0.0:5000

3. Open your favorite web browser and type:

		http://localhost:5000/

4. To login, you can type:
		
		http://localhost:5000/admin		
		
		 User: aaron
		 Password: SuperPass
		 
5. Then select **'view website'**.


Enjoy! :shipit: