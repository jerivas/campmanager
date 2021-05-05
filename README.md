# Camp Manager

## Quickstart

Copy `.env.template` and rename it to `.env`. Fill it with your details. Then:

```bash
poetry install
python manage.py migrate
python manage.py runserver
```

## Deployment

Set up a `dokku` remote and push to it.
