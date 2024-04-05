from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('add',views.addtask,name='addtaskpage'),
    path('view',views.viewtask,name="viewpage"),
    path('delete/<id>',views.deletetask,name='deletetaskpage'),
    path('deletee',views.deletealltask,name="alltask"),
    path('edit/<id>',views.edittask,name="editpage"),
    path('signup', views.signup,name='signupPage'),
    path('signin',views.signin,name='signinpage'),
    path('signout',views.signout,name='signoutpage')

]
