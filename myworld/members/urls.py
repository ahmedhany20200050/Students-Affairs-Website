from django.urls import path
from . import views

urlpatterns = [
  path('', views.startPage, name='start'),
  path('login_screen',views.login,name='loginScreen'),
  path('homepage',views.homepage,name='homepage'),
  path('active-inactive',views.active_inactive,name='active-inactive'),
  path('search',views.search,name='search'),
  path('addStudentPage',views.addStudentPage,name='addStudentPage'),
  path('editPage',views.editPage,name='editPage'),
  path('department_assignment',views.department_assignment,name='department_assignment'),
  #end of rendering links
  
  path('validate',views.validate,name='validate'),
  path('addStudent',views.addStudent,name='addStudent'),
  path('getStudents',views.getStudents,name='getStudents'),
  # path('delete',views.delete,name='delete'),
  path('updateStudents',views.updateStudents,name='updateStudents'),
  path('changeStatus/<int:id>',views.changeStatus,name='changeStatus'),
  path('getSt',views.getSt,name='getST'),
  path('assign/<int:id>',views.assign,name='assing'),
  path('change_status/<int:pk>',views.change_status,name="change_status")

  # path('')
  # path('add/', views.add, name='add'),
  # path('add/addrecord/', views.addrecord, name='addrecord'),
  # path('delete/<int:id>', views.delete, name='delete'),
  # path('update/<int:id>', views.update, name='update'),
  # path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
