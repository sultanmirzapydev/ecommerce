from django.db import models
import os
import random


def get_filename_ext(filepath):
	#print(filepath)
	
	
	name, ext = os.path.splitext(filepath)
	return name, ext


def upload_image_path(instance, filename):
	#print(instance)
	#print(filename)
	new_filename = random.randint(1,4000000000)
	name, ext = get_filename_ext(filename)
	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)

	return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class ProductManager(models.Manager):
	def get_by_id(self,id):
		qs = self.get_queryset().filter(id=id)
		if qs.count() == 1:
			return qs.first()
		return None



class Product(models.Model):
	title        = models.CharField(max_length=120)
	description  = models.TextField()
	price        = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
	image        = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
	objects      = ProductManager()

	def __str__(self):
		return self.title
