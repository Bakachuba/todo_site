from django.shortcuts import redirect, render
from django.contrib import messages

from todo.models import Todo
from .forms import TodoForm


def index(request):
    item_list = Todo.objects.order_by('-date')

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # Save the form data to create a new Todo instance
            todo_instance = form.save(commit=False)
            todo_instance.save()
            return redirect('todo')

    form = TodoForm()

    page = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST',
    }
    return render(request, 'index.html', page)


def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, 'Item removed')
    return redirect('todo')
