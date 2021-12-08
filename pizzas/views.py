from django.shortcuts import redirect, render
from pizzas.forms import CommentForm
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
    comments = pizza.comment_set.all()
    context = {'pizza': pizza, 'toppings': toppings, 'comments':comments}

    return render(request, 'pizzas/pizza.html', context)

def comment(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            print('form is valid')
            new_comment = form.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            form.save()
            return redirect('pizzas:pizza', pizza_id = pizza_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, 'pizzas/comment.html', context)