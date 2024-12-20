# Generated by Django 4.2.3 on 2023-07-28 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0003_book_uploaded_by_alter_book_pdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=100)),
                ('filiere', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('uploaded_by', models.CharField(blank=True, max_length=100, null=True)),
                ('user_id', models.CharField(blank=True, max_length=100, null=True)),
                ('pdf', models.FileField(upload_to='Bproject/pdf/')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_etudiant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf',
            field=models.FileField(upload_to='Bproject/pdf/'),
        ),
    ]