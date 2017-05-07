from __future__ import unicode_literals

from django.db import models
from ..log.models import User
from datetime import date, datetime

class TaskManager(models.Manager):
    def add_task(self, postData, id):
            errors = []
            date = postData['date']
            now = datetime.now().date()
            print date
            print now

            if len(postData['task']) < 1:
                errors.append('Task cannot be empty')

            if len(postData['time']) < 1:
                errors.append('Time cannot be empty')

            if len(postData['date']) < 1:
                errors.append('Date cannot be empty')

            # if date < now:
            #     errors.append('date cannot be in the past')


            if errors:
                return (False, errors)

            else:
                try:
                    user = User.objects.get(id=id)
                    print user
                    newobj = Task.objects.create(
                      task=postData['task'],
                      date=postData['date'],
                      time=postData['time'],
                      user_task=user,

                    )
                    return (True, newobj)

                except:
                    if errors:
                        return (False, errors)


    def delete(self, request, id):
        errors = []
        try:
            task = Task.objects.get(id=id)
            print task
            task.delete()
            return True
        except:

            return False

    def update_task(self, ids, postData):
          errors = []

          if len(postData['task']) < 1:
              errors.append('Task cannot be empty')

          if len(postData['time']) < 1:
              errors.append('Time cannot be empty')


          if errors:
              return (False, errors)

          else:
              task = Task.objects.get(id=ids)
              task.task = postData['task']
              task.status = postData['status']
              task.date = postData['date']
              task.time = postData['time']
              task.save()
              return (True, task)


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=100)
    status = models.CharField(max_length=45, default='Pending')
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    user_task = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_tasks")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TaskManager()
