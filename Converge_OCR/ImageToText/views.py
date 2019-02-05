from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import detect_document
from django.core.files.storage import FileSystemStorage , default_storage

#home page view
def home(request):
    return HttpResponse("<h1>Middle finger</h1>")
#image upload and detection view
@csrf_exempt  
def image(request):
    #check if request is of POST type and has a file attached with it as image
    if request.method == 'POST' and request.FILES['image']:
        #dist of file object in POST request
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        path = './media/'+ filename
        detection = detect_document(path)
        default_storage.delete(path)
        return JsonResponse({'detection':detection})