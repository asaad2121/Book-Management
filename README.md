# Book-Management

### Table of Contents
- [Steps for running project](#steps-for-running-project)
 * [Clone Project](#clone-repository)
 * [Environment Setup](#environment-setup)
 * [Installation of Dependencies](#installation-of-dependencies)
 * [Migrations and SuperUser](#migrations-and-superuser)
 * [Running Server](#running-django-server)
- [Import Scripts](#import-scripts)
 * [To Run Import Author](#to-run-import-author)
 * [To Run Import Books](#to-run-import-books)
- [Postman API](#postman-api)
    

### Steps for running project:

##### Clone Repository:
```bash
git clone https://github.com/asaad2121/Book-Management.git
cd genebox
```

##### Environment Setup:

```bash
pip install virtualenv
virtualenv venv
```
##### Installation of Dependencies:

```bash
source venv/bin/activate
pip install -r requirements.txt
```

##### Migrations and SuperUser
```bash
source venv/bin/activate
source .env
python manage.py migrate
python manage.py createsuperuser
```

##### Running Django Server:

```bash
source venv/bin/activate
source .env
python manage.py runserver
```

### Import Scripts 

The scripts for import Author via CSV and import Books via CSV is stored in the main directory.

##### To Run Import Author
```bash
python .\author_import_csv_data.py
```
```bash
C:\Django\genebox\test\author_test.csv
```
It will look something like this!

![image](https://res.cloudinary.com/gdscrgit/image/upload/v1669574468/samples/import_csv_author_giloqx.png)



##### To Run Import Books
```bash
python .\book_import_csv_data.py
```
```bash
C:\Django\genebox\test\book_test.csv
```
It will look something like this!

![image]() Image link here

### Postman API
Follow these steps to run API via Postman
