#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PaperModel
from .serializers import PaperSerializer

@api_view()
def paper_list(request):
    print(request.GET.get('_start'))
    print(request.GET.get('_limit'))
    # data = PaperModel.objects.all()
    data = PaperModel.objects.raw('select * from arxivapi_papermodel limit {0},{1}'.format(request.GET.get('_start'), request.GET.get('_limit')))
    data_serializers = PaperSerializer(data, many=True)
    return Response(data_serializers.data)
