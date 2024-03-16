from django.shortcuts import render, redirect, reverse
from authors.models import Author
from authors.forms import AuthorModelForm
from django.contrib.auth.decorators import login_required

def index(request):
    # return HttpResponse("test")
    authors = Author.objects.all()
    return render(request,'authors/index.html',context={"authors":authors})

def show(request,id):
    author = Author.objects.prefetch_related('books').get(id=id)
    print(author.__dict__)
    # author = Author.objects.get(id=id)
    return render(request, 'authors/show.html', context= {"author":author})

# def create(request):
#     if request.method == 'POST':
#         author = Author()
#         author.name = request.POST["name"] 
#         author.bdate = request.POST["bdate"] 
#         author.image = request.FILES['image']
#         author.save()
#         url = reverse("authors/authors.index")
#         return redirect(url)
#     return render(request, 'authors/create.html')

# def edit(request,id):
#     author = Author.objects.get(id=id)
#     if request.method == 'POST':
#         author.name = request.POST["name"] 
#         author.bdate = request.POST["bdate"] 
#         if request.FILES:
#             author.image = request.FILES['image']
#         author.save()
#         url = reverse("authors.index")
#         return redirect(url)
#     return render(request, 'authors/edit.html', context= {"author":author})
@login_required(login_url='/users/login')
def delete(request,id):
    author = Author.objects.get(id=id)
    if author.delete():
        url = reverse("authors.index")
        return redirect(url)
    

@login_required(login_url='/users/login')
def create(request):
    form = AuthorModelForm()
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES)
        if form.is_valid():
            author = form.save() 
            return redirect(author.show_url)
        
    return render(request, 'authors/forms/create.html',context={"form":form})

@login_required(login_url='/users/login')
def edit(request, id):
    author = Author.get_author_by_id(id)
    form = AuthorModelForm(instance=author)
    if request.method == 'POST':
        form = AuthorModelForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect(author.show_url)

    return render(request, 'authors/forms/edit.html',context={"form":form})