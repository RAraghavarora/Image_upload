from . import views
from django.conf.urls import url
from django.views.generic import TemplateView

app_name='image'
urlpatterns = [
	url(r'^$',views.upload_file, name='upload_file'),
	#url(r'^profile/$',views.upload_file, name='upload_file')
	]