from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
#importing models
from django.contrib.auth.models import User, Group
from main.models import *
#importing forms
from main.forms import create_admin_form

#decorators
from django.contrib.auth.decorators import login_required, user_passes_test




#test functions
def is_admin(user):
    return user.groups.filter(name='system_admin').exists()

def is_client(user):
    return user.groups.filter(name='instructor').exists()


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
            print(Group.objects.get(id=1))
            user.groups.add(Group.objects.get(id=1))
            user.save()
            print('admin created!', admin_user_name)
        else:
            print("something wrong with the form")

    return render(request, 'main/create_admin.html', {'form': form})



def add_entities_view(request):
    context = {}

    return render(request, 'main/add_entity.html', context)


def entity_detail_view(request):
    relation_name = request.GET.get('relation_name', " ")
    object_id = request.GET.get('object_id', 0)
    context = {}
    print(object_id, relation_name)
    return render(request, 'main/add_entity.html', context)