from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("signup", "0004_camper_lawyer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="camper",
            name="registrar_position",
            field=models.CharField(
                help_text="Position at the municipality",
                max_length=100,
                verbose_name="Birth Certificate Registrar Position",
                blank=True,
            ),
        ),
    ]
