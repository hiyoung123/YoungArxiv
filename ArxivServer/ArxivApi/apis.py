#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PaperModel
from .serializers import PaperSerializer

@api_view()
def paper_list(request):
    data = {'pid':'001','title':'test','published':'2020:12:12','updated':'2020:12:12','summary':'asad'}
            # 'author':'liu','authors':'liuhaiyang','cate':'ml','tags':'dl','link':'http://hiyoungai.com','pdf':'http://hiyoungai.com','version':'1'}
    PaperModel.objects.create(data)

    data_serializers = PaperSerializer(data, many=True)
    return Response(data_serializers.data)

