from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'account/index.html')
def AdminWelcome(request):
    return render(request,'account/admin_welcome.html')
def DoctorWelcome(request):
    return render(request,'account/doctor_welcome.html')
def PatientWelcome(request):
    return render(request,'account/patient_welcome.html')
def Login(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request,user)
                return redirect('admin_welcome')
            elif user is not None and user.is_doctor:
                login(request,user)
                return redirect('doctor_welcome')
            elif user is not None and user.is_patient:
                login(request,user)
                return redirect('patient_welcome')
            else:
                msg = "Invalid Credentails"
    form = LoginForm()
    context = {'form':form}
    return render(request,'account/login.html',context)
def Register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login')
        else:
            msg = 'form is not valid'
    else:
        form = RegisterForm()
    return render(request,'account/register.html', {'form': form, 'msg': msg})

def Logout(request):

    logout(request)
    return redirect('login')