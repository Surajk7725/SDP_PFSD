from django.contrib import admin
from .models import Car,Order,Contact,Bike,OrderBike,Bus,OrderBus

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Bike)
admin.site.register(OrderBike)
admin.site.register(Bus)
admin.site.register(OrderBus)

