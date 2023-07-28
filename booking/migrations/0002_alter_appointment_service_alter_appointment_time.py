# Generated by Django 4.0.1 on 2023-07-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='service',
            field=models.CharField(choices=[('General care doctor', 'General care doctor'), ('General surgery', 'General surgery'), ('Family medicine', 'Family medicine'), ('Emergency medicine', 'Emergency medicine'), ('Cardiology', 'Cardiology'), ('Obstetrics and gynaecology', 'Obstetrics and gynaecology'), ('Dermatology', 'Dermatology')], default='General care doctor', max_length=50),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.CharField(choices=[('12 PM', '12 PM'), ('12:30 PM', '12:30 PM'), ('2 PM', '2 PM'), ('2:30 PM', '2:30 PM'), ('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM')], default='3 PM', max_length=10),
        ),
    ]