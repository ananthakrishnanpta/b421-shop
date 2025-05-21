For every new app in the project

- Ensure that your project virtual environment is activated.
- Ensure that your terminal's pwd is the django project folder

1. `python manage.py startapp <app_name>`
    - for example -  `python manage.py startapp mainapp`

2. Now, to include this app in the project,
    - Go to project root folder and open settings.py
    - Locate the python list named `INSTALLED_APPS`.
        -  This contains the list of app names utilized by the project.
    - Add the newly created app_name as a string at the end of the list.

3. Our project root folder has a `urls.py` meant for routing requests.
 - Now that we are dividing our project into several apps in order to increase the maintainability and readability of the project, we have to divide the job of routing between the apps. 
 - For this purpose, we will be creating an additional `urls.py` module in every individual app and finally importing and utilizing them all together in the project `urls.py` which will be the main routing point.