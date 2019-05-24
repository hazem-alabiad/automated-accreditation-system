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


# dictionary for getting the correctly spelled words
relations_dict = {'departments': 'Department',
                  'curriculums': 'Curriculum',
                  'instructors': 'Instructor',
                  'courses': 'Course',
                  'courseOfferings': 'Courseoffering',
                  'students': 'Student',
                  'semesters': 'Semester',
                  'assessments': 'Assessment',
                  'questions': 'Question',
                  'question_courseLearningObjectives': 'QuestionCourselearningobjective',
                  'question_keyLearningOutcomes': 'QuestionKeylearningoutcome',
                  }

# tells us what is the head of the table corresponding to the given relation
table_head_dict = {'Department': ['Code', 'Name'],
                   'Curriculum': ['ID', 'Version', 'Department code'],
                   'Instructor': ['ID', 'Name', 'Surname', 'Department code'],
                   'Course': ['Code', 'Name', 'Credit'],
                   'Courseoffering': ['ID', 'Course code', 'Semester'],
                   'Student': ['ID', 'Name', 'Surname', 'Department code'],
                   'Semester': ['ID', 'Type', 'Year'],
                   'Assessment': ['ID', 'Course Code', 'Semester'],
                   'Question': ['ID', 'Assessment ID', 'Course Code', 'Semester'],
                   'QuestionCourselearningobjective': ['Question ID', 'Course learning objective ID'],
                   'QuestionKeylearningoutcome': ['Question ID', 'Key learning outcome ID'],
                   'Keylearningoutcome': ['body', 'dept_code'],
                   'Courselearningobjective': ['course_code', 'body'],
                   'Section': ['courseoffering', 'number'],
                   }

# key : an entity, value: all other entities that have a relationship with it
related_entities = {
    'Department': ['Curriculum', 'Instructor', 'Student', 'Keylearningoutcome'],
    'Curriculum': ['Course'],
    'Instructor': ['Section'],
    'Course': ['Courselearningobjective'],
    'Courseoffering': ['Section', 'Assessment'],
    'Student': ['Assessment', 'Section'],
    'Semester': ['Courseoffering'],
}

# returns the object that belongs to the relation specified, with the id given
def get_relation_object(relation_name, object_id):
    if relation_name == 'departments' or relation_name == 'courses':
        return eval(relations_dict[relation_name]).objects.get(code=object_id)
    else:
        return eval(relations_dict[relation_name]).objects.get(id=object_id)


def get_object_details(relation_name, object):
    if relation_name == 'departments':
        return [object.code, object.name]
    elif relation_name == 'curriculums':
        return [object.id, object.version, object.dept_code]
    elif relation_name == 'instructors':
        return [object.id, object.name, object.surname, object.dept_code]
    elif relation_name == 'courses':
        return [object.code, object.name, object.credit]
    elif relation_name == 'courseOfferings':
        return [object.id, object.course_code, object.semester]
    elif relation_name == 'students':
        return [object.id, object.name, object.surname, object.dep_code]
    elif relation_name == 'semesters':
        return [object.id, object.type, object.year]


# returns (realtion_name, [columns])
def get_related_relations_columns(relation_name):
    related_relations_columns = []

    related_ent = related_entities[relations_dict[relation_name]]

    for r in related_ent:
        related_relations_columns.append( (r, table_head_dict[r]) )

    return related_relations_columns




# works for the add, update cases
# if the object_id has a valid value, then the operation is an update
# the form corresponding to the relation name is initialized and added to the context
def add_proper_form_to_context(relation_name, object_id, context):
    if relation_name != " ":
        if relation_name == 'departments':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = departmentForm(instance=instance)
                context['form'] = form
            else:
                form = departmentForm(None)
                context['form'] = form

        elif relation_name == 'curriculums':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = curriculumForm(instance=instance)
                context['form'] = form
            else:
                form = curriculumForm(None)
                context['form'] = form

        elif relation_name == 'instructors':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = instructorForm(instance=instance)
                context['form'] = form
            else:
                form = instructorForm(None)
                context['form'] = form

        elif relation_name == 'courses':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = courseForm(instance=instance)
                context['form'] = form
            else:
                form = courseForm(None)
                context['form'] = form

        elif relation_name == 'courseOfferings':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = courseofferingForm(instance=instance)
                context['form'] = form
            else:
                form = courseofferingForm(None)
                context['form'] = form

        elif relation_name == 'students':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = studentForm(instance=instance)
                context['form'] = form
            else:
                form = studentForm(None)
                context['form'] = form

        elif relation_name == 'semesters':
            if object_id:
                instance = get_relation_object(relation_name, object_id)
                form = semesterForm(instance=instance)
                context['form'] = form
            else:
                form = semesterForm(None)
                context['form'] = form

#test functions
def is_admin(user):
    return user.groups.filter(name='system_admin').exists()

def is_client(user):
    return user.groups.filter(name='instructor').exists()

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
    relation_name = request.GET.get('relation', " ")
    if relation_name != " ":
        model_name = relations_dict[relation_name]
        # the eval(model_name) turns a given string into a python class
        all_objects = eval(model_name).objects.all()
        table_head = table_head_dict[model_name]

        context['relation_name'] = relation_name
        context['table_head'] = table_head
        context['rows'] = all_objects

    return render(request, 'main/admin_homepage.html', context)


@login_required(login_url="/signin/")
@user_passes_test(is_client)
def client_home_page_view(request):
    context = {}
    user_id = request.user.id

    all_objects = Courseoffering.objects.all()
    context['rows'] = all_objects

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

        if relation_name_to_submit == 'departments':
            form = departmentForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'curriculums':
            form = curriculumForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'instructors':
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

        elif relation_name_to_submit == 'courses':
            form = courseForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'courseOfferings':
            form = courseofferingForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'students':
            form = studentForm(request.POST)
            if form.is_valid():
                form.save()

        elif relation_name_to_submit == 'semesters':
            form = semesterForm(request.POST)
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
# if the model is the instructor, delete the corresponding user object
    #if relation_name == 'instructors':
        #auth_user = User.objects.filter(model_object.id)


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

        if relation_name_to_submit == "semesters":
            update_form = semesterForm(request.POST)
            if update_form.is_valid():
                model_object.type = update_form.cleaned_data['type']
                model_object.year = update_form.cleaned_data['year']
                model_object.save()

        elif relation_name_to_submit == "curriculums":
            update_form = curriculumForm(request.POST)
            if update_form.is_valid():
                model_object.version = update_form.cleaned_data['version']
                model_object.dept_code = update_form.cleaned_data['dept_code']
                model_object.save()

        elif relation_name_to_submit == "instructors":
            update_form = instructorForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.surname = update_form.cleaned_data['surname']
                model_object.dept_code = update_form.cleaned_data['dept_code']
                model_object.save()

        elif relation_name_to_submit == "courseOfferings":
            update_form = courseofferingForm(request.POST)
            if update_form.is_valid():
                model_object.semester = update_form.cleaned_data['semester']
                model_object.course_code = update_form.cleaned_data['course_code']
                model_object.letter_grades = update_form.cleaned_data['letter_grades']
                model_object.save()

        elif relation_name_to_submit == "courses":
            update_form = courseUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.credit = update_form.cleaned_data['credit']
                model_object.save()

        elif relation_name_to_submit == "departments":
            update_form = departmentUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.save()

        elif relation_name_to_submit == "students":
            update_form = studentUpdateForm(request.POST)
            if update_form.is_valid():
                model_object.name = update_form.cleaned_data['name']
                model_object.surname = update_form.cleaned_data['surname']
                model_object.dep_code = update_form.cleaned_data['dep_code']
                model_object.save()







        if submitting_user_type == 'admin':
            return redirect(reverse('adminHomePage'))
        elif submitting_user_type == 'client':
            return redirect(reverse('clientHomePage'))





    '''if relation_name_to_submit == 'departments':
            dep_code = model_object.code
            new_name =
            ret = cursor.callproc('usp_update_department', )'''


def entity_detail_view(request):
    context = {}
    if request.method == 'GET':
        relation_name = request.GET.get('relation_name', " ")
        object_id = request.GET.get('object_id', 0)
        user_type = request.GET.get('user', " ")
        relation_columns = table_head_dict[relations_dict[relation_name]]

        context['relation_name'] = relation_name
        context['object_id'] = object_id
        context['user_type'] = user_type
        context['relation_columns'] = relation_columns
        context['object_info'] = get_object_details(relation_name, get_relation_object(relation_name, object_id))

        context['related_entities'] = related_entities[relations_dict[relation_name]]

        context['related_entities_cloumns'] = get_related_relations_columns(relation_name)


        '''chosen_related_entity = request.GET.get('related_entity', " ")
        if chosen_related_entity != " ":
            print("chosen_related_entity", chosen_related_entity)
            context['chosen_related_entity'] = chosen_related_entity
            context['chosen_related_entity_columns'] = table_head_dict[chosen_related_entity]'''



    return render(request, 'main/objectDetailsView.html', context)