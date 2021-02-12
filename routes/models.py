from django.db import models


# Create your models here.
class Route(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    iframe_url = models.TextField()
    url = models.TextField()
    is_east_bay_route = models.BooleanField(default=False)
    distance = models.DecimalField(decimal_places=2, default=0.0, max_digits=5)

    def get_absolute_url(self):
        return f"/routes/{self.id}"
