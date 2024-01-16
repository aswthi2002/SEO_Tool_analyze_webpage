
# SEO Tool for Live Web Page Analysis

A brief description of what this project does and who it's for



## Overview

 This project focuses on developing an SEO tool to analyze live web pages. The tool includes features such as user data storage, account creation with a user-friendly interface, password generation, login functionality, and the ability to inspect the code of a website using its URL. Additionally, users can change their username and password through an OTP (One-Time Password) generator, which sends the OTP to their email. The database is designed to facilitate efficient data management and uses user-defined functions to enhance code organization.


## Features

- User Account Management: User-friendly account creation, Password generation for enhanced security.
- Login Functionality: Users can log in to access the tool's features.
- Web Page Code Inspection: Retrieve and analyze the code used in a website by providing its URL.
- Username and Password Modification: Users can change their username and password.
- OTP Generator: Secure OTP generation for user authentication.
- Database Design: Efficient storage and retrieval of user data.



## Tech Stack

**Programming Language:** Python

**Database:** SQLite

**Modules and Functions:** Utilized user-defined functions for code modularity


## How to run

Create and insert data in the table

```bash
a.execute('create table ana(id int unique,username varchar(100),password varchar(100),email varchar(100),phone varchar(11))')
a.execute('insert into ana(id,username,password,email,phone) values(1,"your_name","1212","your_email@gmail.com","your_pass")')
```
Install dependencies

```bash
  pip install beautifulsoup4
  pip install random
  pip install smtplib
  pip install sqlite3

```
Check SMTP Authentication

```bash
  Check Credentials:
    Ensure that the email address and password (or App Password)   used for SMTP authentication are correct.
    If using an App Password, make sure it's generated correctly from your email provider's settings.

  Enable Less Secure App Access:
    For Gmail, if you're facing authentication issues, ensure that "Less secure app access" is turned on in your Google Account settings. Some email providers may have similar settings to allow less secure app access.
    
  Two-Factor Authentication (2FA):
    If you have two-factor authentication enabled for your email account, generate and use an App Password instead of your regular password for SMTP authentication
```


## License

[PSF](https://docs.python.org/3/license.html#psf-license)

