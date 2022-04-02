import json
import pytest
from rest_framework.test import APIClient
from django.views.decorators.csrf import csrf_exempt



c = APIClient() 

@csrf_exempt
@pytest.mark.django_db
def test_wrong_parameter_click():
    payload = {
        "Campaignnnnn": '4510461'
    }

    response = c.post('/click', payload, format='json')
    response_dict = json.loads(response.content.decode())
    assert response_dict['Status'] == 301


@csrf_exempt
@pytest.mark.django_db
def test_wrong_value_click():
    payload = {
        "Campaign": "Wrong"
    }

    response = c.post('/click', payload, format='json')
    response_dict = json.loads(response.content.decode())
    assert response_dict['Status'] == 302

@csrf_exempt
@pytest.mark.django_db
def test_wrong_parameter_clickTime():
    payload = {
        "Campaign": 4510461,
        "End_date": "2021-11-07 03:30:00"
    }
    response = c.post('/clickTime', payload, format='json')
    response_dict = json.loads(response.content.decode())
    assert response_dict['Status'] == 301

@csrf_exempt
@pytest.mark.django_db
def test_wrong_value_clickTime():
    payload = {
        "Campaign": 4510461,
        "Start_date": 5,
        "End_date": "2021-11-07 03:30:00"
    }

    response = c.post('/clickTime', payload, format='json')
    response_dict = json.loads(response.content.decode())
    assert response_dict['Status'] == 302
