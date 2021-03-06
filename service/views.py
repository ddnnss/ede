from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from service.models import *
from callback.forms import *
from order.forms import *
from comments.models import *
from blog.models import *
from customuser.forms import UpdateForm
from order.models import Order
from subdomain.models import *
import random
import settings


def index(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    allComments = Comment.objects.all()
    print('request.subdomain', request.subdomain)
    subdomain = request.subdomain
    homeactive = 'active'

    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.indexTitle.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
        pageDescription = seotag.indexDescription.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
        pageKeywords = seotag.indexKeywords.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'

    try:
        seoText = HomePageText.objects.get(domain=subdomain).fullText.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    except:
        seotag = SeoTag.objects.first()
        seoText = seotag.homeDefaultText.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)

    return render(request, 'pages/index.html', locals())

def robots(request):
    subdomain = request.subdomain
    if subdomain and not request.homedomain:
        robotsTxt = f"User-agent: *\nDisallow: /admin/\nUser-Agent: Googlebot\nDisallow: /\nHost: {settings.PROTOCOL}{subdomain.name}.{settings.MAIN_DOMAIN}.ru/\nSitemap:{settings.PROTOCOL}{subdomain.name}.{settings.MAIN_DOMAIN}.ru/sitemap.xml"
    else:
        robotsTxt = f"User-agent: *\nDisallow: /admin/\nHost: {settings.PROTOCOL}{settings.MAIN_DOMAIN}.ru/\nSitemap: {settings.PROTOCOL}{settings.MAIN_DOMAIN}.ru/sitemap.xml"

    return HttpResponse(robotsTxt, content_type="text/plain")

def services(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    allService = ServiceName.objects.all()
    subdomain = request.subdomain
    priceactive = 'active'
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.servicesTitle.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
        pageDescription = seotag.servicesDescription.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                            subdomain.townAlias)
        pageKeywords = seotag.servicesKeywords.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                      subdomain.townAlias)
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'

    return render(request, 'pages/services.html', locals())

def service(request,name_slug):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    priceactive = 'active'
    currenService = get_object_or_404(ServiceName, name_slug=name_slug)
    allSubService = SubServiceName.objects.filter(service=currenService)
    faqTitle = currenService.faqTitle
    featuresTitle = currenService.featuresTitle
    compareTitle = currenService.compareTitle
    allFaq = ServiceFaq.objects.filter(service=currenService)
    allFeature = ServiceFeature.objects.filter(service=currenService)
    allService = ServiceName.objects.all()
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    subdomain = request.subdomain
    allComments = Comment.objects.filter(service=currenService)
    pageH1 = currenService.tagH1.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%',subdomain.townAlias)
    pageTitle = currenService.title.replace('%TOWN%',subdomain.town).replace('%TOWN_ALIAS%',subdomain.townAlias)
    pageDescription = currenService.description.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    pageKeywords = currenService.keywords.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    text = None
    try:
        seotag = SeoTag.objects.first()
    except:
        pass

    try:
        text = ServicePageText.objects.get(domain=subdomain,service=currenService)
    except:
        pass

    if text:
         seoText = text.fullText.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    else:
         seoText = currenService.defaultText.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                       subdomain.townAlias)

    return render(request, 'pages/service.html', locals())

def subservice(request,name_slug,subservice):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    priceactive = 'active'
    currenService = get_object_or_404(SubServiceName, name_slug=subservice)
    faqTitle = currenService.faqTitle
    featuresTitle = currenService.featuresTitle
    compareTitle = currenService.compareTitle
    allFaq = ServiceFaq.objects.filter(subService=currenService)
    allFeature = ServiceFeature.objects.filter(subService=currenService)
    allService = ServiceName.objects.all()
    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    subdomain = request.subdomain
    allComments = Comment.objects.filter(service=currenService.service)
    pageH1 = currenService.tagH1.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    pageTitle = currenService.title.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    pageDescription = currenService.description.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                          subdomain.townAlias)
    pageKeywords = currenService.keywords.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    text = None
    try:
        seotag = SeoTag.objects.first()
    except:
        pass

    try:
        text = ServicePageText.objects.get(domain=subdomain, service=currenService.service)
    except:
        pass

    if text:
        seoText = text.fullText.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
    else:
        seoText = currenService.defaultText.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                      subdomain.townAlias)

    return render(request, 'pages/subservice.html', locals())

def contacts(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    contactactive = 'active'

    subdomain = request.subdomain
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.contactTitle.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
        pageDescription = seotag.contactDescription.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                               subdomain.townAlias)
        pageKeywords = seotag.contactKeywords.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                         subdomain.townAlias)
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'

    callbackForm = CallbackForm()
    callbackOrderForm = CallbackOrderForm()
    return render(request, 'pages/contacts.html', locals())

def policy(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    return render(request, 'pages/policy.html', locals())

def allPosts(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    postsactive = 'active'
    allPost = BlogPost.objects.filter(is_active=True)
    subdomain = request.subdomain
    try:
        seotag = SeoTag.objects.first()
        pageTitle = seotag.postsTitle.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%', subdomain.townAlias)
        pageDescription = seotag.postsDescription.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                              subdomain.townAlias)
        pageKeywords = seotag.postsKeywords.replace('%TOWN%', subdomain.town).replace('%TOWN_ALIAS%',
                                                                                        subdomain.townAlias)
    except:
        pageTitle = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageDescription = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
        pageKeywords = 'НЕ ЗАПОЛНЕНА ТАБЛИЦА СЕО ТЕГИ'
    return render(request, 'pages/posts.html', locals())

def showPost(request,slug):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)
    postsactive = 'active'
    post = get_object_or_404(BlogPost, name_slug=slug)
    pageTitle = post.page_title
    pageDescription = post.page_description
    pageKeywords = post.page_keywords
    return render(request, 'pages/post.html', locals())

def lk(request):
    n1 = random.randint(0, 9)
    n2 = random.randint(0, 9)

    subdomain = request.subdomain
    if not request.homedomain:
        returnUrl = settings.PROTOCOL + subdomain.name + '.' + settings.RETURN_URL
    else:
        returnUrl = settings.PROTOCOL + settings.RETURN_URL

    print('returnUrl', returnUrl)
    if request.user.is_authenticated:
        totalFullPrice = 0
        totalActiveOrders = 0
        messageForm = MessageForm()
        orderForm = OrderForm()
        userForm = UpdateForm()
        allOrders = Order.objects.filter(user=request.user)
        for order in allOrders:
            totalFullPrice += order.fullPrice
            if order.complete and not order.is_fullPayed:
                totalActiveOrders += 1
        allService = ServiceName.objects.all()
        return render(request, 'pages/lk.html', locals())
    else:
        return render(request, 'pages/index.html', locals())




