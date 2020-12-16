from django.db import models
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField
MY_CHOICES = (('java', 'java'),
              ('c++', 'c++'),
              ('python', 'python'),
              ('c#', 'c#'),
              ('php', 'php'),
              )



class Book(models.Model):
    name  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100, default="")
    skillset = MultiSelectField(choices=MY_CHOICES, default="")
    skill_1 = models.CharField(max_length=50, default="")
    skill_2 = models.CharField(max_length=50, default="")
    skill_3 = models.CharField(max_length=50, default="")
    skill_4 = models.CharField(max_length=50, default="")
    skill_5 = models.CharField(max_length=50, default="")
    phone_no = PhoneNumberField(null=False, blank=False, unique=True)
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
