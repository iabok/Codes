from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.views import RecipeCreateView, RecipeListView
from pricecaculator.views import PriceCreateView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/', RecipeCreateView.as_view(), name="Create"),
    url(r'^price/', PriceCreateView.as_view(), name="Create"),
    url(r'^view/', RecipeListView.as_view(), name="View_list"),
)
