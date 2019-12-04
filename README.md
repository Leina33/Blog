# BLOG WEBSITE

A personal blogging website where you can create and share your opinions and other users can read and comment on them.

## Built By [DOMINIC RUTTO](https://github.com/Leina33/)
A personal blogging website where you can create and share your opinions and other users can read and comment on them. You can view the site at: https://blogruto.herokuapp.com/
## Description


## User Stories

These are the behaviours/features that the application implements for use by a user.
As a user I would like to:

- See the blogs other people posted
- signed in for me to leave a comment
- View the blogs i have created
- Comment on different blog posts and leave and leave a feedback
- Submit a blog in any category
- view different categories

## Specifications

| Behaviour                                  |            Input             |                                                               Output |
| :----------------------------------------- | :--------------------------: | -------------------------------------------------------------------: |
| Display comments                           |       **On page load**       |           List of various comments sources is displayed per category |
| Display comments from people who signed in |  **Click on Add comments**   |         Redirected to a page with a list of comments from the source |
| Display the pitches and comments           |       **On page load**       |                 Each pitch displays an title, description and author |
| Read an entire pitch                       | **pitch category sub-title** | Redirected to the picked category source's site to read entire pitch |
| Go back to pick category you need          |        **Click Home**        |                                  Redirected to the post a pitch area |

## SetUp / Installation Requirements

### Prerequisites

- python3.6
- pip
- virtualenv

### Cloning

- In your terminal:
  $ git clone https://github.com/Leina33/Blog.git
    

## Running the Application

- Creating the virtual environment
  $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/env
- Installing Flask and other Modules
  $ python3.6 -m pip install Flask
        $ python3.6 -m pip install Flask-Bootstrap
  $ python3.6  pip install flask-migrate
        $ python3.6 manage.py db init
  $ python3.6 manage.py db migrate -m "Initial Migration"
        $ python3.6 manage.py db upgrade
  $ pip install flask-SQLAlchemy
        $ pip install psycopg2
- To run the application, in your terminal:
  \$./start.sh or python3.6 manage.py server

## Testing the Application

- To run the tests for the class files:
  $ cd app
        $ python3.6 test_user.py

## Technologies Used

- Python3.6
- Flask

## License

MIT &copy;2019 [DOminic Rutto](https://github.com/Leina33)
BLOG- Is web application for users to express the blogs and interest about particular topics.
