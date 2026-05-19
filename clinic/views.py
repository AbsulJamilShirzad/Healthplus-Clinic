from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def doctors(request):
    return render(request, 'doctors.html')


def appointment(request):
    return render(request, 'appointment.html')


def contact(request):
    return render(request, 'contact.html')
