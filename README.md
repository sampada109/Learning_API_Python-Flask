# Learning APIs with Python Flask

This repository is dedicated to my journey of learning how to build APIs using Python Flask. As I progress through various concepts and implementations, I will document my steps and learnings in this README file.

In this we will take an example of Cafe Management , where we will create API Endpoints for different operations such as-
- GET Items: Retrieving all the items.
- GET Item: Retrieving any single item that user want to fetch.
- POST Item: Adding items to existing data.
- PUT Item: Updating any existing item.
- DELETE Item: Deleting any item.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Learning Steps](#learning-steps)
  - [Step 1: Setting up the Project](#step-1-setting-up-the-project)
  - [Step 2: Creating the Flask App](#step-2-creating-the-flask-app)
  - [Step 3: Creating First API  Endpoint (GET ITEMS)](#step-3-creating-first-api-endpoint)

- [Resources](#resources)

## Installation

(This section will be updated with installation instructions as we progress)

## Usage

(This section will be updated with usage instructions as we progress)

## Learning Steps

### Step 1: Setting up the Project

1. Created a new directory for the project on my computer.
2. Initialized a new Git repository:
```git init```
3. Created a `README.md` file to document the project.
4. Created and activated a new virtual environment:

- Creating: ```python -m venv venv```
- Activating(on windows): ```.venv/Scripts/activate```
5. Created a `requirements.txt` file and added Flask as a dependency.
6. Installed the project dependencies: ```pip install -r requirements.txt```

### Step 2: Creating the Flask App

1. Created an `app.py` file to write the Flask code for the REST API.
2. In `app.py`, imported the Flask class from flask module and created a new Flask application instance ( app = Flask() ).
3. Running the `app.py` file in terminal : ```flask run```
4. When file will run, url will be provided which we can open on any browser.
5. **404 error will occur means there is no page found, But in this case it's fine because we have not define any route or view function in our app.py file to shown anything.

- SOME IMPORTANT SETUP (you might find helpfull)

### Step 3: Creating First API Endpoint (GET Items)


1. In `app.py`, I have created a list of dictionary, where I will store different items. Each dictionary will have 2 keys value pair- name & price for each item.
2. Then I have created a route for retrieving all cafe items using a decorator (e.g., `@app.route('/getmenu')`).
3. Defined a function to handle GET requests to the `/getmenu` route.
5. Returned a JSON response containing the list of cafe items.


## Testing with Postman:

- While it's straightforward to fetch items using a browser for a GET request, but testing other functionalities like adding, updating, or deleting can be complicated and thus requires a more robust tool. This is where Postman comes in.
- Postman is a popular for testing API, that allows you to easily:
1. Send HTTP requests: You can construct and send various types of HTTP requests (GET, POST, PUT, DELETE) to your API endpoints.
2. Set request parameters: Postman enables you to define headers, body parameters, and URL parameters for your requests, mimicking real-world usage scenarios.
3. View and analyze responses: Postman displays the response status code, headers, and body content, allowing you to verify if your API is functioning as expected.

- ### Using Postman to Test Our API:
1. Download and install Postman https://www.postman.com/.
2. OR you can install its extension in VSCode directly.
3. Create a new collection/Folder, then add Request(there will options for different request method).
4. Select a GET request, add the `base url(http://127.0.0.1:5000)` and extend it with `/getmenu` endpoint to retrieve the list of cafe items.
5. Send the request and observe the response in Postman. You should see the JSON response containing the list of items.
6. You can also save the request and create a new request for another endpoint.


## Resources

(List any resources, tutorials, or documentation used so far)

