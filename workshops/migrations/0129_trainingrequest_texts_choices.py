# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-02-11 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0128_auto_20170710_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingrequest',
            name='gender',
            field=models.CharField(blank=True, choices=[('U', 'Prefer not to say'), ('F', 'Female'), ('M', 'Male'), ('O', 'Other (enter below)')], default='U', max_length=1),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='group_name',
            field=models.CharField(blank=True, default='', help_text='If you are applying at the same time as friends or colleagues, pick a name for your group (e.g., the name of your institution) and fill that in, and we will try to put you in the same training class.', max_length=100, verbose_name='Group name'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='location',
            field=models.CharField(help_text='Please give city, and province or state if applicable.', max_length=100, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='max_travelling_frequency',
            field=models.CharField(choices=[('not-at-all', 'Not at all'), ('yearly', 'Once a year'), ('often', 'Several times a year'), ('other', 'Other (enter below)')], default='not-at-all', help_text=None, max_length=40, verbose_name='How frequently would you be able to travel to teach such classes?'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='previous_experience',
            field=models.CharField(choices=[('none', 'None'), ('hours', 'A few hours'), ('workshop', 'A workshop (full day or longer)'), ('ta', 'Teaching assistant for a full course'), ('courses', 'Primary instructor for a full course'), ('other', 'Other (enter below)')], default='none', help_text='Please include teaching experience at any level from grade school to post-secondary education.', max_length=40, verbose_name='Previous experience in teaching'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='previous_experience_explanation',
            field=models.TextField(blank=True, null=True, verbose_name='Description of your previous experience in teaching'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='previous_involvement',
            field=models.ManyToManyField(blank=True, help_text='Please check all that apply.', to='workshops.Role', verbose_name='In which of the following ways have you been involved with The Carpentries'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='previous_training',
            field=models.CharField(choices=[('none', 'None'), ('hours', 'A few hours'), ('days', 'A few days'), ('workshop', 'A workshop'), ('course', 'A certification or short course'), ('full', 'A full degree'), ('other', 'Other (enter below)')], default='none', help_text=None, max_length=40, verbose_name='Previous formal training as a teacher or instructor'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='previous_training_explanation',
            field=models.TextField(blank=True, null=True, verbose_name='Description of your previous training in teaching'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='programming_language_usage_frequency',
            field=models.CharField(choices=[('daily', 'Every day'), ('weekly', 'A few times a week'), ('monthly', 'A few times a month'), ('yearly', 'A few times a year'), ('not-much', 'Never or almost never')], default='daily', max_length=40, verbose_name='How frequently do you work with the tools that The Carpentries teach, such as R, Python, MATLAB, Perl, SQL, Git, OpenRefine, and the Unix Shell?'),
        ),
        migrations.AlterField(
            model_name='trainingrequest',
            name='teaching_frequency_expectation',
            field=models.CharField(choices=[('not-at-all', 'Not at all'), ('yearly', 'Once a year'), ('monthly', 'Several times a year'), ('often', 'Primary occupation'), ('other', 'Other (enter below)')], default='not-at-all', help_text=None, max_length=40, verbose_name='How often would you expect to teach Carpentry Workshops after this training?'),
        ),
    ]
