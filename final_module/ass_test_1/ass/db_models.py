from django.db import models


class Assessment(models.Model):
    courseoffering = models.ForeignKey('Courseoffering', models.DO_NOTHING)
    files = models.BinaryField(blank=True, null=True)
    weight = models.FloatField()

    class Meta:
        managed = True
        db_table = 'assessment'


class AssessmentStudent(models.Model):
    student = models.ForeignKey('Student', models.DO_NOTHING, primary_key=True)
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING)
    grade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'assessment_student'
        unique_together = (('student', 'assessment'),)


class Assignment(models.Model):
    id = models.IntegerField(primary_key=True)
    start_date = models.DateField()
    due_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'assignment'


class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=255)
    credit = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'course'


class Courselearningobjective(models.Model):
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')
    body = models.CharField(max_length=1000)

    class Meta:
        managed = True
        db_table = 'courselearningobjective'


class Courseoffering(models.Model):
    semester = models.ForeignKey('Semester', models.DO_NOTHING)
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')
    letter_grades = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'courseoffering'


class Curriculum(models.Model):
    version = models.IntegerField()
    dept_code = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept_code')

    class Meta:
        managed = True
        db_table = 'curriculum'


class CurriculumCourse(models.Model):
    curriculum = models.ForeignKey(Curriculum, models.DO_NOTHING, primary_key=True)
    course_code = models.ForeignKey(Course, models.DO_NOTHING, db_column='course_code')

    class Meta:
        managed = True
        db_table = 'curriculum_course'
        unique_together = (('curriculum', 'course_code'),)


class Department(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=25)

    class Meta:
        managed = True
        db_table = 'department'


class Examination(models.Model):
    id = models.IntegerField(primary_key=True)
    room = models.CharField(max_length=10)
    m_date = models.DateField()
    duration = models.SmallIntegerField()
    type = models.CharField(max_length=7)

    class Meta:
        managed = True
        db_table = 'examination'


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dept_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_code')

    class Meta:
        managed = True
        db_table = 'instructor'


class Keylearningoutcome(models.Model):
    body = models.CharField(max_length=1000)
    dept_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept_code')

    class Meta:
        managed = True
        db_table = 'keylearningoutcome'


class Question(models.Model):
    body = models.CharField(max_length=1000)
    weight = models.FloatField()
    assessment = models.ForeignKey(Assessment, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'question'


class QuestionCourselearningobjective(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING)
    courselearningobjective = models.ForeignKey(Courselearningobjective, models.DO_NOTHING, primary_key=True)
    value = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'question_courselearningobjective'
        unique_together = (('courselearningobjective', 'question'),)


class QuestionKeylearningoutcome(models.Model):
    question = models.ForeignKey(Question, models.DO_NOTHING, primary_key=True)
    key_learning_outcome = models.ForeignKey(Keylearningoutcome, models.DO_NOTHING)
    value = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'question_keylearningoutcome'
        unique_together = (('question', 'key_learning_outcome'),)


class Quiz(models.Model):
    id = models.IntegerField(primary_key=True)
    duration = models.SmallIntegerField()
    q_date = models.DateField()

    class Meta:
        managed = True
        db_table = 'quiz'


class Section(models.Model):
    courseoffering = models.ForeignKey(Courseoffering, models.DO_NOTHING)
    number = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'section'


class SectionInstructor(models.Model):
    section = models.ForeignKey(Section, models.DO_NOTHING, primary_key=True)
    instructor = models.ForeignKey(Instructor, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'section_instructor'
        unique_together = (('section', 'instructor'),)


class SectionStudent(models.Model):
    section = models.ForeignKey(Section, models.DO_NOTHING, primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'section_student'
        unique_together = (('section', 'student'),)


class Semester(models.Model):
    type = models.CharField(max_length=10)
    year = models.CharField(max_length=4)

    class Meta:
        managed = True
        db_table = 'semester'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    dep_code = models.ForeignKey(Department, models.DO_NOTHING, db_column='dep_code')

    class Meta:
        managed = True
        db_table = 'student'
