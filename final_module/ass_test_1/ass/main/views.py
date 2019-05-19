from django.shortcuts import render
from django.contrib.auth import authenticate, login
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

# dictionary for getting the correctly spelled words
relations_dict = {'departments': 'Department',
                  'curriculums': 'Curriculum',
                  'instructors': 'Instructor',
                  'courses': 'Course',
                  'courseOfferings': 'Courseoffering',
                  'students': 'Student',
                  'semesters': 'Semester',
                  }

# tells us what is the head of the table corresponding to the given relation
table_head_dict = {'Department': ['Code', 'Name'],
                   'Curriculum': ['Version', 'Department code'],
                   'Instructor': ['Name','Surname', 'Department code'],
                   'Course': ['Code', 'Name', 'Credit'],
                   'Courseoffering': ['Course code', 'Semester'],
                   'Student': ['id', 'Name', 'Surname', 'Department code'],
                   'Semester': ['Type', 'Year'],
                   }




# returns a list of lists
#def get_table_elements(relation_name):
    #if relation_name == 'Department':



# list of tuples that makes up the table body

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

        context['table_head'] = table_head





    return render(request, 'main/admin_homepage.html', context)

@login_required(login_url="/signin/")
@user_passes_test(is_client)
def client_home_page_view(request):
    return render(request, 'main/client_homepage.html')



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



