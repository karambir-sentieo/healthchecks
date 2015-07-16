from django.conf.urls import url

from hc.front import views

urlpatterns = [
    url(r'^$',                      views.index,  name="hc-index"),
    url(r'^checks/add/$',           views.add_check, name="hc-add-check"),
    url(r'^checks/([\w-]+)/name/$', views.update_name, name="hc-update-name"),
    url(r'^checks/([\w-]+)/timeout/$', views.update_timeout, name="hc-update-timeout"),
    url(r'^checks/([\w-]+)/email/$', views.email_preview),
    url(r'^checks/([\w-]+)/remove/$', views.remove, name="hc-remove-check"),
    url(r'^pricing/$',              views.pricing, name="hc-pricing"),
    url(r'^docs/$',                 views.docs, name="hc-docs"),
    url(r'^about/$',                views.about, name="hc-about"),
]