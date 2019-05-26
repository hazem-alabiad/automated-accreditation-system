from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.db import connection

#importing models
from django.contrib.auth.models import User, Group

from main.models import *
#importing forms
from main.forms import *

#decorators
from django.contrib.auth.decorators import login_required, user_passes_test


# tells us what is the head of the table corresponding to the given relation
table_head_dict = {'Department': ['Code', 'Name'],
                   'Curriculum': ['Curriculum ID', 'Version', 'Department code'],
                   'Instructor': ['Instructor ID', 'Name', 'Surname', 'Department code'],
                   'Course': ['Course Code', 'Name', 'Credit'],
                   'Courseoffering': ['Courseoffering ID', 'Course code'],
                   'Student': ['Student ID', 'Name', 'Surname', 'Department code'],
                   'Semester': ['Semester ID', 'Type', 'Year'],
                   'Assessment': ['Assessment ID', 'Course Code', 'Semester', 'Type'],
                   'Question': ['Question ID', 'Weight', 'Assessment ID'],
                   'QuestionCourselearningobjective': ['Objective', 'Measurement'],
                   'QuestionKeylearningoutcome': ['Outcome', 'Measurement'],
                   'Keylearningoutcome': ['Keylearningoutcome ID', 'body',],
                   'Courselearningobjective': ['Courselearningobjective ID', 'body'],
                   'Section': ['Section ID', 'Info'],
                   'Examination': ['Examination ID', 'Courseoffering', 'Weight', 'Room', 'Date', 'Duration', 'Type'],
                   'Quiz': ['Quiz ID', 'Courseoffering', 'Weight','Duration', 'Date'],
                   'Assignment': ['Assignment ID', 'Courseoffering', 'Weight', 'Start date', 'Due date'],
                   }

# key : an entity, value: all other entities that have a relationship with it
related_entities = {
    'Department': ['Curriculum', 'Instructor', 'Student', 'Keylearningoutcome'],
    'Curriculum': ['Course'],
    'Instructor': ['Section'],
    'Course': ['Courselearningobjective'],
    'Courseoffering': ['Section', 'Examination', 'Quiz', 'Assignment'],
    'Student': ['Section', 'Examination', 'Quiz', 'Assignment'],
    'Semester': ['Courseoffering'],
    'Section': ['Student', 'Instructor'],

    'Examination': ['Question'],
    'Quiz': ['Question'],
    'Assignment': ['Question'],
    'Question': ['QuestionCourselearningobjective', 'QuestionKeylearningoutcome'],

    'client-Section': ['Student', 'Examination', 'Quiz', 'Assignment'],

}

urls = {
    'client': ('clientHomePage', 'clientEntityDetailsPage', 'clientAddEntityPage', 'clientDeleteEntityPage', 'clientUpdateEntityPage'),
    'admin': ('adminHomePage', 'adminEntityDetailsPage', 'adminAddEntityPage', 'adminDeleteEntityPage', 'adminUpdateEntityPage'),
}

# returns the object that belongs to the relation specified, with the id given
def get_relation_object(relation_name, object_id):
    if relation_name == 'Department' or relation_name == 'Course':
        return eval(relation_name).objects.get(code=object_id)
    else:
        return eval(relation_name).objects.get(id=object_id)

# the object_2 is for the (Examination, Quiz, Assignment) cases in which we pass the assessment object as well (object_2)
def get_object_details(relation_name, object, object_2):
    if relation_name == 'Department':
        return [object.code, object.name]
    elif relation_name == 'Curriculum':
        return [object.id, object.version, object.dept_code]
    elif relation_name == 'Instructor':
        return [object.id, object.name, object.surname, object.dept_code]
    elif relation_name == 'Course':
        return [object.code, object.name, object.credit]
    elif relation_name == 'Courseoffering':
        return [object.id, object.course_code]
    elif relation_name == 'Student':
        return [object.id, object.name, object.surname, object.dep_code]
    elif relation_name == 'Semester':
        return [object.id, object.type, object.year]
    elif relation_name == 'Section':
        return [object.id, object.courseoffering]
    elif relation_name == 'Examination':
        return [object.id, object_2.courseoffering, object_2.weight, object.room, object.m_date, object.duration, object.type]
    elif relation_name == 'Quiz':
        return [object.id, object_2.courseoffering, object_2.weight, object.duration, object.q_date]
    elif relation_name == 'Assignment':
        return [object.id, object_2.courseoffering, object_2.weight, object.start_date, object.due_date]
    elif relation_name == 'Question':
        return [object.id, object.weight, object.assessment_id]

def get_corresponding_related_relation_objects(relation_name ,related_relation_name, object_id):
    with connection.cursor() as cursor:

        related_relation = related_relation_name.lower()
        sql_query = ""

        if relation_name == 'Department':
            sql_query = "SELECT * FROM "+related_relation+" WHERE dept_code=%s;"
            if related_relation == 'student':
                sql_query = "SELECT * FROM "+related_relation+" WHERE dep_code=%s;"
        ############################################################################################

        elif relation_name == 'Curriculum':
            sql_query = 'SELECT c.* FROM course c,curriculum_course cc where cc.curriculum_id=%s and cc.course_code=c.code;'
        ############################################################################################

        elif relation_name == 'Instructor':
            sql_query = "SELECT s.id, co.course_code, s.number FROM section s, section_instructor s_i, courseOffering co " \
                        "WHERE s_i.instructor_id=%s and s.id=s_i.section_id and s.courseoffering_id=co.id;"
        ############################################################################################
        elif relation_name == 'Course':
            sql_query = "SELECT * FROM courselearningobjective  WHERE course_code=%s;"
        ############################################################################################
        elif relation_name == 'Courseoffering':
            if related_relation == 'section':
                sql_query = "SELECT s.* FROM courseoffering co, section s WHERE co.id=%s and s.courseoffering_id=co.id;"

            elif related_relation == 'quiz':
                sql_query = "SELECT a.id, co.course_code, a.weight,q.duration, q.q_date FROM courseoffering co, assessment a, " \
                            "quiz q WHERE co.id=a.courseoffering_id AND a.id=q.id AND co.id=%s;"

            elif related_relation == 'examination':
                sql_query = "SELECT a.id, co.course_code, a.weight, e.room, e.m_date, e.duration, e.type FROM courseoffering co, assessment a, " \
                            "examination e WHERE co.id=a.courseoffering_id AND a.id=e.id AND co.id=%s;"

            elif related_relation == 'assignment':
                sql_query = "SELECT a.id, co.course_code, a.weight, assig.start_date, assig.due_date FROM courseoffering co, assessment a, " \
                            "assignment assig WHERE co.id=a.courseoffering_id AND a.id=assig.id AND co.id=%s;"
        ############################################################################################
        elif relation_name == 'Student':
            if related_relation == 'section':
                sql_query = "SELECT se.id, co.course_code, se.number FROM student st, section_student s_s, section se, courseOffering co " \
                            "WHERE st.id=s_s.student_id AND s_s.section_id=se.id AND se.courseoffering_id=co.id and st.id=%s; "

            elif related_relation == 'quiz':
                sql_query = 'SELECT a.id, co.course_code, a.weight,q.duration, q.q_date FROM assessment_student as_st, student s, assessment a,' \
                                'quiz q, courseOffering co ' \
                            'WHERE s.id=as_st.student_id AND as_st.assessment_id=a.id AND a.id=q.id AND a.courseoffering_id=co.id and s.id=%s;'

            elif related_relation == 'examination':
                sql_query = 'SELECT a.id, co.course_code, a.weight, e.room, e.m_date, e.duration, e.type ' \
                            'FROM assessment_student as_st, student s, assessment a,' \
                            'examination e, courseOffering co ' \
                            'WHERE s.id=as_st.student_id AND as_st.assessment_id=a.id AND a.id=e.id AND a.courseoffering_id=co.id and s.id=%s;'

            elif related_relation == 'assignment':
                sql_query = 'SELECT a.id, co.course_code, a.weight, assig.start_date, assig.due_date FROM assessment_student as_st, student s, assessment a,' \
                            'assignment assig, courseOffering co ' \
                            'WHERE s.id=as_st.student_id AND as_st.assessment_id=a.id AND a.id=assig.id AND a.courseoffering_id=co.id and s.id=%s;'
        ############################################################################################
        elif relation_name == 'Semester':
            sql_query = "SELECT e.* FROM courseoffering co, "+related_relation+" e WHERE co.id=%s;"
        ############################################################################################
        elif relation_name == 'Section':
            if related_relation == 'student':
                sql_query ='SELECT st.id, st.name, st.surname, st.dep_code FROM student st, section_student s_s, section se ' \
                           'WHERE st.id=s_s.student_id AND s_s.section_id=se.id and se.id=%s;'

            elif related_relation == 'instructor':
                sql_query = 'SELECT i.id, i.name, i.surname, i.dept_code FROM section s, section_instructor s_i, instructor i ' \
                            'WHERE s.id=s_i.section_id AND s_i.instructor_id=i.id and s.id=%s;'

            elif related_relation == 'quiz':
                sql_query = "SELECT a.id, co.course_code, a.weight,q.duration, q.q_date " \
                            "FROM courseoffering co, assessment a,quiz q , section s " \
                            "WHERE co.id=a.courseoffering_id AND a.id=q.id AND co.id=s.courseoffering_id AND s.id=%s;"

            elif related_relation == 'examination':
                sql_query = 'SELECT a.id, co.course_code, a.weight, e.room, e.m_date, e.duration, e.type ' \
                            'FROM courseoffering co, assessment a, section s,examination e  '  \
                            'WHERE co.id=a.courseoffering_id AND a.id=e.id AND co.id=s.courseoffering_id AND s.id=%s;'

            elif related_relation == 'assignment':
                sql_query = 'SELECT a.id, co.course_code, a.weight, assig.start_date, assig.due_date ' \
                            'FROM courseoffering co, assessment a, assignment assig, section s ' \
                            'WHERE co.id=a.courseoffering_id AND a.id=assig.id AND co.id=s.courseoffering_id AND s.id=%s;'

        ############################################################################################
        elif relation_name in ['Examination', 'Quiz', 'Assignment']:
            sql_query = 'SELECT q.id, asses.id  FROM '+relation_name.lower()+' e, assessment asses, question q ' \
                        'WHERE asses.id=e.id AND asses.id=q.assessment_id and e.id=%s ;'
        ############################################################################################
        elif relation_name == 'Question':
            if related_relation == 'questioncourselearningobjective':
                sql_query ='SELECT clo.id,clo.body FROM question q, question_courselearningobjective q_c, courselearningobjective clo  ' \
                           'WHERE q.id=q_c.question_id AND q_c.courselearningobjective_id=clo.id;'

            elif related_relation == 'questionkeylearningoutcome':
                sql_query = 'SELECT klo.id,klo.body FROM question q, question_keylearningoutcome q_k, keylearningoutcome klo' \
                            ' WHERE q.id=q_k.question_id AND q_k.key_learning_outcome_id=klo.id;'


        cursor.execute(sql_query, [object_id])
        #rows is a list of QuerySet
        rows = cursor.fetchall()
        return rows

# returns (realtion_name, [columns])
def get_related_relations(relation_name, object_id):
    related_relations = []

    related_ent = related_entities[relation_name]
    if relation_name == 'client-Section':
        relation_name = 'Section'

    for r in related_ent:
        related_relations.append((r, table_head_dict[r],
                                    get_corresponding_related_relation_objects(relation_name, r, object_id)))

    return related_relations


# works for the add, update cases
# if the object_id has a valid value, then the operation is an update
# the form corresponding to the relation name is initialized and added to the context
def add_proper_form_to_context(relation_name, object_id, context):
    if relation_name != " ":
        if relation_name == 'Department':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = departmentForm(instance=instance)
                context['form'] = form
            else:
                form = departmentForm(None)
                context['form'] = form

        elif relation_name == 'Curriculum':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = curriculumForm(instance=instance)
                context['form'] = form
            else:
                form = curriculumForm(None)
                context['form'] = form

        elif relation_name == 'Instructor':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = instructorForm(instance=instance)
                context['form'] = form
            else:
                form = instructorForm(None)
                context['form'] = form

        elif relation_name == 'Course':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = courseForm(instance=instance)
                context['form'] = form
            else:
                form = courseForm(None)
                context['form'] = form

        elif relation_name == 'Courseoffering':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = courseofferingForm(instance=instance)
                context['form'] = form
            else:
                form = courseofferingForm(None)
                context['form'] = form

        elif relation_name == 'Student':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = studentForm(instance=instance)
                context['form'] = form
            else:
                form = studentForm(None)
                context['form'] = form

        elif relation_name == 'Keylearningoutcome':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = KeylearningoutcomeForm(instance=instance)
                context['form'] = form
            else:
                form = KeylearningoutcomeForm(None)
                context['form'] = form

        elif relation_name == 'Courselearningobjective':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = CourselearningobjectiveForm(instance=instance)
                context['form'] = form
            else:
                form = CourselearningobjectiveForm(None)
                context['form'] = form

        elif relation_name == 'Section':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                #instance = get_relation_object('Instructor', object_id)

                form = SectionForm(instance=instance)
                #form2 =SectionInstructorForm(instance=instance2)
                context['form'] = form
            else:
                form = SectionForm(None)
                form2 =SectionInstructorForm()
                context['form'] = form
                context['form2'] = form2

        elif relation_name in ['Quiz', 'Assignment', 'Examination']:
            if object_id:

                instance = get_relation_object('Assessment', object_id)
                instance2 = get_relation_object(relation_name, object_id)

                form = AssessmentForm(instance)
                form2 = eval(relation_name+"Form")(instance2)

                context['form'] = form
                context['form2'] = form2
            else:
                form = AssessmentForm(None)
                form2 = eval(relation_name+"Form")(None)

                context['form'] = form
                context['form2'] = form2

        elif relation_name == 'Semester':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = semesterForm(instance=instance)
                context['form'] = form
            else:
                form = semesterForm(None)
                context['form'] = form

        elif relation_name == 'Question':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = QuestionForm(instance=instance)
                context['form'] = form
            else:
                form = QuestionForm(None)
                context['form'] = form

#test functions
def is_admin(user):
    return user.groups.filter(name='system_admin').exists()

def is_client(user):
    return user.groups.filter(name='instructor').exists()

def start_view(request):
    user = request.user
    if not request.user.is_anonymous:
        if is_admin(user):
            return redirect(reverse('adminHomePage'))
        elif is_client(user):
            return redirect(reverse('clientHomePage'))
    else:
        return redirect(reverse('signin'))


# we are using the user's email as the user's name
def sign_in_view(request):
    if request.method == 'POST':
        login_id = request.POST.get('logInID')
        user_password = request.POST.get('logInPass')
        logged_in_user = authenticate(username=login_id, password=user_password)
        print(login_id, user_password)
        if logged_in_user is not None:
            login(request, logged_in_user)
            print('Logged in ', login_id)
            # if the logged in is an admin
            if is_admin(logged_in_user):
                return redirect(reverse('adminHomePage'))
            # else if a user (instructor)
            else:
                return redirect(reverse('clientHomePage'))
        else:
            print('Tokens not correct')

    return render(request, 'main/sign_in.html')

@login_required(login_url="/signin/")
def signout_view(request):
    logout(request)
    return redirect(reverse('signin'))

@login_required(login_url="/signin/")
@user_passes_test(is_admin)
def admin_home_page_view(request):
    context = {}

    # check if any relation is requested
    relation_name = request.GET.get('relation_name', " ")
    if relation_name != " ":
        # the eval(model_name) turns a given string into a python class
        all_objects = eval(relation_name).objects.all()
        table_head = table_head_dict[relation_name]

        context['relation_name'] = relation_name
        context['table_head'] = table_head
        context['rows'] = all_objects

    return render(request, 'main/admin_homepage.html', context)


@login_required(login_url="/signin/")
@user_passes_test(is_client)
def client_home_page_view(request):
    context = {}
    instructor_user_id = request.user.id

    instructor_object = Instructor.objects.get(id=int(request.user.username))

    section_objects = SectionInstructor.objects.filter(instructor=instructor_object)


    context['rows'] = section_objects

    return render(request, 'main/client_homepage.html', context)


#super super user
def create_admin_view(request):
    form = create_admin_form(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            admin_user_name = form.cleaned_data.get('username')
            admin_password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=admin_user_name,
                                    email=admin_user_name+'@hacettepe.edu.tr',
                                    password=admin_password)
            # adding the admin to the admin group
            user.groups.add(Group.objects.get(id=1))
            user.save()
            print('admin created!', admin_user_name)
        else:
            print("something wrong with the form")

    return render(request, 'main/create_admin.html', {'form': form})

# used for both adding entities and updating them
def add_entities_view(request):
    context = {}
    relation_name = request.GET.get('relation_name', " ")
    user_type = request.GET.get('user_type', " ")

    # if GET request
    if request.method == 'GET':
        context['user_type'] = user_type
        context['relation_name'] = relation_name

        add_proper_form_to_context(relation_name, None, context)
        return render(request, 'main/addEntity.html', context)

    # if POST request, take the POST request and save it to the DB
    elif request.method == 'POST':
        relation_name_to_submit = request.POST.get('relation_name_to_submit', " ")
        submitting_user_type = request.POST.get('submitting_user_type', " ")

        if relation_name_to_submit == 'Department':
            form = departmentForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Curriculum':
            form = curriculumForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Instructor':
            form = instructorForm(request.POST)
            if form.is_valid():
                instructor = form.save()
                instructor_first_name = form.cleaned_data['name']
                instructor_last_name = form.cleaned_data['surname']
                # add the instructor as a client user
                user = User.objects.create_user(username=instructor.id,
                                                email=instructor_first_name+'@hacettepe.edu.tr',
                                                password="123",
                                                first_name=instructor_first_name,
                                                last_name=instructor_last_name)
                # adding the instructor to the instructor group
                user.groups.add(Group.objects.get(id=2))
                user.save()

        elif relation_name_to_submit == 'Course':
            form = courseForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Courseoffering':
            form = courseofferingForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Student':
            form = studentForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Courselearningobjective':
            form = CourselearningobjectiveForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Section':
            form = SectionForm(request.POST)
            form2 = SectionInstructorForm(request.POST)
            if form.is_valid():
                if form2.is_valid():
                    ins = form2.cleaned_data['instructor']
                    sec = form.save()
                    SectionInstructor.objects.create(instructor=ins, section=sec)

        elif relation_name_to_submit == 'Semester':
            form = semesterForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'Keylearningoutcome':
            form = KeylearningoutcomeForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit in ['Quiz', 'Assignment', 'Examination']:
            form = eval('AssessmentForm')(request.POST)
            form2 = eval(relation_name_to_submit+'Form')(request.POST)
            print(relation_name_to_submit)

            if form.is_valid():
                assessment = form.save()
                if form2.is_valid():
                    # save the object manually
                    if relation_name_to_submit == 'Quiz':
                        q = Quiz(id=assessment.id,
                                 duration=form2.cleaned_data['duration'],
                                 q_date=form2.cleaned_data['q_date']
                                )
                        q.save()

                    elif relation_name_to_submit == 'Assignment':
                        print('IN ASSIGNMENT', )
                        a = Assignment(id=assessment.id,
                                       start_date=form2.cleaned_data['start_date'],
                                       due_date=form2.cleaned_data['due_date']
                                       )
                        a.save()
                        print('IN ASSIGNMENT', a)

                    elif relation_name_to_submit == 'Examination':
                        e = Examination(id=assessment.id,
                                        room=form2.cleaned_data['room'],
                                        m_date=form2.cleaned_data['m_date'],
                                        duration=form2.cleaned_data['duration'],
                                        type=form2.cleaned_data['type'],
                                       )
                        e.save()

        elif relation_name_to_submit == 'Question':
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save()
                with connection.cursor() as cursor:
                    cursor.execute(sql_query, question.assessment.id)
                    clo_ids = cursor.fetchall()

                    cursor.execute(sql_query, question.assessment.id)
                    klo_ids = cursor.fetchall()




        elif relation_name_to_submit == 'Keylearningoutcome':
            form = KeylearningoutcomeForm(request.POST)
            if form.is_valid():
                form.save()


        if submitting_user_type == 'admin':
            return redirect(reverse('adminHomePage'))
        elif submitting_user_type == 'client':
            return redirect(reverse('clientHomePage'))

def delete_entities_view(request):
    relation_name = request.GET.get('relation_name', " ")
    user = request.GET.get('user', ' ')
    object_id = request.GET.get('object_id', 0)

    model_object = get_relation_object(relation_name, object_id)
    model_object.delete()


    if user == 'admin':
        return redirect(reverse('adminHomePage'))
    elif user == 'client':
        return redirect(reverse('clientHomePage'))

def update_entities_view(request):
    context = {}
    relation_name = request.GET.get('relation_name', " ")
    user_type = request.GET.get('user', " ")
    object_id = request.GET.get('object_id', 0)


    # if GET request
    if request.method == 'GET':
        context['user_type'] = user_type
        context['relation_name'] = relation_name
        context['object_id'] = object_id
        add_proper_form_to_context(relation_name, object_id, context)
        return render(request, 'main/addEntity.html', context)

    # if POST request, get the id of the object, update it using procedures
    elif request.method == 'POST':
        relation_name_to_submit = request.POST.get('relation_name_to_submit', " ")
        submitting_user_type = request.POST.get('submitting_user_type', " ")
        object_id = request.POST.get('object_id_name', " ")

        model_object = get_relation_object(relation_name_to_submit, object_id)

        if relation_name_to_submit == "Semester":
            update_form = semesterForm(request.POST)
            if update_form.is_valid():
                model_object.type = update_form.cleaned_data['type']
                model_object.year = update_form.cleaned_data['year']
                model_object.save()

        elif relation_name_to_submit == "Curriculum":
            update_form = curriculumForm(request.POST)
            if update_form.is_valid():
                model_object.version = update_form.cleaned_data['version']
                model_object.dept_code = update_form.cleaned_data['dept_code']
                model_object.save()

        elif relation_name_to_submit == "Instructor":
            update_form = instructorForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.surname = update_form.cleaned_data['surname']
                model_object.dept_code = update_form.cleaned_data['dept_code']
                model_object.save()

        elif relation_name_to_submit == "CourseOffering":
            update_form = courseofferingForm(request.POST)
            if update_form.is_valid():
                model_object.semester = update_form.cleaned_data['semester']
                model_object.course_code = update_form.cleaned_data['course_code']
                model_object.letter_grades = update_form.cleaned_data['letter_grades']
                model_object.save()

        elif relation_name_to_submit == "Course":
            update_form = courseUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.credit = update_form.cleaned_data['credit']
                model_object.save()

        elif relation_name_to_submit == "Department":
            update_form = departmentUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.save()

        elif relation_name_to_submit == "Student":
            update_form = studentUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.surname = update_form.cleaned_data['surname']
                model_object.dep_code = update_form.cleaned_data['dep_code']
                model_object.save()

        elif relation_name_to_submit == "Keylearningoutcome":
            update_form = KeylearningoutcomeForm(request.POST)
            if update_form.is_valid():
                model_object.dept_code = update_form.cleaned_data['dept_code']
                model_object.body = update_form.cleaned_data['body']
                model_object.save()


        if submitting_user_type == 'admin':
            return redirect(reverse('adminHomePage'))
        elif submitting_user_type == 'client':
            return redirect(reverse('clientHomePage'))

def entity_detail_view(request):
    context = {}
    if request.method == 'GET':
        relation_name = request.GET.get('relation_name', " ")
        object_id = request.GET.get('object_id', 0)
        user_type = request.GET.get('user', " ")
        relation_columns = table_head_dict[relation_name]

        # 0: homepage, 1: detail, 2: add, 3: delete, 4: update
        context['user_urls'] = urls[user_type]

        context['relation_name'] = relation_name
        context['object_id'] = object_id
        context['user_type'] = user_type
        context['relation_columns'] = relation_columns

        if relation_name == 'Question':
            question_obj = Question.objects.get(id=object_id)
            context['question_body'] = question_obj.body

        if relation_name in ['Quiz', 'Assignment', 'Examination']:
            assessment = Assessment.objects.get(id=object_id)
            context['object_info'] = get_object_details(relation_name, get_relation_object(relation_name, object_id), assessment)
        else:
            context['object_info'] = get_object_details(relation_name, get_relation_object(relation_name, object_id), None)


        # for the client view of the section we show him the Student, Quiz, Assignment, Examination
        if user_type == 'client' and relation_name == 'Section':
            context['related_entities_names'] = related_entities['client-Section']
            # list of tuples: [ (entity_name, entity_columns, corresponding_entity_rows), .... ]
            context['related_entities'] = get_related_relations('client-Section', object_id)

        # for the rest of the cases
        else:
            context['related_entities_names'] = related_entities[relation_name]
            # list of tuples: [ (entity_name, entity_columns, corresponding_entity_rows), .... ]
            context['related_entities'] = get_related_relations(relation_name, object_id)

        return render(request, 'main/objectDetailsView.html', context)

    elif request.method == 'POST' and request.POST.get('question_objective_outcome'):
        question_id = int(request.POST.get('question_id'))
        question_obj = Question.objects.get(id=question_id)

        related_entity_name = request.POST.get('related_entity_name')
        print(question_id)
        print(question_obj)
        print(related_entity_name)

        objects = QuestionCourselearningobjective.objects.filter(question_id=question_id)

        print(objects)



        #assessment_questions = Question.objects.filter(assessment=assessment_id)

        if request.POST.get('user_type') == 'admin':
            return redirect(reverse('adminHomePage'))

        elif request.POST.get('user_type') == 'client':
            return redirect(reverse('cleintHomePage'))



