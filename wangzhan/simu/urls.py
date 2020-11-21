from django.urls import path
from . import views

app_name="simus"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:simu_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:simu_id>/edit/', views.edit, name='edit'),
    path('<int:simu_id>/update/', views.update, name='update'),
    path('<int:simu_id>/delete/', views.delete, name='delete'),
    path('search_result/', views.search_result, name='search_result'),
    path('<int:simu_id>/like/', views.like, name='like'),
]