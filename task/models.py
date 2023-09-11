from django.db import models


class Task_Backend(models.Model):
    image = models.ImageField(upload_to='images_Backend/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.text}'


class Task_Frontend(models.Model):
    image = models.ImageField(upload_to='images_Frontend/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.text}'