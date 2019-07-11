from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.generic import View
import random
import string
from .models import URL
import dateparser
from django.conf import settings
from django.utils.decorators import method_decorator
import urllib
import re
import datetime

# Create your views here.


def get_short_url(url):
    is_not_unique = True

    while is_not_unique:
        short_url = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if not URL.objects.filter(pk=short_url).exists():
            is_not_unique = False
            return short_url

class GetShortenUrl(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetShortenUrl, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        rdata = json.loads(request.body)
        given_url = rdata.get('url', None)
        expire = rdata.get('expire', None)

        if given_url is None or expire is None:
            return JsonResponse({'message': 'INVALID PARAMS'})

        short_url = get_short_url(given_url)

        url_obj = URL.objects.create(tiny_url = short_url, original_url = given_url, expired_at=expire)
        url_obj.save()

        response_url = settings.SITE_URL + "/" + short_url

        return JsonResponse({'short-url': response_url})




def formaturl(url):
    if not re.match('(?:http|ftp|https)://', url):
        return 'http://{}'.format(url)
    return url


@csrf_exempt
def get_real_url(request, short_url):
    url = short_url
    if not url:
        return JsonResponse({'message': 'INVALID PARAMS'})
    url_obj = get_object_or_404(URL, pk=url)
    print("url_obj.expired_at", url_obj.expired_at)
    if  dateparser.parse(url_obj.expired_at) >= datetime.datetime.now():
        location = url_obj.original_url
        location = formaturl(location)
        res = HttpResponse(location, status=302)
        res['Location'] = location
        return res
    else:
        raise Http404()









