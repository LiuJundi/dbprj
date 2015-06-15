from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "getWash.views.home", name="home"),
    url(r'^account/signUp/$', "getWash.views.signUp", name="signUp"),
    url(r'^shopping/$', "getWash.views.shopping", name="shopping"),
    url(r'^unitPrice/$', "getWash.views.unitPrice", name="unitPrice"),
    url(r'^coverArea/$', "getWash.views.coverArea", name="coverArea"),
    url(r'^about/$', "getWash.views.about", name="about"),
    url(r'^makeOrder/$', "getWash.views.makeOrder", name="makeOrder"),

    url(r'^manage/orders/$', "getWash.views.orders", name="orders"),
    url(r'^manage/getOrders', "getWash.views.getOrders", name="getOrders"),
    #url(r'^manage/finishedOrders/$', "getWash.views.finishedOrders", name="finishedOrders"),
    #url(r'^manage/(?P<school>[a-zA-Z ]+)/(?<building>[a-zA-Z 0-9]+)/$', )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
