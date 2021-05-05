from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0002_auto_20150522_1541"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camper",
            name="lawyer",
        ),
    ]
