from django.db import models


class District(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Subcounty(models.Model):
    name=models.CharField(max_length=200)
    district = models.ForeignKey('District', on_delete=models.CASCADE,  # related_name='district', 
    null=True)
    def __str__(self):
        return self.name

class Parish(models.Model):
    name=models.CharField(max_length=200)
    sub_county = models.ForeignKey('Subcounty', on_delete=models.CASCADE, #related_name='sub_county',
     null=True)
    def __str__(self):
        return self.name

class Officer(models.Model):
    name = models.CharField(max_length=30)
    Telephone = models.CharField(max_length=30)
    parish = models.ForeignKey('Subcounty', on_delete=models.CASCADE, #related_name='parish'
     null=True)
    def __str__(self):
        return self.name
    
class Farmer(models.Model):
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'male'),
        
    )
    MARRIAGE_STATUS= (
        ('Married', 'Married'),
        ('Single', 'Single'),
        
    )
    Marriage_status =models.CharField(max_length=30, choices=MARRIAGE_STATUS)
    name = models.CharField(max_length=30)
    Age = models.IntegerField
    Telephone = models.IntegerField
    image= models.ImageField(upload_to = '../Media/', default='./static/images/no_img.jpg')
    Gender=models.CharField(max_length=20, choices=GENDER)
    officer = models.ForeignKey('Officer', on_delete=models.CASCADE, related_name='officer', null=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    latitude=models.CharField