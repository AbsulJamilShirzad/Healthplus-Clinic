from django.shortcuts import render
from .models import Appointment


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def contact(request):
    return render(request, 'contact.html')


def appointment(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')

        Appointment.objects.create(
            name=name,
            email=email,
            date=date
        )

    return render(request, 'appointment.html')
