# Generated by Django 5.0.6 on 2024-05-20 09:57

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funds', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('amount', models.IntegerField(null=True, verbose_name='Запланированная сумма')),
                ('image', models.ImageField(upload_to='collects/', verbose_name='Изображение')),
                ('completion_datetime', models.DateTimeField(null=True, verbose_name='Дата и время завершения')),
                ('occasion', models.CharField(choices=[('Свадьба', 'Wedding'), ('День рождения', 'Birthday'), ('Добро без повода', 'Kindness'), ('Женское дело', 'Women'), ('Повышение', 'Promotion'), ('Просто так', 'Just Like That'), ('Рождение ребенка', 'Baby Shower'), ('Хорошая привычка', 'Good Habit')], default='Просто так', max_length=100, verbose_name='Повод')),
                ('problem', models.CharField(choices=[('Алкоголизм и наркомания', 'Addiction'), ('Бедность', 'Poverty'), ('Бездомность', 'Homelessness'), ('Гендерное неравенство', 'Gender Inequality'), ('Инвалидность', 'Disability'), ('Права человека', 'Human Rights'), ('Психическое здоровье', 'Mental Health'), ('Искусство и культура', 'Culture And Art'), ('Сиротство', 'Orphanhood'), ('Бездомные животные', 'Homeless Animals')], max_length=100, verbose_name='Проблема')),
                ('fund', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='collects', to='funds.fund', verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Сбор',
                'verbose_name_plural': 'Сборы',
                'ordering': ('-created_at',),
            },
        ),
    ]
