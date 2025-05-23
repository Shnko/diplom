# Generated by Django 5.2 on 2025-05-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_adoptionparent_options_alter_child_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannedRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('1', 'Врач'), ('2', 'Средний медицинский персонал'), ('3', 'Младший медицинский персонал'), ('4', 'Провизор'), ('5', 'Фармацевт'), ('6', 'Педагогический персонал'), ('7', 'Специалисты с высшим не медицинским образованием'), ('8', 'Прочий персонал')], verbose_name='категория')),
                ('count', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='количество')),
            ],
            options={
                'verbose_name': 'штатное расписание',
                'verbose_name_plural': 'штатное расписание',
            },
        ),
    ]
