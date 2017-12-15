from django.db import models

# Create your models here.


## MODEL
class Property(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    property_name = models.CharField('Property Name',db_column='property_name', max_length=100)
    property_address = models.CharField('Address',db_column='property_address', max_length=100)

    class Meta:
        managed = True

    def __str__(self):
        return self.property_name


## MODEL
class MeterWater(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    meter_property = models.ForeignKey('Property')
    meter_date = models.DateField(db_column='meter_date', null=True, blank=True)
    meter_amount = models.IntegerField(db_column='meter_amount', default=0)

    class Meta:
    managed = True

    def __str__(self):
        return self.meter_amount