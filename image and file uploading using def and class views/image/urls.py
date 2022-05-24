
from django.urls import path
from image import views
from django.conf import settings
from django.conf.urls.static import static

#using class based view
from .views import BookListView,UploadBookView
urlpatterns=[
    path('books/',views.book_list,name='book_list'),
    path('books/upload/',views.upload_book,name='upload_book'),
    path('upload/',views.upload,name='upload'),
    path('',views.Home.as_view(),name='home'),
    #using class based view
    path('class/books/',BookListView.as_view(),name='class_book_list'),
    path('class/books/upload/',UploadBookView.as_view(),name='class_upload_book'),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
