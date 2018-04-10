from django.urls import path
from . import views

app_name = 'cave'

urlpatterns = [
    path('list/', views.find_all_cave, name='cave_list'),
    path('<int:id>/', views.find_cave_by_id, name='cave_by_id'),
    path('search/', views.search_for_cave, name='search_for_cave'),
]
