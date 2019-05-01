# Generated by Django 2.1.7 on 2019-05-01 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190501_1000'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Assessment',
        ),
        migrations.RemoveField(
            model_name='assessmentstudent',
            name='student',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='Courseoffering',
        ),
        migrations.RemoveField(
            model_name='curriculumcourse',
            name='curriculum',
        ),
        migrations.DeleteModel(
            name='Examination',
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
        migrations.DeleteModel(
            name='Keylearningoutcome',
        ),
        migrations.RemoveField(
            model_name='questioncourselearningobjective',
            name='courselearningobjective',
        ),
        migrations.RemoveField(
            model_name='questionkeylearningoutcome',
            name='question',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.RemoveField(
            model_name='sectioninstructor',
            name='section',
        ),
        migrations.RemoveField(
            model_name='sectionstudent',
            name='section',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
        migrations.DeleteModel(
            name='AssessmentStudent',
        ),
        migrations.DeleteModel(
            name='Courselearningobjective',
        ),
        migrations.DeleteModel(
            name='Curriculum',
        ),
        migrations.DeleteModel(
            name='CurriculumCourse',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionCourselearningobjective',
        ),
        migrations.DeleteModel(
            name='QuestionKeylearningoutcome',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='SectionInstructor',
        ),
        migrations.DeleteModel(
            name='SectionStudent',
        ),
    ]
