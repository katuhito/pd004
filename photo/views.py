from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    """ トップページのビュー"""
    #index.htmlをレンダリング
    template_name = 'index.html'
    

