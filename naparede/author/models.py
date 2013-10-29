from django.db import models

class Author(models.Model):
    name = models.CharField('Name', max_length=200, null=False, default="name")
    about = models.TextField('About', null=False, default="about")
    email = models.EmailField('Email',  max_length=100, null=True)

    def __unicode__(self):
        return self.name

class Link(models.Model):
    author = models.ForeignKey(Author, related_name='link_author')
    name = models.CharField('Name', max_length=200, null=True)
    url = models.CharField('Url', max_length=200, null=True)