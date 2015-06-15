from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "getWash.views.home", name="home"),
    url(r'^signIn/$', "getWash.views.signIn", name="signIn"),
    url(r'^shopping/$', "getWash.views.shopping", name="shopping"),
    url(r'^unitPrice/$', "getWash.views.unitPrice", name="unitPrice"),
    url(r'^coverArea/$', "getWash.views.coverArea", name="coverArea"),
    url(r'^about/$', "getWash.views.about", name="about"),
    url(r'^signUp/$', "getWash.views.signUp", name="signUp"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
