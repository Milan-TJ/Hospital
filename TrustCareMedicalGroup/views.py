from django.shortcuts import render,redirect
from.models import Doctor,Patient
from.forms import AddDoctor,AddPatient,LoginDoctor,LoginPatient

def home(request):
    return render(request,'index.html')

def AboutUs(request):
    cr=Doctor.objects.all()
    return render(request,'about.html',{'cm':cr})

def Doctorlogin(request):
    request.session['UserType']="Doctor"
    if request.method=='POST':
             email=request.POST.get('email')
             password=request.POST.get('password')
             chkemail=Doctor.objects.filter(email=email)
             if chkemail:
                   cr= Doctor.objects.filter(email=email,password=password)
                   if cr:
                       Doctor_details=Doctor.objects.get(email=email,password=password)
                       id=Doctor_details.id
                       request.session['id']=id
                       return redirect("DoctorView")
                   else:
                       valid="password is incorrect"
                       return render(request,'login.html',{'valid2':valid,'UserType':"Doctor"})  
             else:
                 valid="Enter a proper email address"
                 return render(request,'login.html',{'valid1':valid,'UserType':"Doctor"})  
    else:
        return render(request,'login.html',{'UserType':"Doctor"})

def Patientlogin(request):
    request.session['UserType']="Patient"
    if request.method=='POST':
             email=request.POST.get('email')
             password=request.POST.get('password')
             chkemail=Patient.objects.filter(email=email)
             if chkemail:
                   cr= Patient.objects.filter(email=email,password=password)
                   if cr:
                       Doctor_details= Patient.objects.get(email=email,password=password)
                       id=Doctor_details.id
                       request.session['id']=id
                       return redirect("ViewDetails")
                   else:
                       valid="password is incorrect"
                       return render(request,'login.html',{'valid2':valid,'UserType':"Patient"})  
             else:
                 valid="Enter a proper email address"
                 return render(request,'login.html',{'valid1':valid,'UserType':"Patient"})  
    else:
        return render(request,'login.html',{'UserType':"Patient"})

def DoctorRegister(request):
    form1 = AddDoctor()
    if request.method=='POST':
        form1=AddDoctor(request.POST,request.FILES)
        if form1.is_valid():
                form1.save()
                return redirect("Doctorlogin")
    return render(request,'register.html',{'form1':form1,'UserType':"Doctor"})


def PatientRegister(request):
    form2 = AddPatient()
    if request.method=='POST':
        form2 = AddPatient(request.POST,request.FILES)
        if form2.is_valid():
                form2.save()
                return redirect("Patientlogin")
    return render(request,'register.html',{'form2':form2,'UserType':"Patient"})

def EditDoctor(request,pk):
    cr = Doctor.objects.get(id=pk)
    form1 = AddDoctor(instance=cr)
    if request.method=='POST':
          form1 =  AddDoctor(request.POST,instance=cr)
          if form1.is_valid():
               form1.save()
               return redirect("DoctorView")
    return render(request,'register.html',{'form1':form1,'UserType':"Doctor"})


def EditPatient(request,pk):
    cr = Patient.objects.get(id=pk)
    form2 = AddPatient(instance=cr)
    if request.method=='POST':
          form2 =  AddPatient(request.POST,instance=cr)
          if form2.is_valid():
               form2.save()
               return redirect("ViewDetails")
    return render(request,'register.html',{'form2':form2,'UserType':"Patient"})

def ViewDetails(request,pk):
         cr = Patient.objects.get(id=pk)
         return render(request,'viewprofile.html',{'cm':cr})

def ViewDetails(request):
        pid=request.session['id']
        cr = Patient.objects.get(id=pid)
        cq = Doctor.objects.get(id=cr.doctor_id)
        return render(request,'viewprofile.html',{'cm':cr,'cn':cq})

    
def DoctorView(request):
    did=request.session['id']
    cr = Doctor.objects.get(id=did)
    cdp= Patient.objects.filter(doctor_id=did)
    return render(request,'doctorprofile.html',{'cm':cr,'cn':cdp})

def AdminView(request):
    return render(request,'admin.html')


