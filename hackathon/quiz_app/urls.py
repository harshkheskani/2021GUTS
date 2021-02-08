from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views

app_name = "quiz-app"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("category/", views.category_select, name="category"),
    path("user/profile/", views.profile, name="profile"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("<slug:category_name_slug>/question/", views.question, name="question"),
    path("json-test/", views.json_test, name="json-test"),
    path("<slug:category_name_slug>/add-question/", views.new_question, name="add-question")
    ]
