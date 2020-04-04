from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Person(models.Model):
    uid = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Image(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    encoding = ArrayField(models.FloatField(blank=True, null=True), size=1000, null=True, default=0)


class Gate(models.Model):
    name = models.CharField(max_length=100)


class Log(models.Model):
    log_id = models.AutoField(primary_key=True, unique=True)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    entry_gate = models.ForeignKey(Gate, related_name='entry',on_delete=models.CASCADE)
    entry_datetime = models.DateTimeField(blank=True, null=True)
    entry_image = models.ImageField(upload_to='entry/{self.entry_gate}', null=True)
    exit_gate = models.ForeignKey(Gate,related_name='exit', on_delete=models.CASCADE, null=True)
    exit_datetime = models.DateTimeField(blank=True, null=True)

