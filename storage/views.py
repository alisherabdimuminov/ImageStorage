from django.shortcuts import render
import base64
from django.core.files.base import ContentFile
from .models import Storage
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(http_method_names=["POST"])
def upload_image(request):
    print(request.data)
    data = request.data.get("image")
    format, imgstr = data.split(';base64,') 
    ext = format.split('/')[-1] 
    storage = Storage()
    storage.image = ContentFile(base64.b64decode(imgstr), name='face.' + ext)
    storage.save()
    return Response({"url": storage.image.url})