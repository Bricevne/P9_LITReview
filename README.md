# Build a web application using Django - OpenClassrooms project 9

This project is about developing a new web application enabling users to ask for or publish 
reviews about books and articles.

It also offers:
* an authentication app for authentication purposes
* a subscription app which permits users to follow others in order to read their tickets and
reviews in their own feed

You can access a feed page to read all tickets and reviews from the people you follow, a "posts" page to find all your 
own posts, a subscription page to follow other users as well as a profile page to change your password.

## Installation

Clone [the repository](https://github.com/Bricevne/P9_LITReview) on your computer.

```
git clone https://github.com/Bricevne/P9_LITReview.git
```

Set your virtual environment under [python 3.10](https://www.python.org/downloads/release/python-3100/)

```bash
python3 -m venv venv # Create the virtual environment and install the dependencies
source venv/bin/activate # Activate the virtual environment
```

Create a file where you'll put the django secret key:

```bash
touch .env # File for environment variables
```

Insert your django secret key in the .env file

`DJANGO_SECRET_KEY="DJANGO_SECRET_KEY"`



## Usage

Run the following code to access the web application:

```bash
python manage.py migrate # Create the migrations
python manage.py runserver # Start the local server
```

You can then access the website with http://127.0.0.1:8000/

## License

[MIT](https://choosealicense.com/licenses/mit/)
