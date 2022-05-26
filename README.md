# Bank-Loan-Information-System

# TO SETUP DATABASE

1. If you don't have mysql download one and install.
2. Go to "edit system environmental variables".'
3. Click "environmental variables"
4. In "System Variables", click new.
5. Add 
        
        DATABASE_ENGINE=django.db.backends.mysql
        DATABASE_BANK=db_bank
        DATABASE_PASSWORD=password
        DATABASE_USER=db_username
6. Restart computer.


# IN MYSQL WORKBENCH

1. Click "local instance connection".
2. Create a new sql script.
3. Run 
        CREATE USER 'db_username'@'localhost' IDENTIFIED BY 'password';
        CREATE DATABASE db_bank;
        GRANT ALL PRIVILEGES ON * . * TO 'db_username'@'localhost';
        FLUSH PRIVILEGES;
4. If the code works, refresh schemas and you should be able to see "db_bank".


# TO SETUP APPLICATION

1. Make sure you are in the right directory.
2. Run "pipenv shell" to make virtual environent
3. Go to bank_loan_information_system directory.
4. Run "pip install -r requirements.txt"
5. Run "python manage.py makemigrations"
6. Run "python manage.py migrate"
7. Create superuser "python manage.py createsuperuser"
8. Run program "python manage.py runserver"
9. Go to admin page and login superuser
10. Create groups: "banker", "borrower", "hasbankaccount"
