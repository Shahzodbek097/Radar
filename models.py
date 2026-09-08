from django.db import models

# Create your models here.

class Radar(models.Model):
    car_number=models.CharField(max_length=10)
    car_tezlik=models.IntegerField()
    car_jarima=models.IntegerField()
    vaqt=models.CharField(max_length=20)

    class Meta:
        db_table='radar'
        managed=False
        verbose_name="Radar ma'lumot"
        verbose_name_plural="Radar ma'lumotlari"

    def __str__(self):
        return f"mashina raqami {self.car_number}"
