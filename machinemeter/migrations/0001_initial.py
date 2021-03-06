# Generated by Django 2.1 on 2018-08-02 22:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('price_first', models.IntegerField()),
                ('price_after', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=[('min', 'minute'), ('hr', 'hour'), ('mm', 'millimetre'), ('cm', 'centimetre'), ('m', 'metre'), ('g', 'gram'), ('kg', 'kilogram'), ('l', 'litre')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='machinemeter.Machine')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
