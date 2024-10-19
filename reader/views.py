# reader/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import PDF

@login_required
def index(request):
    pdfs = PDF.objects.filter(user=request.user)
    return render(request, 'index.html', {'pdfs': pdfs})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def upload_pdf(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        PDF.objects.create(user=request.user, title=title, file=file)
        return redirect('index')
    return render(request, 'upload.html')