# Rental System using Django Framework

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)

## Introduction
The Rental System Project is a web application built using the Django Framework. It provides a platform for managing and renting various items or services. This project is designed to streamline the process of renting and tracking items, making it efficient for both renters and owners.

## Features
- User authentication and authorization
- CRUD operations for users,vehicles and shop owners.
- Rental history tracking
- Responsive and user-friendly interface
- Payment integration for rental transactions

## Installation

Here are the steps to create the project:

1.Ensure that you have PyCharm IDE and PostgreSQL (PgAdmin) or MySQL installed on your computer.

2.To create a Django project in PyCharm:
  - Open the terminal and execute the command **pip install django** to download the Django 
    package.
  - Use the command **django-admin startproject projectname** to initiate a Django project.
  - Navigate to the project directory using the **cd projectname** command.
  - Create apps within the Django project using the command **django-admin startapp yourappname**.

3.After setting up the project and apps, go to the **settings.py** file inside your project. In the 'INSTALLED_APPS' section, include the apps of your project.

4.Include the app URLs in the project-level **urls.py** file (inside your project name directory).

5.Connect the PostgreSQL or MySQL database to the project. A code snippet for the 'DATABASES' setting is provided in **settings.py**. Ensure you enter your respective database details.

6.The project includes functionality for sending emails for forgotten passwords. At the bottom of settings.py, ensure you provide your email address along with the password.

7.Template creation:
  - Create a directory at the project level named 'templates.'
  - Inside the templates directory, create subdirectories with the names of your respective apps.
  - Within the app directories, create HTML files corresponding to each app.

8.Static directory:
  - This directory is for storing styles and images.
  - Similar to the templates directory, create a static directory at the project level.
  - Create subdirectories named - css, js, images.
  - Store styles.css, script.js, and images as needed.
  - Create **urls.py** inside apps as there will be no urls.py in the apps by default.
  - Optionally, include **forms.py** if necessary.

9.Create superuser:
  - Enter the command **python manage.py createsuperuser** in the terminal.
  - Then give your user details like username,email(optional) and password.
  - To access the administration page - ' /admin ' in the url in browser. Then login with the credentials that you have given in the terminal.

10.Makemigration and migrate:
  - After creating the models for the table creation, you have to run the commands **python manage.py makemigrations** and **python manage.py migrate** in the terminal.

11.Run the development server:
  - Run the project in the pycharm using the command **python manage.py runserver**.The command will access the application in your web browser at http://localhost:8000/
    

These steps are designed for beginners to create the project. Upon reviewing the repository, you will definitely understand the structure to be followed.

## Usage

1. **Admin Panel:**
   - Visit the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage users, items, and view rental history.

2. **Main Application:**
   - Explore the main application at [http://localhost:8000/](http://localhost:8000/) to browse and rent items.

## Technologies Used

The Rental System Project is built using the following technologies:

- **Django Framework:** The web framework for building robust and scalable web applications.
  
- **HTML, CSS, JavaScript:** Standard web technologies used for crafting the frontend interface and enhancing user interactivity.

- **Bootstrap:** A popular CSS framework utilized for styling, providing a responsive and visually appealing design.

- **SQLite:** The default database engine used for data storage. It can be changed in the project settings to suit specific requirements.


## Deployment

This project, the Rental System, has been successfully deployed on [PythonAnywhere](https://www.pythonanywhere.com/), a popular platform for hosting and deploying Python web applications.

### Project Deployment Link

The Rental System Project is accessible online at the following link: [http://sk7ayanokoji.pythonanywhere.com/](http://sk7ayanokoji.pythonanywhere.com/)

### Instructions for Accessing the Deployed Project:

1. Open your web browser and navigate to [http://sk7ayanokoji.pythonanywhere.com/](http://sk7ayanokoji.pythonanywhere.com/).

2. Explore the main application to browse and rent vehicles as per your requirements.
