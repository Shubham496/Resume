# Generated manually after removing skill proficiency scores from the resume.

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_certification_remove_project_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='level',
        ),
    ]
