from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logistics", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="smallgroup",
            name="generation",
            field=models.PositiveIntegerField(
                default=1,
                verbose_name="Generation",
                choices=[
                    (1, "Josías 1"),
                    (2, "Josías 2"),
                    (3, "Freshmen"),
                    (4, "Sophomores"),
                    (5, "Juniors"),
                    (6, "Seniors"),
                ],
            ),
        ),
    ]
