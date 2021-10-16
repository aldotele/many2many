## many2many
database design practice with many-to-many relationships and bridge tables

## How to launch
#### using Docker
from the root directory of the project, type on terminal:\
`docker-compose build`\
`docker-compose up`

#### without Docker (and with Python installed)
`pip install -r requirements.txt`\
`python manage.py migrate.py`\
`python manage.py runserver`

after the previous steps, navigate either to *http://localhost:8000* or *http://127.0.0.1:8000/* on your browser.