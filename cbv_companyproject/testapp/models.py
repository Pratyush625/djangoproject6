from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    ceo=models.CharField(max_length=70)

    #After inserting data it will show the target page (details page) so we are here using reverse url
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
