# Build a web application using Django - OpenClassrooms project 9

This project is about developing a new web application enabling users to ask for or publish 
reviews about books and articles.

## Installation

Clone the repository on your computer.

```
git clone https://github.com/Bricevne/P9_LITReview.git
```

Set your virtual environment under python 3.10

```
python3 -m venv venv # Create the virtual environment and install the dependencies
source venv/bin/activate # Activate the virtual environment
```

Create a file where you'll put the django secret key:

```
touch .env # File for environment variables
```

Insert your django secret key in the .env file

`DJANGO_SECRET_KEY="DJANGO_SECRET_KEY"`



## Usage

Run the following code to access the web application:

```
python manage.py migrate # Create the migrations
python manage.py runserver # Start the local server
```

## License

MIT