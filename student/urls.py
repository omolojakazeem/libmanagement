from django.urls import path
from .views import add_student, student_index
urlpatterns = [
    path('', student_index, name='student_index'),
    path('add_student/', add_student, name='add_student')
]