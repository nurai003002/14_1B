from django.shortcuts import render
from apps.base.models import *
from apps.secondary.models import *

# Create your views here.
def index(request):
    admin = Admin.objects.latest('id')
    footer = Footer.objects.latest('id')
    banner = Banner.objects.all().order_by("-id")[:2]
    banner_all = Banner.objects.all()
    service = Service.objects.all()  
    services = Services.objects.all()
    video = Video.objects.latest('id')

    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'base/index.html', locals())

def about_us(request):
    admin = Admin.objects.latest('id')
    footer = Footer.objects.latest('id')
    about = AboutUs.objects.latest('id')
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'about.html', locals())

def team(request):
    # setting = Settings.objects.latest('id')
    team = Team.objects.all()
    footer = Footer.objects.all()
    
    # founder = Founder.objects.latest('id')
    if request.method =="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        message = request.POST.get('message')

    return render(request, 'team.html', locals())

def post(request):
    admin = Admin.objects.latest('id')
    footer = Footer.objects.latest('id')
    banner_all = Banner.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'post.html', locals())

def news(request):
    admin = Admin.objects.latest("id")
    footer = Footer.objects.latest('id')
    news = News.objects.latest('id')
    banner_all = Banner.objects.all()
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'news.html', locals())

def gallery(request):
    admin = Admin.objects.latest('id')
    footer = Footer.objects.latest('id')
    if request.method == 'POST':
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        adults_quantity = request.POST.get("adults_quantity")
        childs_quantity = request.POST.get("childs_quantity")
        result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'gallery.html', locals())

def contact(request):
    admin = Admin.objects.all()
    footer = Footer.objects.latest('id')
    contact = Contact.objects.latest('id')
    if request.method == 'POST':
        if "contact_submit" in request.POST:
            fullname = request.POST.get("fullname")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            theme = request.POST.get("theme")
            message = request.POST.get("message")
            result = ContactPost.objects.create(fullname = fullname, email = email,phone = phone, theme = theme, message = message)
        if "footer_submit" in request.POST:
            fullname = request.POST.get("fullname")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            adults_quantity = request.POST.get("adults_quantity")
            childs_quantity = request.POST.get("childs_quantity")
            result = FooterPost.objects.create(fullname = fullname, phone = phone, date = date, adults_quantity = adults_quantity, childs_quantity = childs_quantity)
    return render(request, 'contact.html', locals())

def service(request):
    service = Service.objects.all()  
