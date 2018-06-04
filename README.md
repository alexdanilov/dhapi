# Restaurants API

### Installation

1. Setup environment `pipenv --python=3.6 && pipenv shell`
2. Install packages `pipenv install -r requirements.txt`
3. Create and fill database `python manage.py migrate && python manage.py loaddata initial_data`

### Run project
`python manage.py runserver`

### Run tests
`python manage.py test`


### Warnings
Project can accept html content type and display DjangoRestFramework UI for testing API via web.