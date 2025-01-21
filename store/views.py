from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import App, CustomUser
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .vercel_blob_update import add_to_blob, delete_from_blob

def is_admin(func):
    def check(request,*args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return func(request,*args, **kwargs)
        messages.error(request,'Authorised personals only!')
        return redirect('Index')
    return check

@is_admin
def admin_home(requests):
    apps = App.objects.all()
    return render(requests,'store/admin_home.html', {'apps' : apps})

@is_admin
def admin_delete_app(request,app_name):
    app = App.objects.filter(name=app_name)
    app.delete()
    messages.success(request,'App removed successfully')
    return redirect('Admin')

@is_admin
def admin_add_app(request):

    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        apk_file = request.FILES.get('apk-file')  # File input for APK
        apk_url = add_to_blob('APK',apk_file)['url']
        icon = request.FILES.get('logo')  # File input for Icon
        icon_url = add_to_blob('ICON',icon)['url']
        points = request.POST.get('points')
        
        # Ensure required fields are filled
        if not name or not description:
            return render(request, 'store/admin.html', {
                'error': 'Name and Description are required fields!',
            })

        # Create and save the App instance
        app = App(
            name=name,
            description=description,
            created_by=request.user,  # Set the user who created the app
            apk_file=apk_url,
            icon=icon_url,
            points=points
        )
        app.save()
        messages.success(request,'App added successfully')
        # Redirect or show a success message
        return redirect('Admin')  # Replace 'success_page' with your desired URL
    return render(request, 'store/admin.html')

@is_admin
def admin_view(request):
        return render(request,'store/admin.html')

@is_admin
def admin_delete_vew(requests,app_name):
    app = App.objects.filter(name=app_name)
    delete_from_blob(app.icon)
    delete_from_blob(app.apk_file)
    return render(requests,'store/delete_app.html',{'apps':app})

def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validate form data
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('/register/')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('/register/')

        # Create the user
        user = CustomUser.objects.create_user(full_name=fullname, email=email, password=password1)
        user.save()

        # Log the user in
        messages.success(request, "Registration successful!")
        login(request, user)
        return redirect('Dashboard')
    return render(request, 'store/register.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('Dashboard')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            if user.is_superuser:
                return redirect('Admin')
            else:
                return redirect('Dashboard')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('Login')

    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully!')
    return redirect('Index')

def dashboard(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        user = CustomUser.objects.get(email=request.user)
        points = user.points_earned
        return render(request, 'store/dashboard.html', {'apps': apps, 'name':request.user.full_name,'points' : points})
    messages.error(request,'No user found, Please Login')
    return redirect('Login')

def index(requests):
    return render(requests,"store/index.html")

def update_app(requests,app_name):
    app = App.objects.filter(name=app_name)
    return render(requests,'store/app_edit.html',{'apps':app})

@login_required
def update_points(request,app_name):
    screenshot = request.FILES.get('screenshot')
    app = App.objects.get(name = app_name)
    app_points = app.points
    user = CustomUser.objects.get(email = request.user)
    user.points_earned += app_points
    user.screenshot = screenshot
    user.save()
    return redirect('Dashboard')