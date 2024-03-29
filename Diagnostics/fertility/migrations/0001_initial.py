# Generated by Django 2.2.2 on 2019-07-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fertility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.PositiveIntegerField(choices=[(1, 'spring'), (2, 'fall'), (3, 'winter'), (4, 'summer')])),
                ('age', models.PositiveIntegerField()),
                ('childish_diseases', models.PositiveIntegerField(choices=[(0, 'no'), (1, 'yes')])),
                ('accident_or_serious_trauma', models.PositiveIntegerField(choices=[(0, 'no'), (1, 'yes')])),
                ('surgical_intervention', models.PositiveIntegerField(choices=[(0, 'no'), (1, 'yes')])),
                ('high_fevers_in_last_year', models.PositiveIntegerField(choices=[(1, 'more than 3 months ago'), (2, 'less than 3 months ago'), (3, 'no')])),
                ('frequency_of_alcohol_consumption', models.PositiveIntegerField(choices=[(1, 'once a week'), (2, 'hardly ever or never'), (3, 'several times a week'), (4, 'several times a day'), (5, 'every day')])),
                ('smoking_habit', models.PositiveIntegerField(choices=[(1, 'occasional'), (2, 'daily'), (3, 'never')])),
                ('no_of_hours_spent_sitting_per_day', models.PositiveIntegerField()),
                ('confidence', models.FloatField()),
            ],
        ),
    ]
