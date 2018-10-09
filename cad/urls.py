from django.urls import path
from . import views

urlpatterns = [
    path('cads', views.index, name='agenda-cads-index'),
    path('all', views.all, name='agenda-cads-all'),
    path('<int:id>', views.show, name='agenda-cads-show'),
    path('<int:year>/<int:month>/<int:day>', views.day, name='agenda-cads-day'),
    path('new', views.new, name='agenda-cads-new'),
    path('delete/<int:id>', views.delete, name='agenda-cads-delete'),
    path('edit', views.edit, name='agenda-cads-edit'),
    ]