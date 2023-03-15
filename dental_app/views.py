from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from dental_app.forms import patientForm
from dental_app.models import patient
import random
from django.db.models import Q
import statistics
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.

def index(request):
    return render (request,"home_page.html")

def add_patient(request):
    form=patientForm
    if request.method=="POST":
        form=patientForm(request.POST)
        branch=form.data["branch"]
        date=form.data["date"]
        first_name=form.data["first_name"]
        last_name=form.data["last_name"]
        id_number=form.data["id_number"]
        doctor=form.data["doctor"]
        photo_type=form.data["photo_type"]
        deal_number=form.data["deal_number"]
        price_type=form.data["price_type"]
        credit=int(form.data["credit"])+random.randrange(1,200)
        cash=form.data["cash"]
        reimbursement_from_insurance=form.data["reimbursement_from_insurance"]
        reference_number=form.data["reference_number"]
        invoicing_number=form.data["invoicing_number"]
        way=form.data["way"]
        photographer_name=form.data["photographer_name"]
        p=patient(branch=branch,
        date=date,
        first_name=first_name,
        last_name=last_name,
        id_number=id_number,
        doctor=doctor,
        photo_type=photo_type,
        deal_number=deal_number,
        price_type=price_type,
        credit=credit,cash=cash,
        reimbursement_from_insurance=reimbursement_from_insurance,reference_number=reference_number,
        invoicing_number=invoicing_number,
        way=way,
        photographer_name=photographer_name)
        p.save()
        return display_big_table(request,f"!{first_name+' '+last_name} הוסף בהצלחה")
    else:
        return render(request,"add_patient.html",{'form':form})

def display_big_table(request,message=''):
    patients=patient.objects.all()
    # p=Paginator(patients,10)
    # page=request.GET.get('page')
    # patient_list=p.get_page(page)
    # nums="a"*patient_list.paginator.num_pages

    context = {'patients':reversed(patients),'message':message}

    return render(request,"display_big_table.html",context=context)

def remove(request):
    if request.method=="POST":
        form=patientForm(request.POST)
        id=form.data["id"]
        first_name=form.data["first_name"]
        patients=patient.objects.get(id=id)
        patients.delete()
        return display_big_table(request, f'נמחק - {first_name}')
    else:
        return HttpResponse("remove")

def remove_from_reshon(request):
    if request.method=="POST":
        form=patientForm(request.POST)
        id=form.data["id"]
        first_name=form.data["first_name"]
        patients=patient.objects.get(id=id)
        patients.delete()
        return reshon(request, f'נמחק - {first_name}')
    else:
        return HttpResponse("remove")

def remove_from_tel_aviv(request):
    if request.method=="POST":
        form=patientForm(request.POST)
        id=form.data["id"]
        first_name=form.data["first_name"]
        patients=patient.objects.get(id=id)
        patients.delete()
        return tel_aviv(request, f'נמחק - {first_name}')
    else:
        return HttpResponse("remove")

def reshon(request,message=''):
    patients=patient.objects.filter(branch="ראשון לציון")
    return render(request,"reshon.html",{'patients':reversed(patients),'message':message})

def tel_aviv(request,message=''):
    patients=patient.objects.filter(branch="תל אביב")
    return render(request,"tel_aviv.html",{'patients':reversed(patients),'message':message})

def results(request):
    q=request.GET["q"]
    patients=patient.objects.filter(
    Q(first_name__contains=q) | 
    Q(last_name__contains=q) | 
    Q(branch__contains=q) | 
    Q(date__contains=q)  | 
    Q(doctor__contains=q) | 
    Q(price_type__contains=q) | 
    Q(way__contains=q) | 
    Q(photographer_name__contains=q)
    )
    context={'search_results':patients,'q':q}
    if patients:
        return render(request, "results.html", context=context)
    else:
        return render(request, "no_results.html",{'q':q})

def reports2(request):
    a=str(request.GET.get("a"))
    b=str(request.GET.get("b"))
    c=str(request.GET.get("c"))
    d=str(request.GET.get("d"))
    e=str(request.GET.get("e"))
    f=str(request.GET.get("f"))
    
    patients=patient.objects.filter(
    Q(branch__contains=a) &
    Q(date__contains=b) &
    Q(doctor__contains=c) &
    Q(price_type__contains=d) & 
    Q(way__contains=e) &
    Q(photographer_name__contains=f)
    )
    
    context={'search_reports':reversed(patients)}
    return render(request,"reports2.html", context=context)

def analysis(request):
    patients=patient.objects.all()
    prices=[p.credit+p.cash for p in patients]
    maximum=max(prices)
    minimum=min(prices)
    avg=statistics.mean(prices)
    avg=round(avg,2)
    return render(request,"analysis.html",{'maximum':maximum, 'avg':avg, 'minimum':minimum})    

def view_patient(request):
    id=request.GET["id"]
    patient_view=patient.objects.get(id=id)
    context={'p':patient_view}
    print(context)
    return render(request,'patient_view.html', context=context)

def contact(request):
    return render (request, "contact.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.success(request, ("There was an Error logging in, Try again..."))
            return redirect('login')

    else:
        return render (request, "authenticate/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were Logged out!"))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,("Registration Successfull"))
            return redirect('home')
    else:
        form = UserCreationForm()


    return render(request, 'authenticate/register_user.html', {'form':form})