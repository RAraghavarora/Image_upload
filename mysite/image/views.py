# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import ProfileForm
from django.http import HttpResponseRedirect
from image.models import Upload
from image.forms import ProfileForm,NewForm
from PIL import Image
#def index(request):

def upload_file(request):
	saved = False
	if request.method == "GET":
		context = {'form': ProfileForm}
		return render(request, 'image/profile.html', context)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])
			upload=Upload()
			upload.name=form.cleaned_data["name"]
			upload.picture = form.cleaned_data["picture"]
			im = Image.open(upload.picture)
			#im.show()	
			im = im.resize((250,250))
			im.save("image/static/saved.jpg","JPEG")
			upload.save()

			#form.save()
			saved = True	
			return render(request, 'image/upload.html',{'form':ProfileForm,'saved':saved})
			#return HttpResponseRedirect('image/upload.html')
		else:
			form = ProfileForm()
			saved = False
			return render(request, 'image/profile.html',{'form':NewForm})
	#return render(request, 'image/upload.html', {'form':form})