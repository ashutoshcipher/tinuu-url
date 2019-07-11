

# urlpatterns = patterns('shortenersite.views',
#                        url(r'^$', 'index', name='home'),
#                        # for our home/index page
#
#                        url(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),
#                        # when short URL is requested it redirects to original URL
#
#                        url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
#                        # this will create a URL's short id and return the short URL
#                        )


from django.urls import path

from .views import GetShortenUrl, get_real_url

urlpatterns = [
    path('api/create/', GetShortenUrl.as_view(), name='shorten url'),
    path('s/<str:short_url>/', get_real_url, name='real_url')
]