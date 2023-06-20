from django.db.models import Count, Sum
from django.shortcuts import get_list_or_404
from rest_framework import generics, viewsets, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination

from .serializers import DepartmentSerializer, StaffSerializer
from .models import Department, Staff


class DepartmentListView(generics.ListAPIView):
    """
    - API для получения списка департаментов (включает искусственное поле с числом
    сотрудников + поле с суммарным окладам по всем сотрудникам)
    - API со списком департаментов - без пагинации
    - доступ к списку департаментов - доступен и для анонимных пользователей
    """

    queryset = Department.objects.annotate(staff_count=Count("staff")).annotate(
        total_salary=Sum("staff__salary")
    )
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]


class StaffPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"


class StaffViewSet(
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """
    - API для получения списка сотрудников + реализовать фильтр для поиска по фамилии и по id департамента
    - Добавление/удаление сотрудников через API
    - API со списком сотрудников - с пагинацией
    - Доступ к списку сотрудников - только для авторизованных пользователей
    """

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = StaffPagination

    def get_queryset(self):
        if last_name := self.request.query_params.get("last_name"):
            return get_list_or_404(Staff, last_name=last_name)
        elif department := self.request.query_params.get("department"):
            return get_list_or_404(Staff, department=department)

        return super().get_queryset()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes += [IsAuthenticated]

        return super().get_permissions()

