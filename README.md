# Camp Manager

A Django project on Python 3.

## Quickstart

Note: You will have to manually create `campmanager/local_settings.py`. Here's a template:

```python
# campmanager/local_settings.py

DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "<key>"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        # DB name or path to database file if using sqlite3.
        "NAME": "campmanager",
        # Not used with sqlite3.
        "USER": "campmanager",
        # Not used with sqlite3.
        "PASSWORD": "campmanager",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "127.0.0.1",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

ALLOWED_HOSTS = ["*"]

FABRIC = {
    "DEPLOY_TOOL": "git",  # Deploy with "git", "hg", or "rsync"
    "SSH_USER": "<user>",  # VPS SSH username
    "SSH_PASS": "<pass>",  # VPS SSH password
    "HOSTS": ["<ip>"],  # The IP address of your VPS
    "DOMAINS": ["<domain>"],  # Will be used as ALLOWED_HOSTS
    "REQUIREMENTS_PATH": "requirements.txt",  # Project's pip requirements
    "LOCALE": "es_ES.UTF-8",  # Should end with ".UTF-8"
    "DB_PASS": "<pass>",  # Live database password
    "SECRET_KEY": SECRET_KEY,
    "NUM_WORKERS": 2,

    "EMAIL_USER": "<email>",  # A Gmail account
    "EMAIL_PASS": "<pass>",
}
```

Once you have you've filled `local_settings.py` run:

```bash
# Clone the source from git, then...
cd campmanager

# Create campmanager/local_settings.py, then...

mkvirtualenv -p python3 campmanager
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Deployment

We've backported the Fabric resources found in Mezzanine 4.2. Follow Mezzanine's deployment documentation for that version: https://github.com/stephenmcd/mezzanine/blob/4.2.3/docs/deployment.rst
