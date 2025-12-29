from django.test import TestCase



import json
import pytest
from django.test import Client

@pytest.mark.django_db
def test_create_task():
    client = Client()
    response = client.post(
        "/api/tasks/create/",
        data=json.dumps({"title": "Test Task"}),
        content_type="application/json",
    )
    assert response.status_code == 201

def test_list_tasks():
    client = Client()
    response = client.get("/api/tasks/")
    assert response.status_code == 200

