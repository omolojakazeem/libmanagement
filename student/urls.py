from django.urls import path
from .views import add_student, student_index,student_detail,delete_student

app_name = 'student'

urlpatterns = [
    path('', student_index, name='student_index'),
    path('add_student/', add_student, name='add_student'),
    path('student_detail/<int:id>/', student_detail, name='student_detail'),
    path('delete_student/<int:id>/', delete_student, name='delete_student'),
]