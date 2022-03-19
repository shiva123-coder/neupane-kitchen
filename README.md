## AIM / PURPOSE

This is the last and final project milestone which aims to build and develop a full-stack web application using Python, Django, HTML, CSS, JavaScript, MySQL or Postgres, Stripe and external APIs. The main goal is to create an e-commerce web application for business purposes.
My main target is the food and beverage industry for my e-commerce web application.
My web application features e-commerce functionality, payments using Stripe, user login, blog section, review section for registered customers / users, email confirmation and notification, CRUD functionality for admin to access database records, add, edit, delete items, such as menu, information and blog.
This website is only for educational purposes, the Stripe functionality is set up to accept the test card, please do not enter your personal details, instead please use card details provided in the payment section inside the Features

![image](readme-files/images/home.jpg)

## Table of Contents

- [User Experiences](#user-experiences)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
- [Database models and schema](#database-models-and-schema)
  - [Models](#models)
  - [Database Diagram](#database-diagram)
- [Technoligies Used](#technologies-used)
  - [Languages used](#languages-used)
  - [Frameworks, Libraries, Extensions and Resources Used](#frameworks-libraries-extensions-and-resources-used)
- [Features](#features)
 - [Existing Features](#existing-features)
   - [Navbar](#navbar)
   - [Home Page](#home-page)
   - [All manu page](#all-menu-page)
   - [Item info page](#item-info-page)
   - [Shopping Basket](#shopping-basket)
   - [Checkout](#checkout)
   - [Review](#review)
   - [User Profile](#user-profile)
   - [Blog](#blog)
   - [Superuser](#superuser)
   - [Django messages](#django-messages)
  - [Features to be added in future](#features-to-be-added-in-future)
- [Code Validation](#code-validation)
- [Issues and Resolutions](#issues-and-resolutions)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Heroku Setup](#heroku-setup)
  - [Database Setup](#database-setup)
  - [Deploy to Heroku](#deploy-to-heroku)
  - [Automatic Deploy to Heroku](#automatic-deploy-to-heroku)
  - [Making a Local Clone](#making-a-local-clone)
- [Amazon Web Service](#amazon-web-service)
- [Credit](#credit)
- [Media](#media)
- [Acknowledgements](#acknowledgements)
- [Disclaimer](#disclaimer)


## User experiences

### User Stories
#### Customer
 - As a Customer, I want to be able to view all of the available menu so that I can identify the image, price, information, and review 
 - As a Customer, I want to be able to view specific category from the available menu so that I can identify the image, price, information, and review which suitable for my diet
 - As a Customer, I want to be able to easily identify promotions, such as discounts and / or special offers so that I can Take advantage of extra savings on the menu and reduction of my total spending
 - As a Customer, I want to be able to view / access the interesting articles via blog so that I can to get useful knowledge and read interesting information about the food and traditions
 - As a Customer, I want to be able to select from the available the menu and manage / adjust the order quantity so that I can place the order into basket and easily make changes to my order before check-out
 - As a Customer, I want to be able to easily check my basket so that I can ensure I do not accidentally select the wrong products and / or quantity
 - As a Customer, I want to be able to easily check the total amount of my order so that I can control and avoid unnecessary spending
 - As a Customer, I want to be able to easily enter my payment information in a secured process so that I can check-out quickly with no hassle and protected payment
 - As a Customer, I want to be able to feel my personal and payment information is safe and secure so that I can confidently provide the necessary information to place an order
 - As a Customer, I want to be able to view an order confirmation after check-out so that I can verify that my order has been placed and confirmed with no mistake


#### Site User
 - As a site user, I want to be able to easily register/create an account so that I can have my personal account and be able to view my profile and transactions
 - As a site user, I want to be able to Receive an email confirmation after registering so that I can verify my account and ensure the registration was successful
 - As a site user, I want to be able to Easily login and / or logout so that I can access my personal profile, information and history transaction, also secure my account when not in use
 - As a site user, I want to be able to easily recover my password in case I forget about it so that I can Recover the access to my account and use the website
 - As a site user, I want to be able to add reviews to the available menu so that I can provide useful feedback for other customers and help them to select the favorite menu
 - As a site user, I want to be able to add comments to the articles in the blog so that I can interact with other users or customers and share interesting information related to the articles
 - As a site user, I want to be able to search the menu by name and/or description so that I can find a specific food from the available menu which I like to order
 - As a site user, I want to be able to sort a specific category from the available menu so that I can easily find the menu from specific category by cheapest price, most expensive price  and alphabetical order to suit my diet

#### Admin User
 - As an Admin user, I want to be able to add a new menu so that I can introduce new menu to my customers
 - As an Admin user, I want to be able to edit/update and delete a menu so that I can change the prices, descriptions, images and other information of the food
 - As an Admin user, I want to be able to add a new article to the blog so that I can allow users and customers to find and read new interesting article and information
 - As an Admin user, I want to be able to edit/update an article in the blog so that I can change the details in the article to reflect the latest information, I also want to be able to delete an article in the blog so that I can remove obsolete articles from the blog

### Wireframes

- As an initial process of the project design, wireframes were created for desktop, iPad and mobile screen sizes using [Balsamiq](https://balsamiq.com/).

* Desktop Wireframe - [View](readme-files/wireframes/wireframe-ms4-desktop.pdf)

* iPad Wireframe - [View](readme-files/wireframes/wireframe-ms4-ipad.pdf)

* Mobile Wireframe - [View](readme-files/wireframes/wireframe-ms4-mobile.pdf)


## Database models and schema
### Models
- Profiles
  - User
    - From Django Allauth containing the username, email, and password.
  - Userprofile
    - Model containing the user's details for delivery and future order.

- Menu
  - Items
    - Contains the item information of each items on the page
  - Categories
    - The categories for the each of the items.

- Checkout
  - Order
    - Information on customer's details and order placed by customers.
  - Orderline item
    - Information on the customer order, quantity and the total.

- Reviews
  - Review
    - details of reviewer, review title, description and date of review

- Blog
  - Post
    - the blog post and details of blogger and post title.
  - Comments
    - Comments added by users on each post 

### Database Diagram

  - The database diagram of this project was created by using [Quick Database Diagrams](https://www.quickdatabasediagrams.com/) which shows a list of the fields in each object and relationships between each object.

    <div align="center"><img src="readme-files/images/database-diagram.jpg" alt="database diagram image"></div>

## Technologies Used

### Languages Used
- [Python](https://www.python.org/)
    - I have used  **Python** as the back-end programming language for my project.
- [HTML](en.wikipedia.org/wiki/HTML)
    - I have used **HTML** as the main structural element of my project.
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - The project uses **CSS** to style and theme pages..
 - [Javascript](https://en.wikipedia.org/wiki/JavaScript)
    - The project uses **Javascript** to allow for DOM manipulation.

### Frameworks, Libraries, Extensions and Resources Used  
- [Django](https://www.djangoproject.com/)
  - Django was used to create the project.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
  - Django allauth was used to create the user sign-in function for the site.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
  - Django Crispy Forms were used to utilise the bootstrap form classes.
- [Stripe](https://stripe.com/ie)
  - Stripe has been used for the payment section of the site.
- [Amazon AWS](https://aws.amazon.com/)
  - Amazon AWS was used to store the static files and the images for the site.
- [Quick Database Diagrams](https://www.quickdatabasediagrams.com/)
  - quick database diagrams was used to make a diagram of database schema.
- [JQuery](https://jquery.com)
  - The project uses **jQuery** as the primary JavaScript functionality. This is both the standard jQuery that is built with Materialize components, and my custom jQuery used in my script.js file. 
- [Bootstrap 4](https://getbootstrap.com/)
  - Bootstrap 4 was used for its grid system and its form inputs and its helper classes to make page responsive with minimum code.       
- [Google Fonts:](https://fonts.google.com/)
    - Google font was used to embed the Dosis types font which are used on all pages throughout the website.
- [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add icons for aesthetic and UX purposes.
- [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
- [Gitpod](https://www.gitpod.io/)
    - Gitpod was used as IDE for local development.
- [GitHub](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Gitpod.
- [Git](https://git-scm.com/)
  - Git was used as aversion control system to regularly and add commit changes made to project and pushing them to GitHub
- [Gunicorn](https://gunicorn.org/)
  - Gunicorn was used for deploying the project to Heroku.
- [Heroku](https://id.heroku.com/login)
  - Heroku was used as the hosting platform to deploy my project.
- [HTML Formatter](https://htmlformatter.com/) 
    - HTML formatter was used to format HTML code
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln/related) 
    - Unicorn Revealer tool was used to identify any overflow issues
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - Lighthouse was used to test the performance and loading speed of the website
- [Am I responsive](http://ami.responsivedesign.is/)
  - Am I responsive was used to taking screenshots of the page at different screen sizes.
- [W3.CSS](https://www.w3schools.com/w3css/defaulT.asp) 
    - General resources.
- [Stack Overflow](https://pt.stackoverflow.com/)
    - General resources.
- [Youtube](https://www.youtube.com/) 
   - General resources.
- Code Institute SLACK Community
   -General resources


## Features
### Existing Features

- All the pages on this website are mainly divided into three sections: Navbar section, main content section and footer section. Navbar is fixed at the top of each page and footer is fixed at the bottom. All of the contents, images and information is displayed in between Navbar and footer section.

#### Navbar
- This project utilize the Bootstrap Navbar to create user friendly and attractive navbar with various nav-links with sub-links to ensure user is able to navigate throghout all the page easily from the navbar. Navbar is fixed an the top of the page and divided into three section itself from. Left corner of the navbar shows the name of the business and right corner has three options, Account, basket and blog. Center part of the navbar is divided into three section where top section has flashing delivery promo message, middle section has search field for user to search the items just by typing on the field and bottom section has various menu options to choose which give an option for user to choose the items from their desired category without having to browse to all the items. Nabar is designed to expand to the full screen on larger screen and layout of the navbar is designed to chnaged on small/medium screen. Navbar will collapse on small and medium screen and toggle icon will be appear on the right corner and upon clicking on the toggle icon, top section expand below and display the options and serch bar. Account, basket and blog option will be shoown on top of the navbar while viewing on small/medium devices.  
- Further explanation on the Nav-links and functionlaity as below :
 - Account Option
   - Account option has two different view, logged in user view and non-logged in user view 
   - Logged in user can see three options: Admin, My account and Logout. user will be redirected to right page upon clickin on the link
   - Non logged in user can see two options: Login and Register, user will be redirected to right page upon clickin on the link for further activity to access the page
  - Basket option
    - Idea of having basket option on this project is to always show the user spendings without having to go through unnecessary steps, amount is shown below the basket in GBP and amount will always be shown as  £0.00 untill user add any items to the basket and price on the basket keep updating everytime user add/remove the item to the basket, this allow user to easily control on their spendings.
  - Blog option
    - User will be directed to the blog page once blog option is clicked where user will be able to see various post added by site owner and also be able to comment to the post
  - Home - option for user to visit home page
  - All Menus - user will be able to see all the menu available on the page just by clicking this option
  - Non-veg Meal - This allow user to select only non-veg on the menu rather than browsing the whole menu to find the non-veg, this option has four sub-options to choose from which are chicken, lamb, fish and all non-veg meals.
  - Veg Meal - This allow user to select only Veg items on the menu rather than browsing the whole menu to find the Veg item, this option has four sub-options to choose from which are soup, rice, veg-curry and all veg-meals.
  - Specials - This option allow user to find the items from two sub-options, beverage and new taste. purpose of having this option is to attract more customers by regularly updating various new and special items.
  - Search field - This field allow users to search their desire items just by typing name of the item or description/receipe, if any matches found then browser will show the items to the user, purpose of having this is to help users on saving their time to find the items

#### Home Page
- The background image on the home page is carefully choosen to show the nature of the food this site offer. The image serves as welcome getaway to encourage the curiosity and exploration sense of the users who are accessing the website. The image will draw the attention and give clear indicative of what the website is trying to display or share to the users. As image is the main focus on the homepage, therefore no other contents added to homepage except small slogan and button for user to order, once button clicked user will be taken to the menu page where all items will be displayed.

#### All Menu page
- This page mainly focus on attracting users to the site therefore text information is kept to minimum and carefully selected images are shown with just the name of the food, price and category with small cutlery icon to give extra look to the item. this section is created by utilizing the bootstrap card and upon selecting on the image, browser will then display the item information page. User also have an option to sort the items on the page. Sort opting is situated at the top right section and user has four option to sort the products :
  - Sort by price(Low to High)
  - Sort by price(High to Low)
  - Sort by Name(A to Z)
  - Sort by Name(Z to A)
Top left of the page show the numbers of the items on the page. Aditionally edit and delete button also found below each item image however this option is restricted to superuser only and this allow anyone with superuser access user to edit/update and delete the item information to the site anytime. Backend logic has created using django and python to identify the superusers.

#### Item info page
- Main content of this page is divided into two sections, bootstrap grid has been utilized to create this page and added container with row and column to seperate each section and their subsections to make page responsive on small devices.
 - Item information section
    - User can View the bigger image of the item, item description and price. This section also allow user to add the items to the basket if they wish to do so, user can simply input the quantity on the quantity field or select the quantity by clicking + or - button and then click the button below to add to the basket. Success message will be display on the screen to inform user about their action and success message will also show the basket summary. User also has an option to go back to the main menu if they wish to order more item, by clicking order more button next to the image will navigate user to the menu page.
 - Review Section
    - This section shows all the reviews added by users to the item, reviews section in just below the image and will show review title, rating, description, name of the reviewer and date in dd.mm.y format. User must be logged in to add the review therefore link have been provided just below the image for user to login and once log in successful, user will be then redirected to the same page without having to navigate from the homepage. Once logged in, user will then see button to add review and review can be added by completing the form. all the added reviews can be seen just below the image immediately and user also has an option to edit or delete their review. back end logic fron django/python will check if reviewer and logged in person is same then edit/delete will be displayed below the review for user to add/delete their review

#### Shopping Basket
- Entire section of this page is reserved just for basket information only and main aim is to give user clear view of their order. This page will show item added in the basket with image and name, price of each item, quantity and total spending per item. This page will also show the basket total, delivery fee and sub-total amount. User still has an oppurtinity to remove or add/reduce item quantity just by using the input form and clicking update/remove option below the input form. At the botton of the page user can see how much will be their total spending based on the quantity selected, backend functionality added on this page to let user know that how much extra they will be charged if their order do not reach minimun order requirement for free delivery, therefore message will appear on the screen encouraging user to spend more to save delivery fee. If user is happy with their order then they can proceed to checkout by selecting checkout button or they can add few other items just by selecting select more item button which will then navigate the user back to main menu page.


#### Checkout
- This is the one of the most important section section of this project and this was most complex section to develop, this section mainly use Stripe for payment and also utilize bootstrap and javascript/jquery for its responsiveness and functionality. This page is divided into two sections as below :
  - Order Summary
    - User will have final view of their order in this section before completing the order, this section will show item, price, quantity, basket total, any delivery fee and sub-total. User has no option to adjust their shopping basket at this stage however they can easily navigate back to their basket just by clicking Review Basket button on this page.
  - Payment Section
    - This section is the final section of the page and use the stripe payment method, user just need to provide their details, delivery details and then card details in the payment form to complete the payment. This form required to be fully validated before completing the order, stripe javascript handle the form validation process and display an error message if any field in the payment form is missing or incorrect
      - Delivey address
        - Aim behind this website is to make this as website for personal online food business in near future therefore main users/customers of this site will be local customers who live in the nearby area which is why only postal code and address field have been added on the payment section as no other field required such as country, town etc.
      - Stripe payment form
        - At this stage this project is build for education purpose only therefor stripe test card details can be use to make a test order, card details are below:
            - Card Number : 4242424242424242
            - Card Expiry date: Any date in the future
            - CVC : Any 3 digit number
            - ZIP : Any 5 digit number
        - Once form validated and click complete order button,  order will complete and then order confirmation will be display and also sent to user's email. All orders will be stored into the database
        - during this process, user has an the save-info checkbox next to the form so that their profile will be created and stored in database, this is really good features for returning user as this avoid user from entering their details everytime when they want to order from site which hassle free and also minimize the time.

#### Review 
- Add Review
    - Review setion has added to the item info page and all the review will be displayed below the item with the review title, rating, description, name of the reviewer and date in dd.mm.y format. User must be logged in to add the review therefore link have been provided just below the image for user to login and once log in successful, user will be then redirected to the same page without having to navigate from the homepage. Once logged in, user will then see button to add review and review can be added by completing the simple  form, form have only 3 field: title, review and rating. Title field in the form can be blank however rest of the fields are mandatory. All the added reviews can be seen just below the image immediately and user also has an option to edit or delete their review.

- Edit/delete Review
    - Once user logged into the page, if block in the backend execute and check the user info against the record on database and if logged in user is the same user who post the review than only show edit and delete option. In order to edit the review, user simply need to click edit button and form will appear on the page which will already be prefilled with the information provided by user, user just need to update the field and click update button then updated review will be stored in database and display on the page, User can also delete the review just by clicking the delete button which then completly remove the review from the page and database. user with superuser access can delete any reviews on the page but cant edit therefore only delete button will be display when user logged in as a supersuer.

#### User Profile
  - User has option to view their profile once they logged into the page, All of their past orders will be displayed on their profile and if any changes on their delivery address or contact details, this can also be updated on this page just by updating the form in this page which already prefilled with their details provided to the site previously.

#### Blog
   - This website also consist of blog where site owner can add various post/articles on variety of things. Once user logged in as a superuser, page will automatically disply the button to add post and upon clicking on the button user will be taken to the another page to add the post then user just need to complete the form with details and add post. Details will be then saved to database and post will be added to the page, Siilarly user can perform edit and delet action to the page just by clicking the button below each post.
   All non-logged in user and user without superuser access can view the post and comment on the post however user must be logged in to add or delete the post. user do not have option to edit the post therefore only option is to add and delete the post.

#### Superuser
- Anyone with superuser access of the page will have full control of the page and supersuser is able to perform all CRUD functionality. In order to make process simple and less time consuming, all logic has been added in order to grant the access to various action in very less steps. If user logged in as a superuser then all items on the menu will have edit/delete button which allow superuser to easily update items to the page, similarly blog page will have add posy button displayed and all reviews and comment will also have delete buttons for superuser if in case any comment/review required to be deleted from the page due to the nature of review/comment.

#### Django messages
  - This site utilizes the django messages framework to display various message to inform user on their action everytime when user perform an action, this include add, delete and update. four different types of messages template has been created and they will appear on the page as a bootstrap toast, below are the four different message level :
     - Success messages
     - Warning Messages
     - Error Messages
     - Info Messages

#### Features to be added in future
 - Distance calculation based on user's delivery address and delivery charge based on distance
 - Average rating calculation and display average rating of each item below the item image.
 - Option for users to delete their account  

## Code Validation

- [W3C Markup Validation](https://validator.w3.org/#validate_by_input) 
  - W3C Markup Validation was used throughout the process to validate HTML codes
- [W3C CSS Validation](https://jigsaw.w3.org/css-validator/) 
  - W3C CSS Validation was used to vaildate CSS codes
- [JSHINT](https://jshint.com/) 
  - JSHINT was used for JavaScript code warning & error check.
- [PEP8 online](http://pep8online.com/)
  - PEP8 online tool was used to ensure all python codes on projects are PEP8 compliant.
- [Python Tutor](https://pythontutor.com/visualize.html#mode=edit)
  - Python tutor was used to visualize the python code and identify any error.


## Issues and Resolutions

- Error message appeared when I was making migration after creating models for menu app.
  - this was an easy fix as error message was clearly indicating that project required to install Pillow in order to complete migration therefore I ran pip3 install Pillow command in my terminal to install Pillow and re ran makemigration command, once Pillow installed I did not see any error message while making migrations.

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

- I was testing my live site after creating menu app and during test images used on menu template did not displayed on browser however alt attributes were working fine, in this case I thought it was definitely naming mismatch and start cross checking the images name however I couldnt see any error on this. Finally after doing some resaerch on ***how to render images using django*** I understood that my template required image url as I had imageField in my model/database and this required to supply image url while passing to template. I have updated image url to my template accordingly and this fixed issue.
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
   - I then did further research on the console error and found that I needed to ***update the CDN for jQuery*** on my file, I was using ***slim version of jQuery*** which was causing an issue as only full version of jQuery support animation effects. I have then replaced slim version on jQuery CDN with full version which then solved my problem.

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

- Issue with form field on Profile app: after building the functionality to store and display user profile, I was testing the functionality on the live site and spotted 2 issues as below :
  - Full name field and address field on the form appeared empty once info saved to profile and viewed from my profile option
    - I checked for any possible error on speeling and assigned value on forms.py, models.py and views.py however couldnt see any issue. I then run some print statement on address and full name field and noticed nothing printed on terminal, I then check on my weebhook view and JS code. somehow I have noticed that I had naming mismatch on couple of field for address and fullname, also i was using incorrect get method to retrive the user's name so I had to correct all the address mismatch and update get method, after this process I saw that details were printed on terminal and upadted on profile accordingly.

  - Placeholders text on the profile page form were not showing for address and contact number field.
    - I have checked all the possible errors on my view and form and couldnt spot any issue, I have then did plenty of research on google/slack but no tips found. Thanks to tutor support team from CI who advised me to check the indentation, indeed It was just as very silly error on form.py as I intended the if block incorrectly which resulted this issue and resolved once indentation fixed.

- Issue on admin profile while adding the item image: while admin adding the new item to the page I created an option to add the item without any image too however in this case default image should be displayed on the page indicating item has no image but this process failed while testing and default image did not showed on the item image. I built an if statement on all image tag to ensure default image to be only display if item has no image but for some reason this failed.
  - First this for at this stage was to check django setting for MEDIA_URL variable as this variable was used in template fo no image, I then checked any possible issue on if/else block and across all the settings and view but couldnt see any issue. Upon checking on Slack/Google and stack overflow I have seen plenty of post related to this issue however none of the post helped me as I had all setting correct. Finally I decided to check on the Django documantation page and [I found the solution over there](https://docs.djangoproject.com/en/3.2/ref/settings/), I simply needed to add below to the context_processors of my django setting
    ```
    'django.template.context_processors.media',
    ```

- [404 error](media/bugs/heroku404.jpg) while opening the app from heroku after deployed. 
  - Since it's "no item matches the given query" and request url is the home page, any chance I may have deleted a product that may have still been in the cart? If so, the steps below should help:
    - open up Dev Tools, go to the Application tab, select Storage from the sidebar, then click the "Clear Site Data" button, it fixed the issue by emptying cart (use deployed site to Clear site data)

- Image on nav-brand did not displayed on deployed site however it was shown on production mode, Checked file name, path and also checked on AWS S3 to ensure right image was uploaded with right image name and it was also satisfactory. Issue was causing due to incorrect file path on img tag ( [django setting for MEDIA_URL variable](media/bugs/django-setting.jpg) did not match with image file path) which ressolved as below:

    ```
      before:
      - <img class="card-img-top img-fluid main-logo " src="/media/logo1.png"

      after:
      - <img class="card-img-top img-fluid main-logo " src="{{ MEDIA_URL }}logo1.png"
    ```

- Django kept throwing an unexpected erron on several occasion such as : no-table found 
  - Issue solved after migrating the change to database by running commands below,
    - python3 manage.py makemigrations --dry-run
    - python3 manage.py makemigrations
    - python3 manage.py migrate

- Heroku Application Error while opening deployed App, which solved as below :
  - select app from heroku profile and select Overview option on dashboard, upon checking on the Dyno information, below status noticed
  ```
  gunicorn neupane_kitchen.wsgi:application           OFF 
  ```
  whcich meand no dynos were added
  - select Resource option on dashboard and dynos appeared there, clicked on pencil on the right hand side and select toggle to active dyno and confirm
  - Back to Overview and below were shown, this means dynos active and issue now ressolved.
    ```
  gunicorn neupane_kitchen.wsgi:application           ON
  ```


## Testing 
 -Website was tested through the build process using live browser and dev tool , additionally each pages were tested using Google Chrome, Microsoft edge and Safari. Also live pages were tested using Desktop, Laptop, iPhone, iPad and Android phone. Test document can be found here - [CLICK HERE TO VIEW](TEST.md)


## Deployment
- This project was initially set up on GitHub using the Code Institue Gitpod Template. I have used the Code Institute gitpod template and named my repository.
- After creating repository in github I then open the repository with Gitpod using green GitPod button on the github page.
- I then use gitpod terminal throughout the build process to install library/packages and to create folders and files
- git was used throughout the build process of this project as version control to Github
  - git add was used to add the files to staging area
  - git commit was used to commit my work with commit message
  - git push was used to updates my committed changes and allows send them to remote repository.

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


  
 #### Automatic Deploy to Heroku.
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


### Making a Local Clone 

   - Following setps required to clone the project to the local machine.
     - Log in to GitHub and locate the GitHub Repository
     - Under the repository name, click "Clone or download".
     - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
     - Open Git Bash on computer (Command Prompt can also be use instead of git bash) 
     - Change the current working directory to the location where you want the cloned directory to be made.
     - Type git clone, and then paste the URL you copied in Step 3.
        
        ```
        git clone https://github.com/shiva123-coder/neupane-kitchen.git
   
        ```

       - Press Enter. Your local clone will be created.
          
         ```
         Cloning into 'neupane-kitchen'...
         remote: Enumerating objects: 1061, done.
         remote: Counting objects: 100% (1061/1061), done.
         remote: Compressing objects: 100% (590/590), done.
         Receiving objects:  91% (966/10remote: Total 1061 (delta 521), reused 832 (delta 296), pack-reused 0
         Receiving objects:  92% (977/1061
         Receiving objects: 100% (1061/1061), 12.89 MiB | 7.06 MiB/s, done.
         Resolving deltas: 100% (521/521), done.

         ```


     - In order to use the full functionality of the site following environment variables must be set up

       - SECRET_KEY = <secret key>.

       - STRIPE_PUBLIC_KEY = <stripe public key>

       - STRIPE_SECRET_KEY = <stripe secret key>

       - STRIPE_WEBHOOK_SECRET = <stripe webhook secret>

       - IN_DEVELOPMENT = True
     
     - Additionally project required to install all the required packages and dependecies which can be installed by using the following command
      
       ```
       pip3 install -r requirements.txt

       ```


     - Last step is to migrate the models to set up database by using commands below
       
       ```
        python3 manage.py makemigrations --dry-run    # check 
        
        python3 manage.py makemigrations              # make migrations

        python3 manage.py migrate --plan              # check migration plan

        python3 manage.py migrate                     # migrate

       ```

     - Now project can be run by using the command below

       ```
       python3 manage.py runserver

       ```

## Amazon Web Service

  - AWS was used in this project to host static and media files for this project.
  - AWS account was creating by completing the sign-up process through the [AWS website](https://aws.amazon.com).

1.  Create the bucket
    - Below steps were taken to create the bucket
        - Create a new bucket on the AWS S3 service
        - From the main dashboard search for S3 and then select get started option
        - Select Create bucket button and give the bucket name and select your region
        - Uncheck the block public access and acknowledge that the bucket will now be public
        -  Select create bucket.
    
2. Bucket settings.
   - Select bucket properties settings and turn on static website hosting
   - Add index.html to index field and  and error.html to the error and save.

   - Select bucket Permissions settings now, click on the buckets Permissions tabs and add below config :
       ```
       [
          {
              "AllowedHeaders": [
                  "Authorization"
              ],
              "AllowedMethods": [
                  "GET"
              ],
              "AllowedOrigins": [
                  "*"
              ],
              "ExposeHeaders": []
          }
       ]

       ```
    - On the bucket policy option, click on generate policy and Select S3 bucket policy
    - Add * to the principal field to select all principals
    - Choose the action to get object.
    - Paste in your ARN which is available on the previous page.
    - Click, add statement
    - Then click, generate policy.
    - Now copy and paste your new policy into the bucket policy.
      ```
      {
         "Version": "2012-10-17",
         "Id": "Policy1635692466356",
         "Statement": [
            {
                  "Sid": "Stmt1635692462924",
                  "Effect": "Allow",
                  "Principal": "*",
                  "Action": [
                     "s3:GetObject",
                     "s3:PutObject",
                     "s3:DeleteObject"
                  ],
                  "Resource": "arn:aws:s3:::neupane-kitchen/*"
            }
         ]
      }

      ```

    - Add /* onto the end of the resources key
    - Click Save.
    - Access control list
    - In the access control list tab set the list objects permission to everyone.
    
3. Create a User

   - Back in the AWS main dashboard search for IAM and follow the process below : 
    - Firstly create a group to put user in.
    - Click create a new group and name it.
    - Click through to the end and save the group.
    - Create a policy.
    - In our group click, policy and then, create policy.
    - Select the JSON tab and then import managed policies.
    - Search S3 and select AmazonS3FullAccess and import.
    - In the resources section paste in our ARN from before.
    - click through to review the policy.
    - Fill in name and description and then click generate policy.
    - Back in your group click permission and then attach the policy.
    - Find the policy which is just created and attach it.
    

    - Select Users from the sidebar and then click, add user.
    - Create a user name and select programmatic access then click next.
    - Then select your group to add your user to.
    - Click through to the end and then click create user.
    - download the CVS file and save it as it contains the users keys

    (note: CVS file must be download and keep it safe/secret at this stage as after this process its not possible to download CVS file again)

4. Connecting to Django
  - Once AWS has been set up now this needs to be connect to Django. Steps below were taken to accomplish this.
   - Head up to the gitpod terminal and use below command to install ***boto3 and django storages*** packages

      ```
       pip3 install boto3
       pip3 install django-storages
      ``` 

    
   - Then freeze the requirements by using below command in the terminal
       ```
       pip3 freeze > requirements.txt
       ```
   - Back to the settings.py add some settings as below:
   - first add storages into installed apps in settings.py
   - Back to heroku setting scroll down to 'Reveal config var' and create an environmental variable "USE_AWS" and set it to True in order only run this code when on Heroku.
   - Now add below settings to the settings.py
    
       ```
           if "USE_AWS" in os.environ:

                # Bucket Config

                AWS_STORAGE_BUCKET_NAME = '<bucket name>'
                AWS_S3_REGION_NAME = '<your region>'
                AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
                AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
                AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

                # static and media file storage
                
                STATICFILES_STORAGE = 'custom_storages.StaticStorage'
                STATICFILES_LOCATION = 'static'
                DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
                MEDIAFILES_LOCATION = 'media'

                # Override static and media URLs in production

                STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
                MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

        ```
    
  - Create a custom_storages.py file on workspace to tell Django that in production we want to use s3 to store our static and media files.
  - import S3Boto3Storage to the top of the custom_storages.py file
  - Create new classes inside the custom_storages.py file and add location variable as below.


    ``` 
        class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION

        class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ```
  - All setup process has now completed.

5. Add media to AWS.
   - Below steps were taken to add the media to AWS
   - Head back to AWS s3 and create a new folder called media.
   - Select upload and add image files.
   - Then select to grant public access.
   - And then upload the files.
   


## Credit
- Thanks to JustDjango on their [youtube video](https://www.youtube.com/watch?v=cdRj9eNR0KI) on stripe payment, this video help me to understand the handling of validation and error while creating stripe payment functionality.


 - ***Code***
    - I have taken some CSS and JS code from CI walkthrough project and modified as per project requirement while creating loading spinner in checkout section of the project
    - I have taken the code from [stackoverflow](https://stackoverflow.com/questions/16344354/how-to-make-blinking-flashing-text-with-css-3) and modified as per my requirement while creating animation effect on my delivery promo text on Navbar.
    - I have taken code from [stack overflow post](https://stackoverflow.com/questions/63886066/redirect-back-to-previous-page-after-login-in-django-allauth) for login url on my comment section of blog and also for add review section on menu app, code was added to url in order to redirect the user to the same page once they logged in
- Thanks to [Stein for Youtube video](https://www.youtube.com/watch?v=m3hhLE1KR5Q) on Blog page, I took the concept from this video while making my blog app.
- Thanks to [ Coding Stuff for Youtube video](https://www.youtube.com/watch?v=reFJ9hBLFUY&t=632s) on Django, This video help me to gain some knowledge in details for creating review app.
- Thanks to CI on Boutique Ado video lesson, this video lesson helped me to understand the django concept and explanation on the video lessons were very helpful and easy to understand, additionally massive thanks to tutor Chris(ckz8780) for explaining the several tricks to solve the issue and build the logic.

## Media
- Most of the pictures for the project was taken from [Google](https://www.google.com/)
- I have also taken some of the pictures from [Stock Adobe](https://stock.adobe.com/)

## Acknowledgements
- I would like to thank my mentor Chris Quinn for his guidance and advice on this project.
- Thanks to everyone on Slack Community for always being on-hand with requests and support.
- Thanks to everyone on CI tutor support team for always providing with the support and guidance.
- Thanks to everyone from Student Care team (CI) for keeping me update with all changes such as tutor support availibility holiday period and most importantly checking regularly on my progress and always ready to support on my study.

## Disclaimer
- This website was build for educational purpose only