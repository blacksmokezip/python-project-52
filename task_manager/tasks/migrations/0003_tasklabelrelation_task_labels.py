# Generated by Django 4.2.7 on 2023-11-02 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_rename_date_created_label_created_at'),
        ('tasks', '0002_alter_task_options_alter_task_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskLabelRelation',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('label', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    to='labels.label'
                )),
                ('task', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='tasks.task'
                )),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(
                blank=True,
                related_name='labels',
                through='tasks.TaskLabelRelation',
                to='labels.label',
                verbose_name='Метки'
            ),
        ),
    ]
