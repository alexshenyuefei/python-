from django.conf.urls import url

from demo import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^', views.task_test, name="info"),
]
