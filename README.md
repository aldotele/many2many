## many2many
database design practice with many-to-many relationships and bridge tables

## How to launch
#### using Docker
from the root directory of the project, type on terminal:
`docker-compose build`\
`docker-compose up`

navigate to *localhost:8000* on your browser

#### without Docker (and with Python installed)
`pip install -r requirements.txt`\
`python manage.py migrate.py`
`python manage.py runserver`

navigate to *localhost:8000* on your browser