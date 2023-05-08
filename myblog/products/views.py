from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404,redirect
from .models import *
from django import forms
from .forms import *

# Create your views here.
def home(request):
    return render(request, "index.html")

def head(request):
    return render(request, "head.html")

def services(request):
    return render(request, "services.html")

def seemessages(request):
     messages=visitor.objects.all()
     return render(request, "portfolio.html",{"messages":messages})
def seecontent(request,slug,time):
    visitors=visitor.objects.filter(slug=slug,time=time)
    return render(request, "portfolio-details.html",{'visitors':visitors})

def About(request):

    return render(request, 'about.html')

def Contact(request):
    if request.method =='POST':
        form=visitorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Contact')
    else:
        form = visitorForm()    
    return render(request, "contact.html",{'form':form})

def visitorupload(request):    
        if request.method =='POST':
            form=visitorForm(request.POST, request.FILES)

            if form.is_valid():
                form=visitorForm(request.POST, request.FILES)
                name=form.cleaned_data['name']
                gmail=form.cleaned_data['gmail']
                subject=form.cleaned_data['subject']
                content=form.cleaned_data['content']
                form.save()
                return redirect('Contact')
        else:
            form = visitorForm()
        return render(request, 'contact.html',{'form':form})

def upload(request):    
        if request.method =='POST':
            form=imageForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('seeupload')
        else:
            form = imageForm()
        return render(request, 'upload.html',{'form':form})

def delete_upload(request, services):
    pics = images.objects.get(pk=services)
    context = {'item':pics}
    return render(request,'delete_upload.html',context)

 
def admin_page(request):
    return render(request, "admin_page.html")

# def seeupload(request):
#     if request .method =="GET":

#         picture=images.objects.all()
#         return render(request, 'seeupload.html',{'picture':picture})

def seeupload(request):
        return render(request, 'seeupload.html')

def footer(request):
        return render(request, 'testimonials.html')


def piercing(request):
    photo3=images.objects.filter(services="piercing")
    if images.objects.filter(services="piercing"):
        return render(request,'piercing.html',{'photo3':photo3})
    # PiercingIMG=images.objects.filter(services="piercing")
    # if images.objects.filter(services="piercing"):
    #    return HttpResponse("hello world")
def seeselectedupload(request):
    photo=images.objects.filter(services="facial")
    if images.objects.filter(services="facial"):
        return render(request,'facial.html',{'photo':photo})
    else:
        return HttpResponse("nothing here to see")
def seemassage(request):
    photo1=images.objects.filter(services="massage")
    if images.objects.filter(services="massage"):
        return render(request,'massage.html',{'photo1':photo1})
    else:
        return HttpResponse("nothing here to see")
def seeskincare(request):
    photo2=images.objects.filter(services="skincare")
    if images.objects.filter(services="skincare"):
        return render(request,'skincare.html',{'photo2':photo2})
    else:
        return HttpResponse("nothing here to see")
def hairtreatment(request):
    photo4=images.objects.filter(services="hair treatment")
    if images.objects.filter(services="hair treatment"):
        return render(request,'hairtreatment.html',{'photo4':photo4})
    else:
        return HttpResponse("nothing here to see")
def nailtreatment(request):
    photo5=images.objects.filter(services="nail treatment")
    if images.objects.filter(services="nail treatment"):
        return render(request,'nailtreatment.html',{'photo5':photo5})
    else:
        return HttpResponse("nothing here to see")


        # return render(request,'nailtreatment.html',{'photo5':photo5})

def servicelandpage(request):
    return render(request, "servicelandpage.html")

def delete(request ,services):
    obj = get_object_or_404(images, id=services)
    if request.method == "POST":
        obj.delete()
    context={
        "object":obj
    }
    return render(request,'seeupload.html',context)

# def gdetail(request):
#     news=gmodel.objects.all()
#     data={
#         'news':news
#     }
#     return render(request, 'news_detail.html',data)



# def delete(request ,services):
#     delt=images.objects.filter(services="massage").delete()
#     return redirect('seeupload')
#     # if images.objects.filter(services="massage"):
#     #     return ren  der(request,'seeupload.html',{'photo1':photo1})

# def spar_view(request,services):
#     obj = images.objects.get(id=services)
#     context = {
#        ' object': obj
#     }
#     return render(request, 'spar_view.html', context)
   

#    -- delete function --
def index(request):
    obj=images.objects.all()
    return render(request, 'homepage.html',{"obj":obj})

def detail(request,id):
    obj=get_object_or_404(images,pk=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect('index')
    return render(request,"detail.html",{"obj":obj})


# def delete_event(request, services):
#     obj=images.objects.get(pk=services)
#     obj.delete()
#     return redirect('index')
#     # return render(request,"homepage.html",{"obj":obj})



# <a href="{% url 'delete-event' x.services %}" style="background-color: red;">delete</a>


