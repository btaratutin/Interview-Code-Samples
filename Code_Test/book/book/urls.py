from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from book_app.views import *

urlpatterns = patterns('',
	url (r'^$', book_index),
	url(r'^book/$', book_index),			# List of all the Books
	url(r'^book/(\d+)$', get_book),			# Book Stats
	url(r'^book/(\d+)/page/(\d+)$', get_page),	# Reading View
    # Examples:
    # url(r'^$', 'book.views.home', name='home'),
    # url(r'^book/', include('book.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
