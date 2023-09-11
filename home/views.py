from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    views = {}
    views['services'] = Services.objects.all()
    views['feedbacks'] = Feedback.objects.all()
    return render(request,'index.html',views)

def about(request):
    return render(request,'about.html')

def contact(request):
    views = {}
    views['contact_info'] = SiteInfo.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        data = Contact.objects.create(
            name = name,
            email = email,
            subject = subject,
            message = message
        )
        data.save()
        views['success_messages'] = "The form is submitted"
        return render(request, 'contact.html', views)
    return render(request,'contact.html',views)

def portfolio(request):

    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    views = {}
    views['services'] = Services.objects.all()
    return render(request,'services.html',views)