# Generated by Django 2.2.7 on 2019-11-29 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constructorapi', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('body', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('block_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructorapi.AddedBlocks')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constructorapi.Statuses')),
            ],
        ),
    ]
