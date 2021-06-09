# django-blog
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

pet-project to learn django

---
### Install
Run the following commands in the shell:
```shell
git clone https://github.com/dimmy2000/django-blog.git
cd django-blog
pip install --user poetry
poetry shell && poetry install
```

After the poetry environment is set up, run command `pre-commit install` in the shell.

Create `.env` file and fill the following variables with your own values:
```dotenv
SECRET_KEY=your-own-top-secret-phrase-thank-you-very-much
DEBUG=true
```
### Launch

Run the following commands in the shell:
```shell
python manage.py migrate
python manage.py runserver
```
Now you can find test server at http://localhost:8000/ or http://127.0.0.1:8000/
