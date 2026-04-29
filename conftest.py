import pytest
from selenium import webdriver

from helpers import generate_login, generate_name, generate_pass
from urls import API_CREATE_USER, API_DELETE_USER, BASE_URL
import requests


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def user():
    email = generate_login()
    password = generate_pass()
    name = generate_name()
    response = requests.post(
        API_CREATE_USER,
        json={"email": email, "password": password, "name": name})
    access_token = response.json().get("accessToken")
    yield {
        "email": email,
        "password": password,
        "token": access_token}

    requests.delete(
        API_DELETE_USER,
        headers={"Authorization": access_token})
