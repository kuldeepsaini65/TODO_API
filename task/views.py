from django.shortcuts import render, HttpResponse
import json
import logging
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from task.db_con import *
from django.db import connection
logger = logging.getLogger(__name__)
import requests
from django.contrib import messages


def documentation(request):
    return render(request, 'docs.html')




# API Definations for CRUD operations
@csrf_exempt

def create_task_api(request):
    if request.method != "POST":
        return JsonResponse(
            {"status": "error", "message": "Only POST allowed"},
            status=405
        )

    try:
        data = json.loads(request.body)

        if type(data) == type(dict()):
            data = [data]

        with connection.cursor() as cursor:
            row = 0
            for task in data:
                cursor.execute(
                    """
                    INSERT INTO tasks (title, description, due_date, status)
                    VALUES (%s, %s, %s, %s)
                    """,[
                    task["title"],
                    task["description"],
                    task["due_date"],
                    task["status"]
                    ]
                )

                row= row + cursor.rowcount
            print(row)

        return JsonResponse(
            {"status": "success", "message": f"{row} Task(s) created"},
            status=201
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )


def list_tasks_api(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, title, description, due_date, status FROM tasks")
        rows = cursor.fetchall()

        tasks = [
            {
                "id": r[0],
                "title": r[1],
                "description": r[2],
                "due_date": r[3],
                "status": r[4],
            }
            for r in rows
        ]
    return JsonResponse({'status':'success', 'data':tasks} , safe=False)


@csrf_exempt
def task_update_api(request, id):
    if request.method != "PUT":
        return JsonResponse(
            {"status": "error", "message": "Only PUT method allowed"},
            status=405
        )

    try:
        payload = json.loads(request.body)

        title = payload.get("title")
        description = payload.get("description")
        due_date = payload.get("due_date")
        status = payload.get("status")

        with connection.cursor() as cursor:
            cursor.execute(
                """
                UPDATE tasks
                SET title=%s, description=%s, due_date=%s, status=%s
                WHERE id=%s
                """,
                [title, description, due_date, status, id]
            )
            updated = cursor.rowcount

        if updated == 0:
            return JsonResponse(
                {"status": "error", "message": "Task not found"},
                status=404
            )

        return JsonResponse(
            {
                "status": "success",
                "data": {
                    "id": id,
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                    "status": status
                }
            },
            status=200
        )

    except Exception as e:
        return JsonResponse(
            {"status": "error", "message": str(e)},
            status=500
        )


def task_info_api(request, id):
    if request.method != 'GET':
        return JsonResponse(
            {"status":"failed",
             "data": "Only GET request is allowed"},
            status=405
        )
    
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute(
            """
            SELECT id, title, description,due_date, status
            FROM tasks
            WHERE id = %s
            """,
            [id]
            )
            rows = cursor.fetchone()
            

            if rows:
                data = {
                'id' : rows[0],
                'title' : rows[1],
                'description' : rows[2],
                'due_date' : rows[3],
                'status' : rows[4],
            }
                return JsonResponse(
                    {'status' : 'success', 'data':data}, status = 200
                )
            
            else:
                return JsonResponse(
                    {'status' : 'error', 'data':'not found'}, status = 404
                )



@csrf_exempt
def task_delete_api(request,id):
    if request.method ==  'DELETE':
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM tasks WHERE id = %s ", [id])
            num_deleted = cursor.rowcount 
    
            if num_deleted > 0:
                status = 'success'
                response = f"Successfully deleted {num_deleted} task(s)."
            else:
                status = 'failed'
                response = "No task found with that ID."

        return JsonResponse({'status':status, 'data':response})
    
    else:
        return JsonResponse(
            {
                'status':'failed',
                'data' : 'this method is not valid'
            }
        )





# View Functions for App Internal User


def task_list_view(request):
    base_url = "http://127.0.0.1:8000/api/tasks/"
    response = requests.get(base_url)
    data = response.json()
    print(data['data'])
    return render(request, "tasks/task_list.html", {"tasks": data['data']})


@csrf_exempt
def task_add_view(request):
    create_url = "http://127.0.0.1:8000/api/tasks/create/"
    if request.method == "POST":

        data = {
        'title' : request.POST.get('title'),
        'description' : request.POST.get('description'),
        'due_date' : request.POST.get('due_date'),
        'status' : request.POST.get('status'),
        }

        payload = requests.post(create_url, data = json.dumps(data))
        result = payload.json()
        print(result)

        return redirect("task:task_list")

    return render(request, "tasks/task_add.html")



def task_info_view(request, id):
    base_url = 'http://127.0.0.1:8000/api/tasks/'
    url = base_url  + str(id)
    context = {}

    response = requests.get(url)
    data = response.json()
    print(data)
    if data['status'] == 'success':
        context['title'] = data['data']['title']
        context['description'] = data['data']['description']
        context['due_date'] = data['data']['due_date']
        context['status'] = data['data']['status']

    return render(request, 'tasks/task_info.html', context)



def task_update_view(request, id):
    update_url = 'http://127.0.0.1:8000/api/tasks/update/' + str(id)
    get_url = 'http://127.0.0.1:8000/api/tasks/' + str(id)


    context = {}
    if request.method == "GET":
        response = requests.get(get_url)
        data = response.json()
        print(data)
        if data['status'] == 'success':
            context['title'] = data['data']['title']
            context['description'] = data['data']['description']
            context['due_date'] = data['data']['due_date']
            context['status'] = data['data']['status']
            context['update'] = True



    if request.method == "POST":
        payload = {
            "title": request.POST.get("title"),
            "description": request.POST.get("description"),
            "due_date": request.POST.get("due_date"),
            "status": request.POST.get("status"),
        }


        response = requests.put(
            update_url,
            data=json.dumps(payload)
        )

        result = response.json()

        if result.get("status") == "success":
            return redirect("task:task_list")  

        return render(request, "tasks/task_add.html", context)

    return render(request, 'tasks/task_add.html', context)


@csrf_exempt
def task_delete_view(request, id):
    url = "http://127.0.0.1:8000/api/tasks/delete/" + str(id)

    response = requests.delete(url)
    result = response.json()
    if result['status'] == 'success':
        messages.success(request, str(result['data']))
    else:
        messages.error(request, str(result['data']))
    
    return redirect('task:task_list')
