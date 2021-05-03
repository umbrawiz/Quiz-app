# Generated by Django 3.2 on 2021-05-03 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Multiple Choice Question', 'verbose_name_plural': 'Multiple Choice Questions'},
        ),
        migrations.RemoveField(
            model_name='question',
            name='a1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='a2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='a3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='correctFeedback',
        ),
        migrations.RemoveField(
            model_name='question',
            name='incorrectFeedback',
        ),
        migrations.RemoveField(
            model_name='question',
            name='rightAnswer',
        ),
        migrations.AddField(
            model_name='question',
            name='answer_order',
            field=models.CharField(blank=True, choices=[('hold', 'hold'), ('random', 'Random')], help_text='The order in which multichoice                         answer options are displayed                         to the user', max_length=30, null=True, verbose_name='Answer Order'),
        ),
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(blank=True, max_length=2000),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(blank=True, to='quiz.Quiz'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(help_text='Enter the answer text that                                             you want displayed', max_length=1000, verbose_name='Content')),
                ('correct', models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.question', verbose_name='Question')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
    ]
