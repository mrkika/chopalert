from django.db import models


class FoodSpot(models.Model):
    FOOD_CHOICES = [
        ('suya', 'Suya'),
        ('akara', 'Akara'),
        ('puffpuff', 'Puff Puff'),
        ('noodles', 'Noodles'),
        ('shawarma', 'Shawarma'),
        ('others', 'Others'),
    ]

    food_type = models.CharField(max_length=20, choices=FOOD_CHOICES)
    description = models.TextField(blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    posted_at = models.DateTimeField(auto_now_add=True)
    available_until = models.DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to='food_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.get_food_type_display()} at ({self.latitude:.3f}, {self.longitude:.3f})"
