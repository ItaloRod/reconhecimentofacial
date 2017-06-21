from django.shortcuts import render
from .forms import UploadImageForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    data={}
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("Deucerto")
    else:
        form = UploadImageForm()
    data['form'] = form
    return render(request, 'views/principal.html',data)
