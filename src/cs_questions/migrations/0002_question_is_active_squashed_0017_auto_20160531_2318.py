# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 02:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('cs_questions', '0002_question_is_active'), ('cs_questions', '0003_auto_20160508_2227'), ('cs_questions', '0004_auto_20160508_2233'), ('cs_questions', '0005_auto_20160511_1211'), ('cs_questions', '0006_auto_20160522_1146'), ('cs_questions', '0007_auto_20160522_1151'), ('cs_questions', '0008_auto_20160522_1209'), ('cs_questions', '0009_auto_20160522_1302'), ('cs_questions', '0010_auto_20160522_2041'), ('cs_questions', '0011_auto_20160522_2051'), ('cs_questions', '0012_remove_quizresponse_quiz'), ('cs_questions', '0013_auto_20160523_0945'), ('cs_questions', '0014_quizactivity_language'), ('cs_questions', '0015_auto_20160531_1923'), ('cs_questions', '0016_auto_20160531_1924'), ('cs_questions', '0017_auto_20160531_2318')]

    dependencies = [
        ('cs_activities', '0002_auto_20160504_1329_squashed_0017_auto_20160601_0908'),
        ('cs_core', '0001_initial'),
        ('cs_questions', '0001_squashed_0004_auto_20160501_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Marks a question as active/inactive. Inactive questions are notshown publicly and are only available to the question owner.', verbose_name='is active'),
        ),
        migrations.RenameField(
            model_name='codingioresponse',
            old_name='question_fallback',
            new_name='question',
        ),
        migrations.AddField(
            model_name='numericresponse',
            name='question_for_unbound',
            field=models.ForeignKey(blank=True, help_text='Question object reference for unbound responses. This should be null for activity responses.', null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_questions.Question'),
        ),
        migrations.RenameField(
            model_name='codingioresponse',
            old_name='question',
            new_name='question_for_unbound',
        ),
        migrations.AlterField(
            model_name='codingioresponse',
            name='question_for_unbound',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_questions.Question'),
        ),
        migrations.RenameField(
            model_name='questionactivity',
            old_name='question',
            new_name='question_base',
        ),
        migrations.AlterField(
            model_name='questionactivity',
            name='question_base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='cs_questions.Question'),
        ),
        migrations.AlterField(
            model_name='codingioresponse',
            name='question_for_unbound',
            field=models.ForeignKey(blank=True, help_text='Question object reference for unbound responses. This should be null for activity responses.', null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_questions.Question'),
        ),
        migrations.AlterModelOptions(
            name='questionactivity',
            options={'verbose_name': 'question activity', 'verbose_name_plural': 'question activities'},
        ),
        migrations.AddField(
            model_name='questionactivity',
            name='recycle_unbound',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='QuizActivity',
            fields=[
                ('activity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cs_activities.Activity')),
                #('grading_method', models.IntegerField(choices=[(0, 'largest grade of all responses'), (1, 'smallest grade of all responses'), (2, 'mean grade')])),
                ('quiz_grading_method', models.IntegerField(choices=[(0, 'largest grade of all responses'), (1, 'smallest grade of all responses'), (2, 'mean grade')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cs_activities.activity',),
        ),
        migrations.CreateModel(
            name='QuizActivityItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveIntegerField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cs_questions.Question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cs_questions.QuizActivity')),
            ],
        ),
        migrations.CreateModel(
            name='QuizResponse',
            fields=[
                ('response_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cs_activities.Response')),
            ],
            options={
                'abstract': False,
            },
            bases=('cs_activities.response',),
        ),
        migrations.AlterField(
            model_name='freeanswerquestion',
            name='data_type',
            field=models.CharField(choices=[('file', 'Arbitrary file'), ('image', 'Image file'), ('pdf', 'PDF file'), ('richtext', 'Rich text input'), ('richtext', 'Plain text input')], max_length=10),
        ),
        migrations.AlterUniqueTogether(
            name='quizactivityitem',
            unique_together=set([('quiz', 'index')]),
        ),
        migrations.AlterModelOptions(
            name='quizactivity',
            options={'verbose_name': 'quiz activity', 'verbose_name_plural': 'quiz activities'},
        ),
        migrations.CreateModel(
            name='FileFreeAnswerQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='cs_questions.Question')),
            ],
            options={
                'abstract': False,
            },
            bases=('cs_questions.question',),
        ),
        migrations.RenameField(
            model_name='booleanquestion',
            old_name='answer',
            new_name='answer_key',
        ),
        migrations.RenameField(
            model_name='stringmatchquestion',
            old_name='answer',
            new_name='answer_key',
        ),
        migrations.AddField(
            model_name='quizactivity',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cs_core.ProgrammingLanguage'),
        ),
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='question',
            name='long_description',
            field=models.TextField(blank=True, help_text='A detailed explanation.', verbose_name='long description'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='short_description',
            field=models.CharField(default='no-description', help_text='A very brief one-phrase description used in listings.', max_length=140, verbose_name='short description'),
        ),
        # migrations.RenameField(
        #     model_name='quizactivity',
        #     old_name='grading_method',
        #     new_name='quiz_grading_method',
        # ),
    ]
