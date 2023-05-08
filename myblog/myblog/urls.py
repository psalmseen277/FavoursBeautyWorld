"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from products import views
from products.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home, name='home'),
    path('footer',footer, name='footer'),
    path('services',services, name='services'),
    path('seemessages',seemessages, name='seemessages'),
    path("seecontent/<slug:slug>/<str:time>/",seecontent, name='seecontent'),
    path('About',About, name='About' ),
    path('Contact',Contact, name='Contact'),
    path('upload/',upload, name='upload'),
    path('visitorupload/',visitorupload, name='visitorupload'),
    path('admin_page',admin_page, name='admin_page'),
    path('seeupload',seeupload, name='seeupload'),
    path('seeselectedupload',seeselectedupload, name='seeselectedupload'),
    path('piercing',piercing, name='piercing'),
    path('seemassage',seemassage, name='seemassage'),
    path('hairtreatment',hairtreatment, name='hairtreatment'),
    path('nailtreatment',nailtreatment, name='nailtreatment'),
    path('hairtreatment',hairtreatment, name='hairtreatment'),
    path('seeskincare',seeskincare, name='seeskincare'),
    path('servicelandpage',servicelandpage, name='servicelandpage'),
    path('delete/<services>/', views.delete_upload, name='delete'),
    path('index/',index, name='index'),
    path('<int:id>',detail,name='detail'),


    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404=""

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)