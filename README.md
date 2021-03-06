# UserActivity
A Django application implementing a custom management command 

## Steps to run the code 
### 1
Clone the repo using the command<br>
`git clone https://github.com/Himanshu372/UserActivity.git`<br>
on your local system<br>

### 2 
Create a folder for setting up virtual environment<br>
`mkdir venv`<br>
Setup virtual environment inside venv/ folder<br>
`python3 -m venv /path/to/venv repo`<br>
For this step python3 has to pre-installed on your system<br>
This will create a venv/ virutal environment folder at the repo base<br>

For activating the virtual env, navigate to Scripts folder of the venv directory and use the command<br>
`source Scripts/activate`<br>
You'll able to see `(venv)` in your shell, which is an indicator that virtual environment is active<br>

### 3 
Downloading required packages from requirements.txt<br>
`pip install -r requirements.txt`<br>
This is download all the required packages to virtual env<br>

### 4 
Executing code<br>
Go the level where you can manage.py file is in the repo(which is the base level) and execute this command<br> 
`python manage.py runserver`<br>
This is will start the application in development envrionment<br>

### 5
Executing custom management command<br> 
Keep the json data file at the level of manage.py and execute the command<br>
`python manage.py populate_db --filename`<br>
From the file database will get populated<br>
On localhost:8000 port, you can see the UI<br>
If the database has been populated, you will be able to see the json response as required<br>

### 6
Executing tests<br>
For executing tests, use the following command at the 'tests' directory level inside the app<br>
`./manage.py test bike_app.tests.{test_filename}`<br>
