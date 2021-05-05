# Camp Manager

## Quickstart

Copy `.env.template` and rename it to `.env`. Fill it with your details. Then:

```bash
poetry install
python manage.py migrate
python manage.py runserver
```

## Deployment

We've backported the Fabric resources found in Mezzanine 4.2. Follow Mezzanine's deployment documentation for that version: https://github.com/stephenmcd/mezzanine/blob/4.2.3/docs/deployment.rst
