from django.shortcuts import redirect, render

from pizzas.forms import PizzaForm
from .models import Pizza, Topping

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id = pizza_id)
    toppings = pizza.topping_set.all()
    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context)

def comment(request, pizza_id):
    if request != 'POST':
        form = PizzaForm()
    else:
        form = PizzaForm(data = request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('pizzas:pizzas')
            