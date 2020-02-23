#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PaperModel
from .serializers import PaperSerializer

@api_view()
def paper_list(request):
    data = PaperModel.objects.all()
    data_serializers = PaperSerializer(data, many=True)
    return Response(data_serializers.data)

