from django.contrib import admin
from django.urls import path
from todos import views
urlpatterns = [
    # path('',views.index,name='home'),
    path('',views.home,name='home1'),
    # path('delete/<int:item_id>/',views.delete_todo, name='delete_todo')
    path('delete/<item_id>',views.delete_todo, name='delete'),
    path('change_todo/<item_id>',views.change_todo, name='change_todo'),
    path('edit_todo/<item_id>', views.edit_todo, name='edit_todo')
    
]
