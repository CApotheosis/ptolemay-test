from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register("staff", views.StaffViewSet)

app_name = "staff"

urlpatterns = [
    path("", include(router.urls)),
    path("departments/", views.DepartmentListView.as_view(), name="department_list"),
]
