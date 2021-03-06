from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0005_auto_20150522_2307"),
    ]

    operations = [
        migrations.AddField(
            model_name="camper",
            name="fined",
            field=models.BooleanField(
                default=False,
                help_text="This person must pay a fine",
                verbose_name="Fined",
            ),
        ),
        migrations.AddField(
            model_name="counselor",
            name="fined",
            field=models.BooleanField(
                default=False,
                help_text="This person must pay a fine",
                verbose_name="Fined",
            ),
        ),
        migrations.AddField(
            model_name="guest",
            name="fined",
            field=models.BooleanField(
                default=False,
                help_text="This person must pay a fine",
                verbose_name="Fined",
            ),
        ),
    ]
