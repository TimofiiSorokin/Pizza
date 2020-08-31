# Generated by Django 3.1 on 2020-08-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='photo')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='name')),
                ('dough', models.CharField(choices=[('тонкое', 'тонкое'), ('традиционное', 'традиционное')], default='FREE', max_length=30, verbose_name='dough')),
                ('size', models.CharField(choices=[('26 см', '26 см'), ('30 см', '30 см'), ('40 см', '40 см')], default='FREE', max_length=30, verbose_name='size')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
            ],
            options={
                'verbose_name_plural': 'Catalog',
            },
        ),
    ]