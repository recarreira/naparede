from django.db import models

class Painting(models.Model):
    title           = models.CharField('Title', max_length=200, null=False, default="title")
    description     = models.TextField('Description', null=False, default="description")

    def __unicode__(self):
        return self.title

class Image(models.Model):
    painting = models.ForeignKey(Painting, related_name='image_painting')
    image = models.ImageField(upload_to='../media/')