# Generated by Django 2.2.16 on 2021-07-25 12:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authService', '0003_delete_assignment'),
        ('classroom', '0002_auto_20210724_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authService.UserProfile')),
            ],
        ),
    ]