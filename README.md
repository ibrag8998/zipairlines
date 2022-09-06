# ZipAirlines

## How to Run

Code was written using Python 3.10. Also pip is required to run it.

```shell
git clone ...
cd zipairlines
pip install -r requirements.txt
cd web
python manage.py migrate
python manage.py runserver
```

## API Docs

- Swagger UI: http://localhost:8000/swagger/
- ReDoc: http://localhost:8000/redoc/

## Running Tests

```shell
cd web
python manage.py test
```

Coverage:

```shell
# to run tests
coverage run --source='.' manage.py test
# to get report into console
coverage report
# to get it in html form
coverage html
```
