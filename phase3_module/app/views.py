from django.shortcuts import render
from django.db import connection


modified_table_names = {"key learning outcomes": "keylearningoutcome", "course learning objectives": "courselearningobjective"}
# returns three boolean values representing the is_insert, is_delete values.
# the is_update is the negation of is_insert
def get_insert_delete_values(relation_name, request):
    if relation_name in modified_table_names:
        relation_name = modified_table_names.get(relation_name)

    is_insert = request.POST.get("name_insert_or_update_"+relation_name) == "insert"
    is_delete = request.POST.get("name_"+relation_name+"_delete") != ""

    return is_insert, is_delete




def do_transaction_from_form_to_table(request):
    relation_name = request.POST.get("name_selection")
    is_insert, is_delete = get_insert_delete_values(relation_name, request)

    if relation_name == "department":
        dep_code = request.POST.get('name_dep_code')
        dep_name = request.POST.get('name_dep_name')
        dep_name_delete = request.POST.get('name_dep_code_delete')

        with connection.cursor() as cursor:
            if is_delete:
                cursor.execute("CALL usp_delete_department(%s);", [dep_name_delete])
                return
            if is_insert:
                cursor.execute("CALL usp_insert_department(%s, %s);", [dep_code, dep_name])
                return
            elif not is_insert:
                cursor.execute("CALL usp_update_department(%s, %s);", [dep_code, dep_name])








def main_view(request):
    context = {}
    if request.method == 'POST':
        do_transaction_from_form_to_table(request)

        '''
        insert_or_update = request.POST.get("name_insert_or_update")

        is_delete_command = request.POST.get("name_delete_number")
        is_insert_command = is_insert(insert_or_update)
        is_update_command = not is_insert_command

        print(is_delete_command)
        print(is_insert_command)
        print(is_update_command)

        # department transactions
        if relation_name == 'depratment':
            dep_code = request.POST.get("name_dep_code")
            dep_name = request.POST.get("name_dep_name")
            dep_code_deletion = request.POST.get("name_dep_code_delete")
            with connection.cursor() as cursor:
                if is_insert_command:
                    cursor.execute("CALL usp_insert_department(%s, %s);", [dep_code, dep_name])
'''




    return render(request, 'app/module.html', context)
