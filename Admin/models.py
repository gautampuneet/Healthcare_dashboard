from django.db import models

class Doctors(models.Model):
	Name = models.CharField(max_length=100)
	Department = models.CharField(max_length=50)
	Photo = models.FileField(upload_to = 'upload' )
	Employee_id = models.BigIntegerField()
	joining_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.Name