from django.conf.urls.defaults import patterns, include, url
from ModelForm.books.views import AuthorView

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',AuthorView)
    # Examples:
    # url(r'^$', 'ModelForm.views.home', name='home'),
    # url(r'^ModelForm/', include('ModelForm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)