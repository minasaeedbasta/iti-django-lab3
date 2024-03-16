from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from books.models import Book
from books.forms import BookModelForm

def home(request):
    return render(request,'books/home.html')


def index(request):
    books = Book.objects.all()
    return render(request,'books/index.html',context={"books":books})

def show(request,id):
    book = Book.objects.get(id=id)
    return render(request, 'books/show.html', context= {"book":book})

# def create(request):
#     if request.method == 'POST':
#         book = Book()
#         book.name = request.POST["name"] 
#         book.author = request.POST["author"] 
#         book.price = request.POST["price"] 
#         book.no_of_pages = request.POST["no_of_pages"] 
#         book.image = request.FILES['image']
#         book.save()
#         url = reverse("books/books.index")
#         return redirect(url)
#     return render(request, 'books/create.html')

# def edit(request,id):
#     book = Book.objects.get(id=id)
#     if request.method == 'POST':
#         book.name = request.POST["name"] 
#         book.author = request.POST["author"] 
#         book.price = request.POST["price"] 
#         book.no_of_pages = request.POST["no_of_pages"]
#         if request.FILES:
#             book.image = request.FILES['image']
#         book.save()
#         url = reverse("books.index")
#         return redirect(url)
#     return render(request, 'books/edit.html', context= {"book":book})

@login_required(login_url='/users/login')
def delete(request,id):
    book = Book.objects.get(id=id)
    if book.delete():
        url = reverse("books.index")
        return redirect(url)
    
@login_required(login_url='/users/login')
def create(request):
    form = BookModelForm()
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save() 
            return redirect(book.show_url)
        
    return render(request, 'books/forms/create.html',context={"form":form})

@login_required(login_url='/users/login')
def edit(request, id):
    book = Book.get_book_by_id(id)
    form = BookModelForm(instance=book)
    if request.method == 'POST':
        form = BookModelForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect(book.show_url)

    return render(request, 'books/forms/edit.html',context={"form":form})