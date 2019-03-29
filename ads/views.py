from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .serializers import ProductsSerializer
# Create your views here.
from ads.forms import newform, commentsForm, favoritesForm
from ads.models import Products, Comments, Favorites


def home(request):
    u = request.user
    return render(request,'index.html')
def CategorySearch(request):
    if request.method == 'GET':
        x = request.GET.get('re')
        s = Products.objects.filter(categories=x)
    else:
        x = 'None'
        s = 'None'
    return render(request,'catsearch.html',{'x':x,'s':s})
def productsview(request):
    products = Products.objects.all()
    context = {'p':products}
    return render(request,'products.html',context)
def oneproduct(request,id):
    product = get_object_or_404(Products,id=id)
    comments = Comments.objects.filter(product = product)
    favorites_check = Favorites.objects.filter(user__username=request.user,product=product)
    if request.method == 'POST':
        comment_form = commentsForm(request.POST or None)
        favorites_form = favoritesForm(request.POST or None)
        if comment_form.is_valid():
            comment = request.POST.get('comment')
            comment = Comments.objects.create(product=product,user=request.user,comment=comment)
            comment.save()
        if favorites_form.is_valid():
            favorites = Favorites.objects.create(user=request.user,product = product)
            favorites.save()
    else:
        comment_form = commentsForm()
        favorites_form = favoritesForm()
    context = {'p':product,
               'comments':comments,
               'comment_form': comment_form,
               'favorites_form' : favorites_form,
               'favorites_check' : favorites_check,
               }
    return render(request,'product.html',context)

def favorites(request):
    favorites = Favorites.objects.filter(user__username=request.user)
    context = {'favorites':favorites}
    return render(request,'favorites.html',context)

def search(request):
    if request.method == 'GET':
        x = request.GET.get('cs')
        y = request.GET.get('ccs')
        s = Products.objects.filter(country=x,categories=y)
    else:
        x,y,s = 'NONE'
    context = {
        'x':x,
        'y':y,
        's':s
    }
    return render(request,'search.html',context)
def user_products(request):
    u = request.user
    user_products = Products.objects.filter(user=u)
    context = {
        'user_products':user_products,
        'u':u
    }
    return render(request,'my_ads.html',context)
def redirectaccounthome(request):
    u = request.user
    uu = '/accounts/'+str(u)
    return redirect(uu)
def contact(request):
    return render(request,'contact.html')
def add_product(request):
    form = newform()
    if request.method == 'POST':
        form = newform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('Done')
        return redirect('/')

    else:
        print('Not POST')
    context = {'form':form}
    return render(request,'add.html',context)

#API
class ProductsView(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer