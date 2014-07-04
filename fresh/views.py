# Create your views here.
from rest_framework import viewsets
from fresh import models
from fresh import serializers

import django_rq
import requests


class FreshViewSet(viewsets.ModelViewSet):
    model = models.Fresh
    serializer = serializers.FreshSerializer

    def create(self, request, *args, **kwargs):
        queue = django_rq.get_queue('default')
        # queue.enqueue(FreshViewSet.fetch_url)
        queue.enqueue(goto_baidu)
        return super(FreshViewSet, self).create(request, args, kwargs)

    @staticmethod
    def fetch_url():
        print 'Fetch in Queue'
        requests.get('http://www.baidu.com')


def goto_baidu():
    print 'Goto baidu'
    requests.get('http://www.baidu.com')