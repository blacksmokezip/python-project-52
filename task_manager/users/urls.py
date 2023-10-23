from django.urls import path
from task_manager.users import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='users'),
    path('create/', views.UserFormCreateView.as_view(), name='users_create'),
    path('<int:id>/update/', views.UserFormUpdateView.as_view(), name='users_update'),
    path('<int:id>/delete/', views.UserFormDeleteView.as_view(), name='users_delete'),
]
