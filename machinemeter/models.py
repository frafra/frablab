from django.db import models
from makers.models import Maker

class Machine(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    description = models.TextField(blank=True)
    price_first = models.IntegerField()
    price_after = models.IntegerField()
    quantity = models.IntegerField()
    unit = models.CharField(
        max_length=3,
        choices=(
            ('min', 'minute'),
            ('hr',  'hour'),
            ('mm',  'millimetre'),
            ('cm',  'centimetre'),
            ('m',   'metre'),
            ('g',   'gram'),
            ('kg',  'kilogram'),
            ('l',   'litre'),
        )
    )

class Usage(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    usage = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)
