from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, "home/about.html")

def contact_us_view(request):
    contact_info = {
        'restaurant_name':'family-e-dine',
        'address':'123 street, abc',
        'phone':'+91-9999999990',
        'email':'abc@gmail.com',
        'hours':'9am-11pm :Sunday off'
    }
    return render(request,'home/contact.html',{'contact_info':contact_info})