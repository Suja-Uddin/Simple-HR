# MISFIT-HR

A simple Django web application to manage requests for HR deparment. 

## Getting Started
You can access the live version of this app through this [link]( https://simple-hr.herokuapp.com/)

There are two branches in this repository: **master** and **production**. **production** branch is used to deploy the application in heruko and **master** branch can be used to clone application source code in your machine to run the it locally. You can also [download](https://github.com/Suja-Uddin/Simple-HR/archive/master.zip) the zip file instead of git cloning.

The next section describes how to run the application locally.

### Prerequisites
* ***Python-3.6.5***
* ***pip3***
* **Django-2.1.3**
* **django-bootstrap3-11.0.0**
* **Git** *(If you want to clone the source code locally)*

### Steps
First, make sure that you have ***Python 3*** installed in your machine.

Now, either [download](https://github.com/Suja-Uddin/Simple-HR/archive/master.zip) the zip file of the source code or open your terminal and paste below command to clone it. 
```
git clone https://github.com/Suja-Uddin/Simple-HR.git
```
Then navigate to the project directory
```
cd Simple-HR
```
You can see a *requirements.txt* file which lists the dependencies. Install them using below command
```
pip3 install -r requirements.txt
```
As **pip3** comes with **python3**, you shouldn't face any problem if you have already python3 installed.

Then execute following command to run the server 
```
python3 manage.py runserver
```
This should produce below output
```
Performing system checks...

System check identified no issues (0 silenced).
November 15, 2018 - 13:20:56
Django version 2.1.3, using settings 'misfit_hr.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

This means that you have successfully run the server! Now navigate to http://127.0.0.1:8000 to access the web application.

If you face any problems like *Error: That port is already in use.*, please follow the instructions mentioned in [here](https://stackoverflow.com/a/20240445)

**Please feel free to knock me at *suja.ripon@gmail.com* if you face any problem**
