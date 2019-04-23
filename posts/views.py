from django.shortcuts import render,redirect
from .forms import OproForm
from .models import Opro
# Create your views here.
def list(r):
    opros = Opro.objects.all()
    return render(r,'posts/list.html',{'opros':opros})
    
def create(request):
    if request.method=="POST":
        form = OproForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
            
        else:
            pass
    
    else:
        form = OproForm()
        return render(request,'posts/create.html',{'form':form})
        
def delete(request,id):
    opro=Opro.objects.get(id=id)
    opro.delete()
    return redirect("asdf:lalala")
    
def edit(request,idid):
    if request.method=='POST':
        
        pass
    else:
        opro = Opro.objects.get(id=idid)
        form = OproForm(instance=opro)
        return render(request, 'posts/edit.html',{'form':form})
    
    