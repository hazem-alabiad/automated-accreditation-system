# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Department(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'department'

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=30, blank=True, null=True)
    dep_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dep_code', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'student'


class Assessment(models.Model):
    courseoffering = models.ForeignKey('Courseoffering', models.DO_NOTHING, blank=True, null=True)
    files = models.BinaryField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment'


class AssessmentStudent(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING, primary_key=True)
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING)
    grade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment_student'
        unique_together = (('student', 'assessment'),)


class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignment'


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255, blank=True, null=True)
    credit = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class Courselearningobjective(models.Model):
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code', blank=True, null=True)
    body = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courselearningobjective'


class Courseoffering(models.Model):
    semester = models.ForeignKey('Semester', models.DO_NOTHING, blank=True, null=True)
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code', blank=True, null=True)
    letter_grades = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courseoffering'


class Curriculum(models.Model):
    version = models.IntegerField(blank=True, null=True)
    dept_code = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curriculum'


class CurriculumCourse(models.Model):
    curriculum = models.ForeignKey(Curriculum, models.DO_NOTHING, primary_key=True)
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')

    class Meta:
        managed = False
        db_table = 'curriculum_course'
        unique_together = (('curriculum', 'course_code'),)


class Examination(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.CharField(max_length=10, blank=True, null=True)
    m_date = models.DateField(blank=True, null=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    type = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'examination'

class Instructor(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    dept_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instructor'

class Keylearningoutcome(models.Model):
    body = models.CharField(max_length=1000, blank=True, null=True)
    dept_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keylearningoutcome'


class Question(models.Model):
    body = models.CharField(max_length=1000, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class QuestionCourselearningobjective(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    courselearningobjective = models.ForeignKey(Courselearningobjective, models.DO_NOTHING, primary_key=True)
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_courselearningobjective'
        unique_together = (('courselearningobjective', 'question'),)


class QuestionKeylearningoutcome(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING, primary_key=True)
    key_learning_outcome = models.ForeignKey(Keylearningoutcome, models.DO_NOTHING)
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_keylearningoutcome'
        unique_together = (('question', 'key_learning_outcome'),)


class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    duration = models.SmallIntegerField(blank=True, null=True)
    q_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz'


class Section(models.Model):
    courseoffering = models.ForeignKey(Courseoffering, models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'


class SectionInstructor(models.Model):
    section = models.ForeignKey(Section, models.DO_NOTHING, primary_key=True)
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'section_instructor'
        unique_together = (('section', 'instructor'),)


class SectionStudent(models.Model):
    section = models.ForeignKey(Section, models.DO_NOTHING, primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'section_student'
        unique_together = (('section', 'student'),)


class Semester(models.Model):
    type = models.CharField(max_length=10, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semester'


