# Generated by Django 3.2.9 on 2021-12-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('holders', '0007_auto_20211210_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=50, verbose_name='SIGLA')),
                ('name', models.CharField(max_length=200, verbose_name='NOME')),
            ],
        ),
        migrations.AddField(
            model_name='holder',
            name='society',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='holders.society', verbose_name='Sociedade'),
            preserve_default=False,
        ),
    ]