from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
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
                   }



#test functions
def is_admin(user):
    return user.groups.filter(name='system_admin').exists()

def is_client(user):
    return user.groups.filter(name='instructor').exists()

# returns the object that belongs to the relation specified, with the id given
def get_relation_object(relation_name, object_id):
    if relation_name == 'departments' or relation_name == 'courses':
        return eval(relations_dict[relation_name]).objects.get(code=object_id)
    else:
        return eval(relations_dict[relation_name]).objects.get(id=object_id)


# we are using the user's email as the user's name
def sign_in_view(request):
    if request.method == 'POST':
        user_email = request.POST.get('logInEmail')
        user_password = request.POST.get('logInPass')
        logged_in_user = authenticate(username=user_email, password=user_password)
        print(user_email, user_password)
        if logged_in_user is not None:
            login(request, logged_in_user)
            print('Logged in ', user_email)
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


#@login_required(login_url="/signin/")
#@user_passes_test(is_client)
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
    context['user_type'] = user_type
    context['relation_name_to_submit'] = relation_name
    # if GET request
    if relation_name != " ":
        if relation_name == 'departments':
            form = departmentForm(None)
            context['form'] = form

        elif relation_name == 'curriculums':
            form = curriculumForm(None)
            context['form'] = form

        elif relation_name == 'instructors':
            form = instructorForm(None)
            context['form'] = form

        elif relation_name == 'courses':
            form = courseForm(None)
            context['form'] = form

        elif relation_name == 'courseOfferings':
            form = courseofferingForm(None)
            context['form'] = form

        elif relation_name == 'students':
            form = studentForm(None)
            context['form'] = form

        elif relation_name == 'semesters':
            form = semesterForm(None)
            context['form'] = form


    # if POST request
    elif relation_name == " ":
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
                # adding the admin to the admin group
                user.groups.add(Group.objects.get(id=1))
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


    return render(request, 'main/addEntity.html', context)

def delete_entities_view(request):
    relation_name = request.GET.get('relation', " ")
    user = request.GET.get('user', ' ')
    object_id = request.GET.get('id', 0)

    object = get_relation_object(relation_name, object_id)
    object.delete()
    print(relation_name, object_id)

    if user == 'admin':
        return redirect(reverse('adminHomePage'))
    elif user == 'client':
        return redirect(reverse('clientHomePage'))





def entity_detail_view(request):
    relation_name = request.GET.get('relation_name', " ")
    object_id = request.GET.get('object_id', 0)
    context = {}

    return render(request, 'main/add_entity.html', context)