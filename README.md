## Issues and Resolutions

- Error message appears when I was making migration after creating models for menu app.
  - this was easy fix as error message clearly indicating that project require to install Pillow in order to complete migration therefore I ran pip3 install Pillow command in my terminal to install Pillow and re ran makemigration command, once Pillow installed I did not see any error message while making migrations.

- When I use python3 manage.py loaddata menu command , error message shown on terminal indicating problem installling fixtures and Could not load menu.Item, this was quite challanging for me to understand the actual issue as I have checked any possible spelling errors or any name mismatch on models.py file, admin.py file and also file names on my project however could not spot any error. After spending almost 45 min on google research I have somohow found that I needed to make new migration to fix this issue, as I made changes to modal and renamed as Item which was previously named as menu which I suspected as an issue. I ran below commands step by step on my terminal which then fixed issue.
```
python3 manage.py makemigrations --dry-run
Migrations for 'menu':
  menu/migrations/0002_auto_20210930_1748.py
  - Create model Item
  - Delete model Menu

python3 manage.py makemigrations
Migrations for 'menu':
  menu/migrations/0002_auto_20210930_1749.py
  - Create model Item
  - Delete model Menu

python3 manage.py migrate --plan
  Planned operations:
    menu.0002_auto_20210930_1749
    Create model Item
    Delete model Menu

python3 manage.py migrate
  Operations to perform:
    Apply all migrations: account, admin, auth, contenttypes, menu, sessions, sites, socialaccount
  Running migrations:
    Applying menu.0002_auto_20210930_1749... OK 
```

- I was testing my live site after creating menu app,and during test images passed on menu template did not displayed on browser however alt attributes were working fine , in this case I thought it was definitely naming mismatch and start cross checking the images name however I couldnt see any error on this. Finally after doing some resaerch on ***how to render images using django*** I understood that my template required image url as I had imageField in my model/database and this required to supply image url while passing to template. I have updated image url to my template accordingly and this fixed issue.
```
before
  <img class="card-img-top img-fluid" src="{{ item.image }}" alt="{{ item.name }}">

after
  <img class="card-img-top img-fluid" src="{{ item.image.url }}" alt="{{ item.name }}">
```

- Issue with scrolling behavior as upon clicked on up-arrow icon, page did not scroll back to the top. I could not see any issue with my codes in HTML and jQuery and decided to checked on dev tool console and noticed there was an error which stating as below:
```
Uncaught TypeError: $(...).fadeOut is not a function
Uncaught TypeError: $(...).fadeIn is not a function
```
  - I then did further research on the console error and fount that I needed to ***update the CDN for jQuery*** on my file, I was using ***slim version of jQuery*** which was causing an issue as only full version of jQuery support animation effects. I have then replaced slim version on jQuery CDN with full version which then solved my problem.

- After I create functionality to add and update items on the basket, I was testing the site on browser however update functionality didnt worked and quantity increased/decreased by 2 everytime on a single click to ***+*** and ***-*** button.
  - I then checked all codes on my views and html file line by line and spotted 2 issue which causing above issue and everything worked as expected after I addressed those issues.
    - I was using script tag to load javascript files on both of the templates i.e , base template and basket template which causing an issue as this resulted action to perform twice and resulted quantity doubled everytime when  ***+*** or ***-*** button clicked, I have then removed script tag from basket template which then resolve this issue.
    - Update option on the basket page did not work upon clicking to it after modifying the item quantiy as quantity and price remained unchanged after modifying the quantity and clicking update option. This issue was causing by naming mismatch while creating views to update basket, input element inside the form had ***name=quantity*** however on views.py file I was using ***item_quantity*** while retriving name from the input element using request.get method this was causing an issue. I have updated this on my views according to the HTML template which fixed this issue
    ```
    before:
    - quantity = int(request.POST.get("item_quantity"))

    after:
    - quantity = int(request.POST.get("quantity"))
    ```

- I have encountered similar issue while testing remove option as it didnt worked and upon checking on terminal there was an error shown, I have done some research on the error and fixed everything as per some information I found on stack overflow and google however same error was shown on terminal , then I reached out to CI tutor support team and as per tutor advised I needed to move the remove part of JS code to my html file which was on static file, which then solved issue. as per tutor advice, for some reason Django post security is not allowing the post request to be successful which is causing a 500 error, which is bit strange to me and I am looking to do further research and study on this. Furthermore I have then decided to move JS code for both update and remove functionality to the bottom of HTML file just to make it simple to understand.

- I had an issue with payment form after adding stripe payment functionality to my checkout page which took me really long time to fix, after completing all the stripe requirements, writting views, signals and javascript codes I was testing the payment form on my browser however testing failed an I was keep getting Django error all the time. I then did massive research on google, slack and stackoverflow to understand the issue and found that similar issue was raised many times however I was not clearly able to understand what causing an issue due to code complexity of the project. I have then approached to tutor support team from CI and tutor advised me that Issue is happen due to I have used the variable before its assignment which was same as error shown on Django. I then strat checking checking all codes one by one and I could not figured out as I set variable named ***intend*** and only used the variable way below its assign. I have the started to analyse and chekeing the indentation line on my workspace and noticed that I set the variable inside the else block but using outside the else block which was the reason of problem, I then simply decided to delete else statement as this was not necessarily required, once I delete the else and update indentetion level issue then ressolve.

- There was another issue again with my form, after I submit the form there was an error message shown on the page, I have checked on the stripe dashboard and payment was received however issue trigerred the error message indicating that there was an issue with my form, I have added some print statements on my code to check the outcome in the terminal and indeed it was appeared to have an issue with the form validation as form was not valid, then I double checked on the form field in my views.py and forms.py and found that was I missing one field while creating form_data on views.py which was causing problem. door_no was assigned as one of the form field on forms.py however this was missing on views.py. Issue ressolve once I updeted door_no field on views.py

- I was still getting django error after fixing all the issue above and this time issue was related to my model which django was clearly indicating. This also became very complicated and difficlut for me to understand therefore I had to reach out to tutor support : Thanks to igor from tutor support team who have superbly advise me on few concepts on ***class and self*** method and this concept helped me to understand the issue : I had some functions in models.py to update the item price however those function were indented inside the wrong class and causing issues which fixed once I move them within the correct class.

- Unfortunately this remained still unsuccessful and I was still having an error, django was throwing an attribute error on my checkout app, this was quite straightforward for me to investigate as django was clearly telling that ***'Order' object has no attribute 'update_total'*** , I then start checking all of my files inside my checkout app and found that there was an issue on signals.py. I had used update_total in my signal instead of update_sum_total and this fixed after I have corrected this.

- After I added webhook to my project, I was using stripe dashboard to test the webhook however test failed and I was keep getting various error code ***502***, ***400***, ***400***. After doing some research on google and slack channel, I found the few ways to check thhis issue further. I ran echo command on my terminal to double check that all of the stripe and webhook secret key is set correctly however when I ran ***echo $STRIPE_WEBHOOK_SECRET*** command on my terminal nothing was shown which was enough for me to understand that webhook secret key was not accessible to my workspace from GitPod env variables. I have then checked on my gitpod setting and compare the varible name against the variable name in my settings.py then I found an issue. Variable name assigned in settings.py was different from the variable name set on my gitpod setting, additionally I checked on webhooks.py file and spotted same issue there. I have then updated my variable across all the settings which then ressolved the problem.

- I was still having an issue while testing the checkout functionality, I created and submit complete one order after completing the payment form, as a result of this form was submitted and order confirmation displayed on page however there was still ***401 error shown*** while checking the events on stripe and also two of the input field (Original basket and Stripe payment intend id) had empty field while checking the order from admin. I had done some further research on 401 error and found the solution of this problem over slack community channel. Issue here was my workspace was not shared at the time of the test which means webhook was not connected to the site. I have then shared my workspace and re-check the functionality again by creating another order and this time all the fields were populated while checking on admin, also no issue on stripe and code 200 was shown.



## Deployment
- Project was deployed to Heroku and process for setup and deployment are as below:
#### Heroku setup
1. Login to [Heroku](https://id.heroku.com/login) and create the app using create app button on heroku website once logged into the page.
2. Give the desire name to the app and choose a region (In my case I have named my app as neupane-kitchen and choose a region as Europe)
3. At this point, app has been created then click the resourses option and search for Heroku Postgres on add-ons section
4. Select the Provision plan, for this project I have use the free plan by selecting ***Hobby Dev - Free*** plan
5. In order to use Postgres few install requirement on gitpod workspace, head up to gitpod terminal and use CLI below to install ***jango database and psycopg2-binary***
   ```
   pip3 install dj_database_url
   pip3 install psycopg2-binary
   ```
6. freeze the requirements using below CLI to make sure Heroku installs all the apps requirements when deployed.
   ```
   pip3 freeze > requirements.txt
   ```

#### Database Setup 
1. Go to settings.py on project level app and import dj_database_url
   ```
   import dj_database_url
2. update database setting as on the settings.py
   ```
   DATABASE = {
       'default' : dj_database_url.prase(<database url form heroku>)
   }
   note: database url can be obtained from heroku config vars ( go to setttings on heroku dashboard and click 'Reveal Config Vars') Or from the command line by typing Heroku config
   ```
3. Run the migrations and get database setup 
   ```
   python3 manage.py migrate
   ```
4. import the items data to the database by using below command
   ```
   python3 manage.py loaddata categories
   python3 manage.py loaddata menu
   
   note : ensure categories is loaded first as items depends on categories
   ```
   
5. create supersuser to login with by typing python3 manage.py createsuperuser in the terminal.
   ```
   gitpod /workspace/neupane-kitchen $ python3 manage.py createsuperuser
   Username (leave blank to use 'gitpod'): shiva123
   Email address: sb4_cbu@yahoo.com
   Password: 
   Password (again): 
   Superuser created successfully.
   ```
6. install gunicorn and also create Procfile to tell Heroku to create web dyno
   ```
   pip3 install gunicorn

   and freeze the requirement
   pip3 freeze > requirements.txt
   ```
7. Use below command to install and login to heroku from terminal
   ```
   type npm install -g heroku on terminal

   type heroku login -i to login 
      gitpod /workspace/neupane-kitchen $ heroku login -i
      heroku: Enter your login credentials
      Email: sb4_cbu@yahoo.com
      Password: ***********
      Logged in as sb4_cbu@yahoo.com

   type heroku apps to see all the apps
     gitpod /workspace/neupane-kitchen $ heroku apps
       === sb4_cbu@yahoo.com Apps
           neupane-kitchen (eu)
           one-stop-solution (eu)
    ```
 8. Disable collect data to avoid heroku from collecting static data when project is deployed initially. 
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
    note : -- app flag required if project has more than one app
    ```
 9. Back in the settings.py update ALLOWED_HOSTS as below
    ```
    ALLOWED_HOSTS = ['<app name>.herokuapp.com', 'localhost']
    note : localhost added on ALLOWED_HOST to ensure gitpod will still work too.
    ```
 #### Deploy to Heroku
 - After git add and git push command, below steps were taken to deploy the app to heroku from the terminal 
    
 - first type heroku git:remote -a <heroku app name> on terminal
    (note : above command required to initialize the heroku git remote due to app was created from Heroku website directly (not with CLI))
       
 - then type git push heroku main on the terminal 

    ```
             gitpod /workspace/neupane-kitchen $ git push heroku main
             Enumerating objects: 1027, done.
             Counting objects: 100% (1027/1027), done.
             Delta compression using up to 16 threads
             Compressing objects: 100% (853/853), done.
             Writing objects: 100% (1027/1027), 12.87 MiB | 7.68 MiB/s, done.
             Total 1027 (delta 496), reused 16 (delta 0), pack-reused 0
             remote: Compressing source files... done.
             remote: Building source:
             remote: -----> Building on the Heroku-20 stack
             remote: -----> Determining which buildpack to use for this app
             remote: -----> Python app detected
             remote: -----> No Python version was specified. Using the buildpack default: python-3.9.7
             remote:        To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
             remote: -----> Installing python-3.9.7
             remote: -----> Installing pip 20.2.4, setuptools 57.5.0 and wheel 0.37.0
             remote: -----> Installing SQLite3
             remote: -----> Installing requirements with pip
             remote:        Collecting asgiref==3.4.1
             remote:          Downloading asgiref-3.4.1-py3-none-any.whl (25 kB)
             remote:        Collecting dj-database-url==0.5.0
             remote:          Downloading dj_database_url-0.5.0-py2.py3-none-any.whl (5.5 kB)
             remote:        Collecting Django==3.2.7
             remote:          Downloading Django-3.2.7-py3-none-any.whl (7.9 MB)
             remote:        Collecting django-allauth==0.45.0
             ................................................
             .................................
             remote: -----> Compressing...
             remote:        Done: 81.6M
             remote: -----> Launching...
             remote:        Released v6
             remote:        https://neupane-kitchen.herokuapp.com/ deployed to Heroku
        
    ```
         
 - Project is now deployed to Heroku.
  
 #### Automatic Deploy to heroku.
 - Visit heroku website and select the app and click on Deploy option
 - Scroll down to Deployment method option and select connect to Github option and type the name of github repository on search field
 - Select connect option and now heroku app is connected to github repo.
 - Scroll further down on deploy option on dashboard and select ' Enable Automatic Deploy' option in order to automatic deployment everytime when the work is is pushed to github.
 - Automatic deployment process can be checked by selecting activity option on heroku dashboard once work is pushed to github, below is the snapshot of building activity from heroku dashboard

    ```
      -----> Building on the Heroku-20 stack
      -----> Using buildpack: heroku/python
      -----> Python app detected
      -----> No Python version was specified. Using the same version as the last build: python-3.9.7
       To use a different version, see: https://devcenter.heroku.com/articles/python-runtimes
      -----> No change in requirements detected, installing from cache
      -----> Using cached install of python-3.9.7
      -----> Installing pip 20.2.4, setuptools 57.5.0 and wheel 0.37.0
      -----> Installing SQLite3
      -----> Installing requirements with pip
      -----> Skipping Django collectstatic since the env var DISABLE_COLLECTSTATIC is set.
      -----> Discovering process types
       Procfile declares types -> web
      -----> Compressing...
       Done: 81.7M
      -----> Launching...
       Released v8
       https://neupane-kitchen.herokuapp.com/ deployed to Heroku

    ```


## Credit
- Thanks to JustDjango on their [youtube video](https://www.youtube.com/watch?v=cdRj9eNR0KI) on stripe payment, this video help me to understand the handling of validation and error while creating stripe payment functionality.


 - ***Code***
  - I have taken some CSS and JS code from CI walkthrough project and modified as per project requirement while creating loading spinner in checkout section of the project
  - I have taken the code from [stackoverflow](https://stackoverflow.com/questions/16344354/how-to-make-blinking-flashing-text-with-css-3) and modified as per my requirement while creating animation effect on my delivery promo text on Navbar.