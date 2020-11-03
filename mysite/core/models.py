from django.db import models


class Book(models.Model):
    name  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject  = models.CharField(max_length=100, default="")
    coverletter = models.CharField(max_length=100, default="")
    pdf = models.FileField(upload_to='books/pdfs/')
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
