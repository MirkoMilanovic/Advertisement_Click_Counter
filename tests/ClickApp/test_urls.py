from django.urls import reverse, resolve
from ClickApp.views import clickApi, clickTimeApi 


def test_click_url():
    path = reverse('click')
    assert resolve(path).func == clickApi


def test_clickTime_url():
    path = reverse('click_time')
    assert resolve(path).func == clickTimeApi


