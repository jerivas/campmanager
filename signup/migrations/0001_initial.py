# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('logistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('birth_date', models.DateTimeField(help_text='The format is YYYY-MM-DD and 24 hour time.', null=True, verbose_name='Birth Date', blank=True)),
                ('state', models.CharField(blank=True, max_length=3, verbose_name='State', choices=[(b'ahu', b'Ahuachap\xc3\xa1n'), (b'cab', b'Caba\xc3\xb1as'), (b'cha', b'Chalatenango'), (b'cus', b'Cuscatl\xc3\xa1n'), (b'lal', b'La Libertad'), (b'lap', b'La Paz'), (b'lau', b'La Uni\xc3\xb3n'), (b'mor', b'Moraz\xc3\xa1n'), (b'saa', b'Santa Ana'), (b'sam', b'San Miguel'), (b'sas', b'San Salvador'), (b'sav', b'San Vicente'), (b'son', b'Sonsonate'), (b'usu', b'Usulut\xc3\xa1n')])),
                ('province', models.CharField(max_length=32, verbose_name='Province', blank=True)),
                ('occupation', models.CharField(max_length=32, verbose_name='Occupation', blank=True)),
                ('lawyer', models.CharField(blank=True, max_length=16, verbose_name='Assigned Lawyer', choices=[(b'jorge', b'Jorge Alberto Mart\xc3\xadnez Mart\xc3\xadnez'), (b'silvia', b'Silvia Anabel Morales de Mart\xc3\xadnez')])),
                ('passport', models.CharField(max_length=16, verbose_name='Passport Number', blank=True)),
                ('birth_cert_num', models.PositiveIntegerField(null=True, verbose_name='Birth Certificate Number', blank=True)),
                ('birth_cert_fol', models.PositiveIntegerField(null=True, verbose_name='Birth Certificate Folio', blank=True)),
                ('birth_cert_book', models.PositiveIntegerField(null=True, verbose_name='Birth Certificate Book', blank=True)),
                ('registrar', models.CharField(max_length=256, verbose_name='Birth Certificate Registrar', blank=True)),
                ('registrar_title', models.CharField(blank=True, max_length=16, verbose_name='Birth Certificate Registrar Title', choices=[(b'm', 'Mr.'), (b'f', 'Mrs.')])),
                ('registrar_position', models.CharField(blank=True, max_length=16, verbose_name='Birth Certificate Registrar Position', choices=[(b'chief', 'Chief'), (b'subchief', 'Subchief')])),
                ('reg_state', models.CharField(blank=True, max_length=3, verbose_name='Registration State', choices=[(b'ahu', b'Ahuachap\xc3\xa1n'), (b'cab', b'Caba\xc3\xb1as'), (b'cha', b'Chalatenango'), (b'cus', b'Cuscatl\xc3\xa1n'), (b'lal', b'La Libertad'), (b'lap', b'La Paz'), (b'lau', b'La Uni\xc3\xb3n'), (b'mor', b'Moraz\xc3\xa1n'), (b'saa', b'Santa Ana'), (b'sam', b'San Miguel'), (b'sas', b'San Salvador'), (b'sav', b'San Vicente'), (b'son', b'Sonsonate'), (b'usu', b'Usulut\xc3\xa1n')])),
                ('reg_province', models.CharField(max_length=32, verbose_name='Registration Province', blank=True)),
                ('permission_status', models.IntegerField(default=0, max_length=1, verbose_name='Permission Status', choices=[(0, 'Incomplete Documentation'), (1, 'Ready to Print'), (2, 'Printed'), (3, 'Signed'), (4, 'Special Case')])),
                ('signed_up', models.BooleanField(default=False, verbose_name='Signed up')),
                ('balance', models.DecimalField(default=0, verbose_name='Balance', max_digits=5, decimal_places=2)),
                ('no_pay', models.BooleanField(default=False, help_text="Mark if this person is exempt of the camp's price", verbose_name="Doesn't pay")),
                ('badge_name', models.CharField(help_text='The name that appears in the badge.', max_length=64, verbose_name='Badge Name', blank=True)),
                ('cabin', models.CharField(blank=True, max_length=16, verbose_name='Cabin', choices=[(b'agape1', b'\xc3\x81gape 1'), (b'agape2', b'\xc3\x81gape 2'), (b'agape3', b'\xc3\x81gape 3'), (b'agape4', b'\xc3\x81gape 4'), (b'alfa', b'Alfa'), (b'anakaino1', b'Anakaino 1'), (b'anakaino2', b'Anakaino 2'), (b'anakaino3', b'Anakaino 3'), (b'anakaino4', b'Anakaino 4'), (b'armenia', b'Armenia'), (b'belen', b'Bel\xc3\xa9n'), (b'ebal', b'Ebal'), (b'gerizim', b'Gerizim'), (b'horeb1', b'Horeb 1'), (b'horeb2', b'Horeb 2'), (b'huespedes1', b'Hu\xc3\xa9spedes 1'), (b'huespedes2', b'Hu\xc3\xa9spedes 2'), (b'huespedes3', b'Hu\xc3\xa9spedes 3'), (b'juda', b'Jud\xc3\xa1'), (b'koinonia1', b'Koinon\xc3\xada 1'), (b'koinonia2', b'Koinon\xc3\xada 2'), (b'koinonia3', b'Koinon\xc3\xada 3'), (b'koinonia4', b'Koinon\xc3\xada 4'), (b'moab', b'Moab'), (b'moria', b'Moria'), (b'nueva1', b'Nueva 1'), (b'nueva2', b'Nueva 2'), (b'nueva3', b'Nueva 3'), (b'nueva4', b'Nueva 4'), (b'omega', b'Omega'), (b'pastorales', b'Pastorales'), (b'peniel', b'Peniel'), (b'sinai', b'Sina\xc3\xad')])),
                ('generation', models.PositiveIntegerField(max_length=1, verbose_name='Generation', choices=[(1, b'Jos\xc3\xadas 1'), (2, b'Jos\xc3\xadas 2'), (3, b'Freshmen'), (4, b'Sophomores'), (5, b'Juniors'), (6, b'Seniors')])),
                ('structure', models.CharField(blank=True, max_length=16, verbose_name='Structure', choices=[(b'preju', b'Preju'), (b'josias', b'Jos\xc3\xadas')])),
                ('bus', models.CharField(blank=True, max_length=16, verbose_name='Bus', choices=[(b'1', b'Bus 1'), (b'2', b'Bus 2'), (b'3', b'Bus 3'), (b'4', b'Bus 4')])),
            ],
            options={
                'ordering': ['first_surname'],
                'abstract': False,
                'verbose_name_plural': 'Campers',
                'verbose_name': 'Camper',
                'permissions': (('generate_permission', 'Generate Permission'),),
            },
        ),
        migrations.CreateModel(
            name='Counselor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('signed_up', models.BooleanField(default=False, verbose_name='Signed up')),
                ('balance', models.DecimalField(default=0, verbose_name='Balance', max_digits=5, decimal_places=2)),
                ('no_pay', models.BooleanField(default=False, help_text="Mark if this person is exempt of the camp's price", verbose_name="Doesn't pay")),
                ('badge_name', models.CharField(help_text='The name that appears in the badge.', max_length=64, verbose_name='Badge Name', blank=True)),
                ('cabin', models.CharField(blank=True, max_length=16, verbose_name='Cabin', choices=[(b'agape1', b'\xc3\x81gape 1'), (b'agape2', b'\xc3\x81gape 2'), (b'agape3', b'\xc3\x81gape 3'), (b'agape4', b'\xc3\x81gape 4'), (b'alfa', b'Alfa'), (b'anakaino1', b'Anakaino 1'), (b'anakaino2', b'Anakaino 2'), (b'anakaino3', b'Anakaino 3'), (b'anakaino4', b'Anakaino 4'), (b'armenia', b'Armenia'), (b'belen', b'Bel\xc3\xa9n'), (b'ebal', b'Ebal'), (b'gerizim', b'Gerizim'), (b'horeb1', b'Horeb 1'), (b'horeb2', b'Horeb 2'), (b'huespedes1', b'Hu\xc3\xa9spedes 1'), (b'huespedes2', b'Hu\xc3\xa9spedes 2'), (b'huespedes3', b'Hu\xc3\xa9spedes 3'), (b'juda', b'Jud\xc3\xa1'), (b'koinonia1', b'Koinon\xc3\xada 1'), (b'koinonia2', b'Koinon\xc3\xada 2'), (b'koinonia3', b'Koinon\xc3\xada 3'), (b'koinonia4', b'Koinon\xc3\xada 4'), (b'moab', b'Moab'), (b'moria', b'Moria'), (b'nueva1', b'Nueva 1'), (b'nueva2', b'Nueva 2'), (b'nueva3', b'Nueva 3'), (b'nueva4', b'Nueva 4'), (b'omega', b'Omega'), (b'pastorales', b'Pastorales'), (b'peniel', b'Peniel'), (b'sinai', b'Sina\xc3\xad')])),
                ('generation', models.PositiveIntegerField(max_length=1, verbose_name='Generation', choices=[(1, b'Jos\xc3\xadas 1'), (2, b'Jos\xc3\xadas 2'), (3, b'Freshmen'), (4, b'Sophomores'), (5, b'Juniors'), (6, b'Seniors')])),
                ('structure', models.CharField(blank=True, max_length=16, verbose_name='Structure', choices=[(b'preju', b'Preju'), (b'josias', b'Jos\xc3\xadas')])),
                ('bus', models.CharField(blank=True, max_length=16, verbose_name='Bus', choices=[(b'1', b'Bus 1'), (b'2', b'Bus 2'), (b'3', b'Bus 3'), (b'4', b'Bus 4')])),
                ('small_group', models.OneToOneField(verbose_name='Small Group', to='logistics.SmallGroup')),
            ],
            options={
                'ordering': ['first_surname'],
                'abstract': False,
                'verbose_name': 'Counselor',
                'verbose_name_plural': 'Counselors',
            },
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('signed_up', models.BooleanField(default=False, verbose_name='Signed up')),
                ('balance', models.DecimalField(default=0, verbose_name='Balance', max_digits=5, decimal_places=2)),
                ('no_pay', models.BooleanField(default=False, help_text="Mark if this person is exempt of the camp's price", verbose_name="Doesn't pay")),
                ('badge_name', models.CharField(help_text='The name that appears in the badge.', max_length=64, verbose_name='Badge Name', blank=True)),
                ('cabin', models.CharField(blank=True, max_length=16, verbose_name='Cabin', choices=[(b'agape1', b'\xc3\x81gape 1'), (b'agape2', b'\xc3\x81gape 2'), (b'agape3', b'\xc3\x81gape 3'), (b'agape4', b'\xc3\x81gape 4'), (b'alfa', b'Alfa'), (b'anakaino1', b'Anakaino 1'), (b'anakaino2', b'Anakaino 2'), (b'anakaino3', b'Anakaino 3'), (b'anakaino4', b'Anakaino 4'), (b'armenia', b'Armenia'), (b'belen', b'Bel\xc3\xa9n'), (b'ebal', b'Ebal'), (b'gerizim', b'Gerizim'), (b'horeb1', b'Horeb 1'), (b'horeb2', b'Horeb 2'), (b'huespedes1', b'Hu\xc3\xa9spedes 1'), (b'huespedes2', b'Hu\xc3\xa9spedes 2'), (b'huespedes3', b'Hu\xc3\xa9spedes 3'), (b'juda', b'Jud\xc3\xa1'), (b'koinonia1', b'Koinon\xc3\xada 1'), (b'koinonia2', b'Koinon\xc3\xada 2'), (b'koinonia3', b'Koinon\xc3\xada 3'), (b'koinonia4', b'Koinon\xc3\xada 4'), (b'moab', b'Moab'), (b'moria', b'Moria'), (b'nueva1', b'Nueva 1'), (b'nueva2', b'Nueva 2'), (b'nueva3', b'Nueva 3'), (b'nueva4', b'Nueva 4'), (b'omega', b'Omega'), (b'pastorales', b'Pastorales'), (b'peniel', b'Peniel'), (b'sinai', b'Sina\xc3\xad')])),
            ],
            options={
                'ordering': ['first_surname'],
                'abstract': False,
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=64, verbose_name='First Name')),
                ('second_name', models.CharField(max_length=64, verbose_name='Second Name', blank=True)),
                ('first_surname', models.CharField(max_length=64, verbose_name='First Surname')),
                ('second_surname', models.CharField(max_length=64, verbose_name='Second Surname', blank=True)),
                ('gender', models.CharField(max_length=1, verbose_name='Gender', choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('birth_date', models.DateTimeField(help_text='The format is YYYY-MM-DD and 24 hour time.', null=True, verbose_name='Birth Date', blank=True)),
                ('state', models.CharField(blank=True, max_length=3, verbose_name='State', choices=[(b'ahu', b'Ahuachap\xc3\xa1n'), (b'cab', b'Caba\xc3\xb1as'), (b'cha', b'Chalatenango'), (b'cus', b'Cuscatl\xc3\xa1n'), (b'lal', b'La Libertad'), (b'lap', b'La Paz'), (b'lau', b'La Uni\xc3\xb3n'), (b'mor', b'Moraz\xc3\xa1n'), (b'saa', b'Santa Ana'), (b'sam', b'San Miguel'), (b'sas', b'San Salvador'), (b'sav', b'San Vicente'), (b'son', b'Sonsonate'), (b'usu', b'Usulut\xc3\xa1n')])),
                ('province', models.CharField(max_length=32, verbose_name='Province', blank=True)),
                ('occupation', models.CharField(max_length=32, verbose_name='Occupation', blank=True)),
                ('gov_id', models.CharField(max_length=10, verbose_name='ID Number', validators=[django.core.validators.RegexValidator(regex=b'^\\d{8}-\\d$', message='Invalid Government ID')])),
                ('known_as', models.CharField(max_length=255, verbose_name='Known as', blank=True)),
            ],
            options={
                'ordering': ['first_surname'],
                'abstract': False,
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receipt_id', models.CharField(unique=True, max_length=16, verbose_name='Receipt ID')),
                ('payment_date', models.DateField(null=True, verbose_name='Date', blank=True)),
                ('amount', models.DecimalField(verbose_name='Amount', max_digits=5, decimal_places=2)),
                ('notes', models.CharField(max_length=256, verbose_name='Notes', blank=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['-receipt_id'],
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.AlterUniqueTogether(
            name='parent',
            unique_together=set([('second_surname', 'first_surname', 'first_name', 'second_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='guest',
            unique_together=set([('second_surname', 'first_surname', 'first_name', 'second_name')]),
        ),
        migrations.AddField(
            model_name='camper',
            name='counselor',
            field=models.ForeignKey(verbose_name='Counselor or Small Group', to='signup.Counselor'),
        ),
        migrations.AddField(
            model_name='camper',
            name='father',
            field=models.ForeignKey(related_name='fathered', verbose_name='Father', blank=True, to='signup.Parent', null=True),
        ),
        migrations.AddField(
            model_name='camper',
            name='mother',
            field=models.ForeignKey(related_name='mothered', verbose_name='Mother', blank=True, to='signup.Parent', null=True),
        ),
        migrations.AddField(
            model_name='camper',
            name='small_group',
            field=models.ForeignKey(verbose_name='Small Group', blank=True, to='logistics.SmallGroup', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='counselor',
            unique_together=set([('second_surname', 'first_surname', 'first_name', 'second_name')]),
        ),
        migrations.AlterUniqueTogether(
            name='camper',
            unique_together=set([('second_surname', 'first_surname', 'first_name', 'second_name')]),
        ),
    ]
