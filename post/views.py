from django.shortcuts import render, redirect
from .models import Form,Product
from .forms import Form2, Form1, Form3, Form4
# Create your views here.

def form_view(request):
    form = Form1(request.POST)
    if request.GET.get("form_id"):
        form = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form1(instance=form)

    if request.method == 'POST':
        obj = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form1(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save()
            id = instance.id or form.id
            return redirect(f"/form2?form_id={id}")
    return render(request,'index.html',{"form":form, })


def form2_view(request):
    
    data =Product.objects.all()
    
    form = Form2(request.POST)
    if request.GET.get("form_id"):
        form = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form2(instance=form)

    if request.method == 'POST':
        obj = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form2(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save()
            id = instance.id or form.id
            return redirect(f"/form3?form_id={id}")
    return render(request,'form2.html',{"form":form,'data':data})



def form3_view(request):
    form = Form3(request.POST)
    if request.GET.get("form_id"):
        form = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form3(instance=form)

    if request.method == 'POST':
        obj = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form3(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save()
            id = instance.id or form.id
            return redirect(f"/form4?form_id={id}")
    return render(request,'form3.html',{"form":form})



def form4_view(request):
    form = Form4(request.POST)
    if request.GET.get("form_id"):
        form = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form4(instance=form)

    if request.method == 'POST':
        obj = Form.objects.filter(id=request.GET.get("form_id")).first()
        form = Form4(request.POST, instance=obj)
        if form.is_valid():
            instance = form.save()
            id = instance.id or form.id
            return redirect(f"/form5?form_id={id}")        
    return render(request,'form4.html',{"form":form})



def form5_view(request):
    my_sub = Form.objects.filter(id=request.GET.get("form_id")).first()

    context = {
        'my_sub': my_sub,
    }   
    return render(request,'form5.html',context)



def final_view(request):
    return render(request,'final.html',{})