from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth import login, authenticate , logout
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView,DetailView,UpdateView, CreateView
from django.forms.models import model_to_dict
from .models import User,Book,Rate,Author,Category
from .forms import SignUpForm,SignInForm,SignUpFormmuser
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
# Create your views here.
def notifsget(request):
    books=User.objects.none()
    favs=request.user.user.favourites.all()
    for seta in favs:
        books= books | seta.book_set.filter(created_at__gt=request.user.user.notifs)
    favs=request.user.user.follows.all()
    for seta in favs:
        books= books | seta.book_set.filter(created_at__gt=request.user.user.notifs)
    books=books.distinct().order_by('-created_at')
    return books
def index(request):
    return  HttpResponse("Hello, world. You're at the polls index.")
def test(request):
    logout(request);
    return  HttpResponse(str(request.user.is_authenticated()))
def home(request):
    print(request.user)
    return  HttpResponse("Hello, world. You're at the home index."+str(request.user.is_authenticated())+str(request.user.id))
def realhome(request):
    
     return render(request,'bookapi/home.html',{'notlen':len(notifsget(request)),"islogged":request.user.is_authenticated()})
def signin(request):
    if request.method == 'POST':
         
        form = SignInForm(request.POST)
       
        
        if True:
            print(form['password'])
            print(form.data.get('username'))
            username = form.data.get('username')
            raw_password = form.data.get('password')
            
            user = authenticate(username=username, password=raw_password)
            
            print(user);

            login(request, user)
            print(request.user.is_authenticated())
            return  HttpResponseRedirect("home")
    else:
        form = SignInForm()
    return render(request, 'bookapi/user_sign_in.html', {'form': form})
def signup(request):
    if request.method == 'POST':
         
        form = SignUpForm(request.POST)
        otform=SignUpFormmuser(request.POST,request.FILES)
        print(form.is_valid())
        print(form.errors)
        print(form.cleaned_data.get('password'))
        print (otform.is_valid())
        print(otform.errors)
        if form.is_valid() and otform.is_valid():
            user=form.save()
            profile=otform.save(commit=False)
            profile.user=user
            
            profile.save();
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            
            print(user);

            login(request, user)
            print(request.user.is_authenticated())
            return  HttpResponseRedirect("home")
    else:
        form = SignUpForm()
        otform = SignUpFormmuser()
    return render(request, 'bookapi/user_sign_up.html', {'form': form,"otherform":otform})
class AddUserView(CreateView):
    model= User
    fields = ['Username','email','image','password','password']
    success_url = '/api/'
def books(request):
    books = Book.objects.all().order_by('-created_at')
    print(books)
    return render(request,'bookapi/books_listing.html',context={"books":books,"id":request.user.id,'notlen':len(notifsget(request))})
def bauthors(request,author_id):
    author = get_object_or_404(Author,pk=author_id)
    books=author.book_set.all().order_by('-created_at')
    print(books)
    return render(request,'bookapi/books_listing.html',context={"books":books,"id":request.user.id,'notlen':len(notifsget(request))})
def bcategs(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    books=category.book_set.all().order_by('-created_at')
    print(books)
    return render(request,'bookapi/books_listing.html',context={"books":books,"id":request.user.id,'notlen':len(notifsget(request))})

def favlist(request):
    books=User.objects.none()
    favs=request.user.user.favourites.all()
    for seta in favs:
        books= books | seta.book_set.all()
    favs=request.user.user.follows.all()
    for seta in favs:
        books= books | seta.book_set.all()
    books=books.distinct().order_by('-created_at')
    print(books)
    return render(request,'bookapi/books_listing.html',context={"books":books[:10],"id":request.user.id,'notlen':len(notifsget(request))})

def notlist(request):
    notifications=notifsget(request);
    print(request.user.user.notifs)
    request.user.user.notifs= timezone.now()
    print(request.user.user.notifs)
    request.user.user.save()
    return render(request,'bookapi/notification_listing.html',context={"notifications":notifications,"id":request.user.id,'notlen':0})

    
def servicebooks(request):
    authme=[]
    auth = Book.objects.all()
    for a in auth:
        authme.append(model_to_dict(a))
    return JsonResponse("HELLO",safe=False)
def likebook(request,book_id):
    print(request.user)
    book=get_object_or_404(Book,pk=book_id)
    if(len(request.user.user.likes.filter(pk=book_id))==0):
        request.user.user.likes.add(book)
    else:
        request.user.user.likes.remove(book)
    
    return JsonResponse({"sucess":True},safe=False)
def readbook(request,book_id):
    print(request.user)
    book=get_object_or_404(Book,pk=book_id)
    if(len(request.user.user.read.filter(pk=book_id))==0):
        request.user.user.read.add(book)
    else:
        request.user.user.read.remove(book)
    
    return JsonResponse({"sucess":True},safe=False)
def wishesbook(request,book_id):
    print(request.user)
    book=get_object_or_404(Book,pk=book_id)
    if(len(request.user.user.wishes.filter(pk=book_id))==0):
        request.user.user.wishes.add(book)
    else:
        request.user.user.wishes.remove(book)
    
    return JsonResponse({"sucess":True},safe=False)
@csrf_exempt
def ratesbook(request,book_id):
    print(request.user)
    Rate.objects.create(user_id=request.user.user.id,book_id=book_id,rate=request.POST['rate'])
    return JsonResponse({"sucess":True},safe=False)
def authors(request):
    authors = Author.objects.all()
    return render(request,'bookapi/authors_listing.html',context={"authors":authors,"id":request.user.id,'notlen':len(notifsget(request))})

def categories(request):
    categories = Category.objects.all()
    return render(request,'bookapi/categories_listing.html',context={"categories":categories,"id":request.user.id,'notlen':len(notifsget(request))})


def followauthor(request,author_id):
    print(request.user)
    author=get_object_or_404(Author,pk=author_id)
    if(len(request.user.user.follows.filter(pk=author_id))==0):
        request.user.user.follows.add(author)
    else:
        request.user.user.follows.remove(author)
    
    return JsonResponse({"sucess":True},safe=False)

def favouritecategory(request,category_id):
    print(request.user)
    category=get_object_or_404(Category,pk=category_id)
    if(len(request.user.user.favourites.filter(pk=category_id))==0):
        request.user.user.favourites.add(category)
    else:
        request.user.user.favourites.remove(category)
    
    return JsonResponse({"sucess":True},safe=False)