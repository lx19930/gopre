

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SlideForm
from .models import Slide

def upload_slide(request):
    if request.method == 'POST':
        form = SlideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slide_list')
    else:
        form = SlideForm()
    return render(request, 'slides/upload_slide.html', {'form': form})

def slide_list(request):
    slides = Slide.objects.all()
    return render(request, 'slides/slide_list.html', {'slides': slides})
