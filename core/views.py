from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model

User = get_user_model()

class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view();