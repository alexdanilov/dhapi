from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)

    opens_at = models.TimeField(default='08:00:00')
    closes_at = models.TimeField(default='23:59:59')

    def __str__(self):
        return self.name
