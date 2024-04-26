from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum

    
def car_invetory_update():
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value=Sum('value') 
    )['total_value'] #retorna somente o valor sem o dicionário 
    # ex: {'total_value': 100.000}
    
    CarInventory.objects.create(
        cars_count= cars_count,
        cars_value=cars_value
    )

@receiver(pre_save, sender=Car)
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Bio gerada automaticamente'
    

@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_invetory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
   car_invetory_update()
    