# User upcoming events view for user_home navigation
def user_upcoming_event(request):
    if not request.user.is_authenticated:
        return redirect('login')
    events = upcoming_event.objects.all()
    return render(request, 'user_upcoming_event.html', {'events': events})
def register_event(request, event_id):
    if not request.user.is_authenticated:
        return redirect('login')
    event = upcoming_event.objects.get(id=event_id)
    # Check if already registered
    already_registered = EventRegistration.objects.filter(user=request.user, event_name=event).exists()
    if not already_registered:
        EventRegistration.objects.create(user=request.user, event_name=event)
    return redirect('user_home')
from django.contrib.auth import logout as django_logout
from django.shortcuts import render,redirect
from django.contrib.auth.models import *
from django.contrib.auth import authenticate,logout,login
from .models import *
def index(request):
    events = upcoming_event.objects.all()
    d = {'events': events}
    return render(request,'index.html', d)

def signin(request):
    error=""
    if request.method=="POST":
        u = request.POST['uname']
        p = request.POST['pswd']
        user = auth.authenticate(username=u,password=p)
        try:
            if user.is_staff:
                auth.login(request,user)
                error="no"
            elif user is not None:
                error="not"
                auth.login(request,user)
                return redirect('user_home')
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)

def signup(request):
    error = ""
    if request.method=='POST':
        f=request.POST['fname']
        l=request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        i=request.FILES['image']
        d=request.POST['dob']
        a=request.POST['add']
        try:
            user=User.objects.create_user(first_name=f,last_name=l,username=e,password=p)
            Signup.objects.create(user=user,mobile=con,gender=gen,image=i,dob=d,address=a)
            error="no"
        except:
            error="yes"
    di={'error':error}
    return render(request,'signup.html',di)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    registered_events = EventRegistration.objects.filter(user=request.user)
    d = {'registered_events': registered_events}
    return render(request, 'user_home.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request,'admin_home.html')
# write code to view user details in admin home page
def view_users(request):
    users = Signup.objects.all()
    d = {'users': users}
    return render(request, 'view_user.html', d)

def upcoming_events(request):
    events = upcoming_event.objects.all()
    d = {'events': events}
    return render(request,'upcoming_event.html', d)

# Add view for adding upcoming events
def add_upcoming_event(request):
    error = ""
    if request.method == "POST":
        event_name = request.POST.get('event_name')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        try:
            upcoming_event.objects.create(
                event_name=event_name,
                event_date=event_date,
                event_time=event_time,
                location=location,
                description=description,
                image=image
            )
            error = "no"
        except Exception as e:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_upcoming_event.html', d)

def logout(request):
    django_logout(request)
    return redirect('index')
# Admin CRUD for upcoming events
def manage_upcoming_event(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')
    events = upcoming_event.objects.all()
    return render(request, 'manage_upcoming_event.html', {'events': events})

def update_upcoming_event(request, event_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')
    event = upcoming_event.objects.get(id=event_id)
    error = ""
    if request.method == "POST":
        event.event_name = request.POST.get('event_name')
        event.event_date = request.POST.get('event_date')
        event.event_time = request.POST.get('event_time')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        if 'image' in request.FILES:
            event.image = request.FILES['image']
        try:
            event.save()
            error = "no"
            return redirect('manage_upcoming_event')
        except Exception as e:
            error = "yes"
    return render(request, 'add_upcoming_event.html', {'event': event, 'error': error})

def delete_upcoming_event(request, event_id):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login')
    try:
        event = upcoming_event.objects.get(id=event_id)
        event.delete()
    except upcoming_event.DoesNotExist:
        pass
    return redirect('manage_upcoming_event')