from django.db import models


Status = (
	('Inservice', 'Inservice'),
	('OOS', 'OOS'),
	)


station = (
	('Station 1' , 'Station 1'),
	('Station 2' , 'Station 2'),
	('Station 3' , 'Station 3'),
	('Station 4' , 'Station 4'),
	('Fleet Matenance' , 'Fleet Matenance'),
	)
ema = (
	('EMA 1', 'EMA 1'),
	('EMA 3', 'EMA 3'),
	('EMA 4', 'EMA 4'),
	('EMA 5', 'EMA 5'),
	('N/A', 'N/A'),
	)

# Create your models here.
class unit(models.Model):
	picture = models.ImageField(null= True, blank=True, upload_to='images/unit_pics')

	unit_no = models.CharField(max_length= 200, null=True)

	Status = models.CharField(max_length=20, choices=Status, default='Inservice')

	Problem = models.CharField(max_length= 200, null=True)

	Notified = models.CharField(max_length= 200, choices=ema, default='N/A')

	Date = models.CharField(max_length=200, null=True)

	Location = models.CharField(max_length=20, choices=station, default='Station 1', null=True)

	def __str__(self):
		return str(self.id)+ ' | ' +str(self.unit_no) + ' | ' + str(self.Status) + ' | ' + str(self.Problem) + ' | ' + str(self.Notified) + ' | ' + str(self.Date) + '|' + str(self.Location)




class courses(models.Model):
	Title = models.CharField(null=True, max_length=200)

	Desription = models.CharField(null=True, max_length=200)

	Instructor = models.CharField(null=True, max_length=200)

	Location = models.CharField(null=True, max_length=200)

	Date = models.CharField(null=True, max_length=200)

	def __str__(self):
		return str(self.Title) + " | " +  str(self.Instructor) + ' | ' + str(self.Location) + ' | ' + str(self.Date)
