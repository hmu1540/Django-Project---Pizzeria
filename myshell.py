import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizzas.models import Pizza, Topping

pizzas = Pizza.objects.all()
# print(pizzas)

for pizza in pizzas:
    print(pizza.id, pizza.name)

pizza = Pizza.objects.get(id=1)
# print(pizza)

toppings = pizza.topping_set.all()
for topping in toppings:
    print(topping)
