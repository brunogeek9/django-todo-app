from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import TodoItem
from .forms import ItemForm
from django.contrib import messages
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None)
        if form.is_valid:
            form.save()
            all_items = TodoItem.objects.all()
            messages.success(request,('item adicionado'))
            return render(request, 'todo_list.html', {'list': all_items})            
    else:
        print('else')        
        template = loader.get_template('home.html')
        all_todos = TodoItem.objects.all()
        return render(request, 'todo_list.html', {'list': all_todos})