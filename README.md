# Build a web application using Django - OpenClassrooms project 9

This project is about developing a new web application enabling users to ask for or publish 
reviews about books and articles.

## Installation

Clone the repository on your computer.

`git clone https://github.com/Bricevne/P9_LITReview.git` 

Set your virtual environment under python 3.10

Create the virtual environment and install the dependencies:

`python3 -m venv venv` 

Activate the virtual environment:

`source venv/bin/activate`

Install the necessary libraries in the virtual environment:

`pip install -r requirements.txt`

Create a file where you'll put the django secret key:

`touch .env`
`DJANGO_SECRET_KEY="DJANGO_SECRET_KEY"`

## Usage

Run the following code to access the web application:

`python manage.py migrate # create the migrations`
`python manage.py runserver # start the local server`

## License

MIT