from django.shortcuts import render, redirect
from .models import Task, User
from datetime import date, datetime
from django.contrib import messages
# Create your views here.
def index(request):
    ids = request.session['id']
    date = datetime.now().date()
    context = {
    'task': Task.objects.filter(user_task=User.objects.get(id=request.session['id'])),
    'user': User.objects.get(id=request.session['id']),
    'date': date
    }
    return render(request, 'appointment/index.html', context)

def add(request):
    if request.method == 'POST':
        valid, data = Task.objects.add_task(request.POST, request.session['id'])
        if valid:
            return redirect('appoint:index')
        else:
                for err in data:
                    messages.error(request, err)
                return redirect('appoint:index')

def task(request, id):
    request.session['book_id'] = id
    context = {
    'appointments': Task.objects.get(id=id),
    'curr_user': User.objects.get(id=request.session['id'])
    }
    return render(request, 'appointment/task.html', context)

def delete(request, rev_id):
    delete = Task.objects.delete(request, rev_id)
    return redirect('appoint:index')

def update_task(request):
    if request.method == 'POST':
        ids = request.session['book_id']
        valid, data = Task.objects.update_task(ids, request.POST)
        if valid:
            return redirect('appoint:index')
        else:

            for err in data:
                messages.error(request, err)
            return redirect('appoint:task', request.session['book_id'])
