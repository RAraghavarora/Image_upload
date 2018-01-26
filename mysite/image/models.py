# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.http import HttpResponseRedirect
from PIL import Image
# Create your models here.
class Upload(models.Model):
	name=models.CharField(max_length=50,help_text='hello?????')
	picture = models.ImageField(upload_to='media/',help_text='Please upload an image')
	def save(self, *args, **kwargs):
		#print "THIS IS PRINT"

		super(Upload, self).save(*args, **kwargs)

#class Meta:
#	db_table= "upload"
