import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("logistics", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Camper",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=64, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        max_length=64, verbose_name="Second Name", blank=True
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=64, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        max_length=64, verbose_name="Second Surname", blank=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        verbose_name="Gender",
                        choices=[("m", "Male"), ("f", "Female")],
                    ),
                ),
                (
                    "birth_date",
                    models.DateTimeField(
                        help_text="The format is YYYY-MM-DD and 24 hour time.",
                        null=True,
                        verbose_name="Birth Date",
                        blank=True,
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ahu", "Ahuachap??n"),
                            ("cab", "Caba??as"),
                            ("cha", "Chalatenango"),
                            ("cus", "Cuscatl??n"),
                            ("lal", "La Libertad"),
                            ("lap", "La Paz"),
                            ("lau", "La Uni??n"),
                            ("mor", "Moraz??n"),
                            ("saa", "Santa Ana"),
                            ("sam", "San Miguel"),
                            ("sas", "San Salvador"),
                            ("sav", "San Vicente"),
                            ("son", "Sonsonate"),
                            ("usu", "Usulut??n"),
                        ],
                        max_length=3,
                        verbose_name="State",
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        max_length=32, verbose_name="Province", blank=True
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        max_length=32, verbose_name="Occupation", blank=True
                    ),
                ),
                (
                    "lawyer",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Assigned Lawyer",
                        choices=[
                            ("jorge", "Jorge Alberto Mart??nez Mart??nez"),
                            ("silvia", "Silvia Anabel Morales de Mart??nez"),
                        ],
                    ),
                ),
                (
                    "passport",
                    models.CharField(
                        max_length=16, verbose_name="Passport Number", blank=True
                    ),
                ),
                (
                    "birth_cert_num",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Birth Certificate Number", blank=True
                    ),
                ),
                (
                    "birth_cert_fol",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Birth Certificate Folio", blank=True
                    ),
                ),
                (
                    "birth_cert_book",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Birth Certificate Book", blank=True
                    ),
                ),
                (
                    "registrar",
                    models.CharField(
                        max_length=256,
                        verbose_name="Birth Certificate Registrar",
                        blank=True,
                    ),
                ),
                (
                    "registrar_title",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Birth Certificate Registrar Title",
                        choices=[("m", "Mr."), ("f", "Mrs.")],
                    ),
                ),
                (
                    "registrar_position",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Birth Certificate Registrar Position",
                        choices=[("chief", "Chief"), ("subchief", "Subchief")],
                    ),
                ),
                (
                    "reg_state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ahu", "Ahuachap??n"),
                            ("cab", "Caba??as"),
                            ("cha", "Chalatenango"),
                            ("cus", "Cuscatl??n"),
                            ("lal", "La Libertad"),
                            ("lap", "La Paz"),
                            ("lau", "La Uni??n"),
                            ("mor", "Moraz??n"),
                            ("saa", "Santa Ana"),
                            ("sam", "San Miguel"),
                            ("sas", "San Salvador"),
                            ("sav", "San Vicente"),
                            ("son", "Sonsonate"),
                            ("usu", "Usulut??n"),
                        ],
                        max_length=3,
                        verbose_name="Registration State",
                    ),
                ),
                (
                    "reg_province",
                    models.CharField(
                        max_length=32, verbose_name="Registration Province", blank=True
                    ),
                ),
                (
                    "permission_status",
                    models.IntegerField(
                        default=0,
                        max_length=1,
                        verbose_name="Permission Status",
                        choices=[
                            (0, "Incomplete Documentation"),
                            (1, "Ready to Print"),
                            (2, "Printed"),
                            (3, "Signed"),
                            (4, "Special Case"),
                        ],
                    ),
                ),
                (
                    "signed_up",
                    models.BooleanField(default=False, verbose_name="Signed up"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        default=0,
                        verbose_name="Balance",
                        max_digits=5,
                        decimal_places=2,
                    ),
                ),
                (
                    "no_pay",
                    models.BooleanField(
                        default=False,
                        help_text="Mark if this person is exempt of the camp's price",
                        verbose_name="Doesn't pay",
                    ),
                ),
                (
                    "badge_name",
                    models.CharField(
                        help_text="The name that appears in the badge.",
                        max_length=64,
                        verbose_name="Badge Name",
                        blank=True,
                    ),
                ),
                (
                    "cabin",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Cabin",
                        choices=[
                            ("agape1", "??gape 1"),
                            ("agape2", "??gape 2"),
                            ("agape3", "??gape 3"),
                            ("agape4", "??gape 4"),
                            ("alfa", "Alfa"),
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("armenia", "Armenia"),
                            ("belen", "Bel??n"),
                            ("ebal", "Ebal"),
                            ("gerizim", "Gerizim"),
                            ("horeb1", "Horeb 1"),
                            ("horeb2", "Horeb 2"),
                            ("huespedes1", "Hu??spedes 1"),
                            ("huespedes2", "Hu??spedes 2"),
                            ("huespedes3", "Hu??spedes 3"),
                            ("juda", "Jud??"),
                            ("koinonia1", "Koinon??a 1"),
                            ("koinonia2", "Koinon??a 2"),
                            ("koinonia3", "Koinon??a 3"),
                            ("koinonia4", "Koinon??a 4"),
                            ("moa", "Moa"),
                            ("moria", "Moria"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("nueva3", "Nueva 3"),
                            ("nueva4", "Nueva 4"),
                            ("omega", "Omega"),
                            ("pastorales", "Pastorales"),
                            ("peniel", "Peniel"),
                            ("sinai", "Sina??"),
                        ],
                    ),
                ),
                (
                    "generation",
                    models.PositiveIntegerField(
                        max_length=1,
                        verbose_name="Generation",
                        choices=[
                            (1, "Jos??as 1"),
                            (2, "Jos??as 2"),
                            (3, "Freshmen"),
                            (4, "Sophomores"),
                            (5, "Juniors"),
                            (6, "Seniors"),
                        ],
                    ),
                ),
                (
                    "structure",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Structure",
                        choices=[("preju", "Preju"), ("josias", "Jos??as")],
                    ),
                ),
                (
                    "bus",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Bus",
                        choices=[
                            ("1", "Bus 1"),
                            ("2", "Bus 2"),
                            ("3", "Bus 3"),
                            ("4", "Bus 4"),
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["first_surname"],
                "abstract": False,
                "verbose_name_plural": "Campers",
                "verbose_name": "Camper",
                "permissions": (("generate_permission", "Generate Permission"),),
            },
        ),
        migrations.CreateModel(
            name="Counselor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=64, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        max_length=64, verbose_name="Second Name", blank=True
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=64, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        max_length=64, verbose_name="Second Surname", blank=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        verbose_name="Gender",
                        choices=[("m", "Male"), ("f", "Female")],
                    ),
                ),
                (
                    "signed_up",
                    models.BooleanField(default=False, verbose_name="Signed up"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        default=0,
                        verbose_name="Balance",
                        max_digits=5,
                        decimal_places=2,
                    ),
                ),
                (
                    "no_pay",
                    models.BooleanField(
                        default=False,
                        help_text="Mark if this person is exempt of the camp's price",
                        verbose_name="Doesn't pay",
                    ),
                ),
                (
                    "badge_name",
                    models.CharField(
                        help_text="The name that appears in the badge.",
                        max_length=64,
                        verbose_name="Badge Name",
                        blank=True,
                    ),
                ),
                (
                    "cabin",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Cabin",
                        choices=[
                            ("agape1", "??gape 1"),
                            ("agape2", "??gape 2"),
                            ("agape3", "??gape 3"),
                            ("agape4", "??gape 4"),
                            ("alfa", "Alfa"),
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("armenia", "Armenia"),
                            ("belen", "Bel??n"),
                            ("ebal", "Ebal"),
                            ("gerizim", "Gerizim"),
                            ("horeb1", "Horeb 1"),
                            ("horeb2", "Horeb 2"),
                            ("huespedes1", "Hu??spedes 1"),
                            ("huespedes2", "Hu??spedes 2"),
                            ("huespedes3", "Hu??spedes 3"),
                            ("juda", "Jud??"),
                            ("koinonia1", "Koinon??a 1"),
                            ("koinonia2", "Koinon??a 2"),
                            ("koinonia3", "Koinon??a 3"),
                            ("koinonia4", "Koinon??a 4"),
                            ("moa", "Moa"),
                            ("moria", "Moria"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("nueva3", "Nueva 3"),
                            ("nueva4", "Nueva 4"),
                            ("omega", "Omega"),
                            ("pastorales", "Pastorales"),
                            ("peniel", "Peniel"),
                            ("sinai", "Sina??"),
                        ],
                    ),
                ),
                (
                    "generation",
                    models.PositiveIntegerField(
                        max_length=1,
                        verbose_name="Generation",
                        choices=[
                            (1, "Jos??as 1"),
                            (2, "Jos??as 2"),
                            (3, "Freshmen"),
                            (4, "Sophomores"),
                            (5, "Juniors"),
                            (6, "Seniors"),
                        ],
                    ),
                ),
                (
                    "structure",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Structure",
                        choices=[("preju", "Preju"), ("josias", "Jos??as")],
                    ),
                ),
                (
                    "bus",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Bus",
                        choices=[
                            ("1", "Bus 1"),
                            ("2", "Bus 2"),
                            ("3", "Bus 3"),
                            ("4", "Bus 4"),
                        ],
                    ),
                ),
                (
                    "small_group",
                    models.OneToOneField(
                        verbose_name="Small Group", to="logistics.SmallGroup"
                    ),
                ),
            ],
            options={
                "ordering": ["first_surname"],
                "abstract": False,
                "verbose_name": "Counselor",
                "verbose_name_plural": "Counselors",
            },
        ),
        migrations.CreateModel(
            name="Guest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=64, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        max_length=64, verbose_name="Second Name", blank=True
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=64, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        max_length=64, verbose_name="Second Surname", blank=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        verbose_name="Gender",
                        choices=[("m", "Male"), ("f", "Female")],
                    ),
                ),
                (
                    "signed_up",
                    models.BooleanField(default=False, verbose_name="Signed up"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        default=0,
                        verbose_name="Balance",
                        max_digits=5,
                        decimal_places=2,
                    ),
                ),
                (
                    "no_pay",
                    models.BooleanField(
                        default=False,
                        help_text="Mark if this person is exempt of the camp's price",
                        verbose_name="Doesn't pay",
                    ),
                ),
                (
                    "badge_name",
                    models.CharField(
                        help_text="The name that appears in the badge.",
                        max_length=64,
                        verbose_name="Badge Name",
                        blank=True,
                    ),
                ),
                (
                    "cabin",
                    models.CharField(
                        blank=True,
                        max_length=16,
                        verbose_name="Cabin",
                        choices=[
                            ("agape1", "??gape 1"),
                            ("agape2", "??gape 2"),
                            ("agape3", "??gape 3"),
                            ("agape4", "??gape 4"),
                            ("alfa", "Alfa"),
                            ("anakaino1", "Anakaino 1"),
                            ("anakaino2", "Anakaino 2"),
                            ("anakaino3", "Anakaino 3"),
                            ("anakaino4", "Anakaino 4"),
                            ("armenia", "Armenia"),
                            ("belen", "Bel??n"),
                            ("ebal", "Ebal"),
                            ("gerizim", "Gerizim"),
                            ("horeb1", "Horeb 1"),
                            ("horeb2", "Horeb 2"),
                            ("huespedes1", "Hu??spedes 1"),
                            ("huespedes2", "Hu??spedes 2"),
                            ("huespedes3", "Hu??spedes 3"),
                            ("juda", "Jud??"),
                            ("koinonia1", "Koinon??a 1"),
                            ("koinonia2", "Koinon??a 2"),
                            ("koinonia3", "Koinon??a 3"),
                            ("koinonia4", "Koinon??a 4"),
                            ("moa", "Moa"),
                            ("moria", "Moria"),
                            ("nueva1", "Nueva 1"),
                            ("nueva2", "Nueva 2"),
                            ("nueva3", "Nueva 3"),
                            ("nueva4", "Nueva 4"),
                            ("omega", "Omega"),
                            ("pastorales", "Pastorales"),
                            ("peniel", "Peniel"),
                            ("sinai", "Sina??"),
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["first_surname"],
                "abstract": False,
                "verbose_name": "Guest",
                "verbose_name_plural": "Guests",
            },
        ),
        migrations.CreateModel(
            name="Parent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=64, verbose_name="First Name"),
                ),
                (
                    "second_name",
                    models.CharField(
                        max_length=64, verbose_name="Second Name", blank=True
                    ),
                ),
                (
                    "first_surname",
                    models.CharField(max_length=64, verbose_name="First Surname"),
                ),
                (
                    "second_surname",
                    models.CharField(
                        max_length=64, verbose_name="Second Surname", blank=True
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        max_length=1,
                        verbose_name="Gender",
                        choices=[("m", "Male"), ("f", "Female")],
                    ),
                ),
                (
                    "birth_date",
                    models.DateTimeField(
                        help_text="The format is YYYY-MM-DD and 24 hour time.",
                        null=True,
                        verbose_name="Birth Date",
                        blank=True,
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ahu", "Ahuachap??n"),
                            ("cab", "Caba??as"),
                            ("cha", "Chalatenango"),
                            ("cus", "Cuscatl??n"),
                            ("lal", "La Libertad"),
                            ("lap", "La Paz"),
                            ("lau", "La Uni??n"),
                            ("mor", "Moraz??n"),
                            ("saa", "Santa Ana"),
                            ("sam", "San Miguel"),
                            ("sas", "San Salvador"),
                            ("sav", "San Vicente"),
                            ("son", "Sonsonate"),
                            ("usu", "Usulut??n"),
                        ],
                        max_length=3,
                        verbose_name="State",
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        max_length=32, verbose_name="Province", blank=True
                    ),
                ),
                (
                    "occupation",
                    models.CharField(
                        max_length=32, verbose_name="Occupation", blank=True
                    ),
                ),
                (
                    "gov_id",
                    models.CharField(
                        max_length=10,
                        verbose_name="ID Number",
                        validators=[
                            django.core.validators.RegexValidator(
                                regex="^\\d{8}-\\d$", message="Invalid Government ID"
                            )
                        ],
                    ),
                ),
                (
                    "known_as",
                    models.CharField(
                        max_length=255, verbose_name="Known as", blank=True
                    ),
                ),
            ],
            options={
                "ordering": ["first_surname"],
                "abstract": False,
                "verbose_name": "Parent",
                "verbose_name_plural": "Parents",
            },
        ),
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                (
                    "receipt_id",
                    models.CharField(
                        unique=True, max_length=16, verbose_name="Receipt ID"
                    ),
                ),
                (
                    "payment_date",
                    models.DateField(null=True, verbose_name="Date", blank=True),
                ),
                (
                    "amount",
                    models.DecimalField(
                        verbose_name="Amount", max_digits=5, decimal_places=2
                    ),
                ),
                (
                    "notes",
                    models.CharField(max_length=256, verbose_name="Notes", blank=True),
                ),
                ("object_id", models.PositiveIntegerField()),
                ("content_type", models.ForeignKey(to="contenttypes.ContentType")),
            ],
            options={
                "ordering": ["-receipt_id"],
                "verbose_name": "Payment",
                "verbose_name_plural": "Payments",
            },
        ),
        migrations.AlterUniqueTogether(
            name="parent",
            unique_together={
                ("second_surname", "first_surname", "first_name", "second_name")
            },
        ),
        migrations.AlterUniqueTogether(
            name="guest",
            unique_together={
                ("second_surname", "first_surname", "first_name", "second_name")
            },
        ),
        migrations.AddField(
            model_name="camper",
            name="counselor",
            field=models.ForeignKey(
                verbose_name="Counselor or Small Group", to="signup.Counselor"
            ),
        ),
        migrations.AddField(
            model_name="camper",
            name="father",
            field=models.ForeignKey(
                related_name="fathered",
                verbose_name="Father",
                blank=True,
                to="signup.Parent",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="camper",
            name="mother",
            field=models.ForeignKey(
                related_name="mothered",
                verbose_name="Mother",
                blank=True,
                to="signup.Parent",
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="camper",
            name="small_group",
            field=models.ForeignKey(
                verbose_name="Small Group",
                blank=True,
                to="logistics.SmallGroup",
                null=True,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="counselor",
            unique_together={
                ("second_surname", "first_surname", "first_name", "second_name")
            },
        ),
        migrations.AlterUniqueTogether(
            name="camper",
            unique_together={
                ("second_surname", "first_surname", "first_name", "second_name")
            },
        ),
    ]
