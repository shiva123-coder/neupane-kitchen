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

- I was testing my live site after creating menu app,and during test images passed on menu template did not displayed on browser however alt attributes were working fine , in this case I thought it was definitely naming mismatch and start cross checking the images name however I couldnt see any error on this. Finally after doing some resaerch on *** how to render images using django *** I understood that my template required image url as I had imageField in my model/database and this required to supply image url while passing to template. I have updated image url to my template accordingly and this fixed issue.
```
before
  <img class="card-img-top img-fluid" src="{{ item.image }}" alt="{{ item.name }}">

after
  <img class="card-img-top img-fluid" src="{{ item.image.url }}" alt="{{ item.name }}">
```