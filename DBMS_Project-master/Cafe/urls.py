"""Delicious URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Cafe import views as del_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login_user/$', del_views.login_user),
    url(r'^login_restaurant/$', del_views.login_restaurant),
    url(r'^authenticate_user/$', del_views.authenticate_user),
    url(r'^authenticate_res/$', del_views.authenticate_res),
    url(r'^home/$', del_views.home),
    url(r'^rest_home/$', del_views.rest_home),
    url(r'^cus_reg/$', del_views.customer_register),
    url(r'^res_reg/$', del_views.restaurant_register),
    url(r'^get/(?P<rest_id>\d+)/$',del_views.rest_display),
    url(r'^query/(?P<check_id>\d+)/$', del_views.query),
    url(r'^additem/$', del_views.additem),
    url(r'^deleteitem/$', del_views.deleteitem),
    url(r'^setstatus/$', del_views.setstatus),
    url(r'^cart/$', del_views.cart),
    url(r'^place_order/$', del_views.place_order),
    url(r'^checkout/$', del_views.checkout),
    # url(r'^showorders/$', del_views.showstatus),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
