from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user = models.ForeignKey(User)
    text = models.CharField(max_length=400)
    date = models.DateTimeField()
    email = models.EmailField()
    url = models.URLField()
    
    def __unicode__(self):
        return "%s" % self.email
        
    class Meta:
        ordering = ['date']
