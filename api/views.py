from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json



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
    api_key = request.api_key

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
def task_delete_api(request, id):

    if request.method != 'DELETE':
        return JsonResponse(
            {
                'status': 'failed',
                'data': 'Only DELETE method is allowed'
            },
            status=405
        )

    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "DELETE FROM tasks WHERE id = %s",
                [id]
            )
            num_deleted = cursor.rowcount

        if num_deleted > 0:
            return JsonResponse(
                {
                    'status': 'success',
                    'data': f"Successfully deleted {num_deleted} task(s)."
                },
                status=200
            )
        else:
            return JsonResponse(
                {
                    'status': 'failed',
                    'data': 'No task found with that ID.'
                },
                status=404
            )

    except Exception as e:
        return JsonResponse(
            {
                'status': 'error',
                'message': str(e)
            },
            status=500
        )


