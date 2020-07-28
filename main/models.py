from django.db import models
from django.utils import timezone


# Create your models here.

class KitchenCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class LivingCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		

class BedRoomCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		

class OfficeCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class DinningCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		

class DoorCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		
		

class WardrobeCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title


class CenterCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.title
		

class TvCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class ClientCategory(models.Model):
	"""docstring fos Category_one"""
	title = models.CharField(max_length=60, default="none")
	image = models.ImageField(upload_to='images')
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
		
		




class ContactModel(models.Model):
	"""docstring for ContactModel"""
	name = models.CharField(max_length=60, default="none")
	email = models.CharField(max_length=60, default="none")
	phone = models.CharField(max_length=60, default="none")
	message = models.CharField(max_length=60, default="none")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name



class FactoryModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="factory image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title



class ProjectModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	title = models.CharField(max_length=60, default="Project image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title




class CategoryModel(models.Model):
	image = models.ImageField(upload_to='factory_images')
	category = models.CharField(max_length=60, default="category image")
	title = models.CharField(max_length=60, default="Project image")
	pub_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.category




