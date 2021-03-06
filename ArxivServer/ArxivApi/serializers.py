#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from rest_framework import serializers
from .models import PaperModel


class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaperModel
        fields = ['id', 'pid', 'title', 'published', 'updated', 'summary',
                  'author', 'authors', 'cate', 'tags', 'link', 'pdf', 'version',
                  'favorite', 'pv', 'pv_total_times']