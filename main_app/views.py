from django.shortcuts import render, redirect
from .models import Bird, Shirt
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })
   
def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  feeding_form = FeedingForm()

  shirts_bird_doesnt_have = Shirt.objects.exclude(id__in = bird.shirts.all().values_list('id'))
  
  return render(request, 'birds/detail.html', { 
    'bird': bird, 
    'feeding_form': feeding_form,
    'shirts' : shirts_bird_doesnt_have,
    })

def add_feeding(request, bird_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.bird_id = bird_id
        new_feeding.save()
    return redirect('detail', bird_id=bird_id)

def assoc_shirt(request, bird_id, shirt_id):
    Bird.objects.get(id=bird_id).shirts.add(shirt_id)
    return redirect('detail', bird_id=bird_id)


class BirdCreate(CreateView):
  model = Bird
  fields = ['name', 'description', 'age']
  success_url = '/birds/'

class BirdUpdate(UpdateView):
  model = Bird
  fields = ['name', 'description', 'age']

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds'

class ShirtCreate(CreateView):
    model = Shirt
    fields = ('name', 'color')

class ShirtUpdate(UpdateView):
    model = Shirt
    fields = ('name', 'color')

class ShirtDelete(DeleteView):
    model = Shirt
    success_url = '/shirts/'

class ShirtDetail(DetailView):
    model = Shirt
    template_name = 'shirts/detail.html'

class ShirtList(ListView):
    model = Shirt
    template_name = 'shirts/index.html'
