from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import tasktab
from . forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class tasklistview(ListView):
    model=tasktab
    template_name='home.html'
    # context_object_name='task'

class taskdetailview(DetailView):
    model=tasktab
    template_name = 'detail.html'
    context_object_name = 'task'

class taskupdateview(UpdateView):
    model=tasktab
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class taskdeleteview(DeleteView):
    model=tasktab
    template_name='delete1.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def task(request):
    task1=tasktab.objects.all()
    if request.method=='POST':
        name=request.POST.get('task')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        task=tasktab(name=name,priority=priority,date=date)
        task.save()
    return render(request,'home.html',{'task':task1})
def delete(request,id):
    if request.method=='POST':
        task=tasktab.objects.get(id=id)
        task.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    task = tasktab.objects.get(id=id)
    form=todoform(request.POST or None,instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'edit.html',{'task':task,'form':form})
