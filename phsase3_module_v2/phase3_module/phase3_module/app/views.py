from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from django.db import IntegrityError, DataError

from app.models import *

modified_table_names = {"key learning outcomes": "keylearningoutcome", "course learning objectives": "courselearningobjective"}
# returns three boolean values representing the is_insert, is_delete values.
# the is_update is the negation of is_insert
def get_insert_delete_values(relation_name, request):
    if relation_name in modified_table_names:
        relation_name = modified_table_names.get(relation_name)

    is_insert = request.POST.get("name_insert_or_update_"+relation_name) == "insert"
    is_delete = request.POST.get("name_"+relation_name+"_delete") != ""

    return is_insert, is_delete

def int_or_0(value):
    try:
        return int(value)
    except:
        return 0



def do_transaction_from_form_to_table(request):
    relation_name = request.POST.get("name_selection")
    is_insert, is_delete = get_insert_delete_values(relation_name, request)
    try:
        #################################### department ##############################
        if relation_name == "department":
            dep_code = request.POST.get('name_dep_code')
            dep_name = request.POST.get('name_dep_name')
            dep_name_delete = request.POST.get('name_department_delete')

            if is_delete:
                Department.objects.filter(code=dep_name_delete).delete()
                return

            if is_insert:
                Department.objects.create(code=dep_code, name=dep_name)
                return
            # the update command
            else:
                d = Department.objects.get(code=dep_code)
                d.name = dep_name
                d.save()

        #################################### student ##############################
        elif relation_name == "student":
            s_id = int_or_0(request.POST.get('name_s_id'))
            s_name = request.POST.get('name_s_name')
            s_surname = request.POST.get('name_s_surname')
            s_dep_code = request.POST.get('name_s_dep_code')
            s_id_delete = int_or_0(request.POST.get('name_student_delete'))

            if is_delete:
                Student.objects.filter(id=s_id_delete).delete()
                return

            if is_insert:
                Student.objects.create(id=s_id, name=s_name, surname=s_surname,
                                       dep_code=Department.objects.get(code=s_dep_code))
                return
            else:
                s = Studnet.objects.get(id=s_id)
                s.name = s_name
                s.surname = s_surname
                s.dep_code = s_dep_code
                s.save()

        #################################### instructor ##############################
        elif relation_name == "instructor":
            i_id = int_or_0(request.POST.get('name_i_id'))
            i_name = request.POST.get('name_i_name')
            i_surname = request.POST.get('name_i_surname')
            i_dep_code = request.POST.get('name_i_dept_code')
            i_id_delete = int_or_0(request.POST.get('name_instructor_delete'))


            if is_delete:
                Instructor.objects.filter(id=i_id_delete).delete()
                return

            if is_insert:
                Instructor.objects.create(id=i_id, name=i_name, surname=i_surname,
                                          dept_code=Department.objects.get(code=i_dep_code))
                return
            else:
                i = Instructor.objects.get(id=i_id)
                i.name = i_name
                i.surname = i_surname
                i.dep_code = i_dep_code
                i.save()

    except IntegrityError as e:
        print(str(e).split("\n")[0])
    except DataError as e:
        print(str(e).split("\n")[0])












def main_view(request):
    context = {}
    if request.method == 'POST':
        do_transaction_from_form_to_table(request)

    return render(request, 'app/module.html', context)
