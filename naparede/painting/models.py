from django.db import models
from author.models import Author

class Galery(models.Model):
    name = models.CharField('Name', max_length=200, null=False)
    
    def __unicode__(self):
        return self.name

class Painting(models.Model):
    author = models.ForeignKey(Author, related_name='painting_author')
    title = models.CharField('Title', max_length=200)
    description = models.TextField('Description')
    height = models.IntegerField('Height(cm)', null=True, blank=True)
    width = models.IntegerField('Width(cm)', null=True, blank=True)
    technique = models.CharField('Painting technique', max_length=200, null=True, blank=True)
    for_sale = models.BooleanField('For sale')
    price = models.DecimalField('Price', max_digits=8, decimal_places=2, null=True, blank=True)
    discount = models.DecimalField('Discount', max_digits=8, decimal_places=2, null=True, blank=True)
    galery = models.ManyToManyField(Galery)

    def __unicode__(self):
        return self.title

class Image(models.Model):
    painting = models.ForeignKey(Painting, related_name='image_painting')
    image = models.ImageField(upload_to='../media/')