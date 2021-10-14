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



## Credit
- Thanks to JustDjango on their [youtube video](https://www.youtube.com/watch?v=cdRj9eNR0KI) on stripe payment, this video help me to understand the handling of validation and error while creating stripe payment functionality.
-  