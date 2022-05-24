from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from .forms import BookForm
from .models import Book

#using class based view
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
# from django.image import FileSystemStorage
# Create your views here.

class Home(TemplateView):
    template_name='home.html'

def upload(request):
    # context={}
    if request.method=='POST':
        uploaded_file=request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
        # fs=FileSystemStorage()
        # name=fs.save(uploaded_file.name,uploaded_file)
        # context['url']=fs.url(name)
    return render(request,'upload.html')


def book_list(request):
    books=Book.objects.all()
    return render(request,'book_list.html',{'booklist':books})

def upload_book(request):
    if request.method =='POST':
        form = BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'upload_book.html',{'bform':form})

# using class based view
class BookListView(ListView):
    model=Book
    template_name='class_book_list.html'
    context_object_name='booklist'

class UploadBookView(CreateView):
    model=Book
    fields=('title','author','pdf','cover')
    success_url=reverse_lazy('class_book_list')
    template_name='class_upload_book.html'
    


