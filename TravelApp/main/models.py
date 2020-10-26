from django.db import models

class Travel(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    # image = models.ImageField()

    def __str__(self):
        return self.title

class Step(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    date = models.DateField()
    summary = models.TextField()

    def __str__(self):
        return self.city