# Building a REST API. Application Architecture

## Objective

The goal of this assignment is to create a REST API for storing and managing contacts. The API should be built using the FastAPI framework and should utilize SQLAlchemy for database management.

## Technical Requirements

**1. Contacts**
To store contacts in your system, you need to design a database that includes all the necessary information.
The database should store:

- First Name
- Last Name
- Email Address
- Phone Number
- Date of Birth
- Additional Information (optional)

**2. API**
The API you develop should support basic data operations. Below is the list of actions your API must be able to perform:

- Create a new contact.
- Retrieve a list of all contacts.
- Retrieve a single contact by its ID.
- Update an existing contact.
- Delete a contact.

**3. CRUD API**

In addition to the basic CRUD functionality, the API should include the following features:

- Allow searching for contacts by first name, last name, or email address (using query parameters).
- Provide a list of contacts whose birthdays are within the next 7 days.

## General Requirements

1.  Use the FastAPI framework to build the API.
2.  Use SQLAlchemy ORM to interact with the database.
3.  Utilize PostgreSQL as the database.
4.  Support full CRUD operations for managing contacts.
5.  Include functionality to store the contact's date of birth.
6.  Provide auto-generated Swagger documentation for the REST API.
7.  Use Pydantic for data validation.
