from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import date, datetime
from .models import courses
from django.contrib import messages
# users.objects.create(fname = "Grooby", lname = "Mcbuckets", email = "grooby@mail.com" )
# users.objects.create(fname = "snookel", lname = "batboy" , email = "batboy@mail.com")
# users.objects.create(fname = "gluk", lname = "mkruk" , email = "ghat@mail.com")
# users.objects.create(fname = "poof", lname = "D'Scroof" , email = "sroo@mail.com")
def index(request):
    queries = courses.objects.all().order_by("created_at")
    context = {'courses' : queries}
    return render(request, "django_app/users.html", context)
# def new(request):
#     return render(request,"django_app/add_user.html")
# def update(request,id):
#     if request.method == "POST":
#         errors = courses.objects.basic_validator(request.POST)
#         if len(errors):
#             for error in errors:
#                 messages.add_message(request, messages.INFO, error)
#         else:
#             this_user = users.objects.get(id = str(id))
#             this_user.fname = request.POST['fname']
#             this_user.lname = request.POST['lname']
#             this_user.email = request.POST['email']
#         return redirect(("/"))
#     else:
#         return redirect(("/"))
def create(request):
    if request.method == "POST":
        errors = courses.objects.basic_validator(request.POST)
        if len(errors):
            for error in errors:
                messages.add_message(request, messages.INFO, error)
        else:
            courses.objects.create(name = request.POST['name'], desc = request.POST['desc'])
        return redirect(("/"))
    else:
        return redirect(("/"))
    return redirect('/')
def show(request, id):
    this_course = courses.objects.get(id = str(id))
    print('SHOW::',this_course)
    context = {'ID' : this_course.id,
                'name' : this_course.name,
                'desc' : this_course.desc,
                'created_at' : this_course.created_at}
    return render(request,"django_app\show_user.html", context)
# def edit(request, id):
#     this_user = users.objects.get(id = str(id))
#     print('EDIT::',this_user)
#     context = {'ID' : this_user.id,
#                 'fname' : this_user.fname,
#                 'lname' : this_user.lname,
#                 'email' : this_user.email,
#                 'created_at' : this_user.created_at}
#     return render(request, "django_app\edit_user.html", context)
def destroy(request, id):
    this_course = courses.objects.get(id = str(id))
    print('DESTROY::',this_course)
    this_course.delete()
    return redirect('/')