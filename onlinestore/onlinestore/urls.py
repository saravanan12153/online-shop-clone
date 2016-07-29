"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from store.views import IndexView, RegistrationView, LoginView, AddStore, \
    ProductsView, StoreEditsView, ProductEditsView
import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^register/$', RegistrationView.as_view()),
    url(r'^login/$', LoginView.as_view()),
    # url(r'^stores/$', storespage),
    url(r'^stores/$', AddStore.as_view()),
    url(r'^stores/(?P<pk>[0-9]+)/edit/$',
        StoreEditsView.as_view(), name='edit_stores'),
    url(r'^stores/(?P<pk>[0-9]+)/products/$',
        ProductsView.as_view(), name="all_products"),
    url(r'stores/(?P<store_id>[0-9]+)/products/(?P<pk>[0-9]+)/$',
        ProductEditsView.as_view(), name="edit_product"),
    # media route
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),
]
