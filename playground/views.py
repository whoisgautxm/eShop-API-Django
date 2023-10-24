from django.shortcuts import render

from . tasks import notify_customer
def say_hello(request):
    
    notify_customer.delay("hello")
    return render(request, 'hello.html', {'name': 'Gautam'})
