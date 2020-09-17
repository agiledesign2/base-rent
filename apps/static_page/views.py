from django.urls import reverse
from django.shortcuts import render
from meta.views import MetadataMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

"""
use_og
use_twitter
use_facebook
use_googleplus
use_title_tag
title
og_title
twitter_title
gplus_title
description
keywords
url
image
image_width
image_height
object_type
site_name
twitter_site
twitter_creator
twitter_card
facebook_app_id
locale
extra_props
extra_custom_props
"""

class HomeView(MetadataMixin, TemplateView):
    template_name="pages/home.html"
    title = 'My Home Page'
    description = 'This is an awesome home page'
    image = 'img/home.png'
    url = ''

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        #context['pk'] = kwargs['pk']
        #context['message'] = 'Hello World!'
        return context

home_view = HomeView.as_view()

class AboutView(MetadataMixin, TemplateView):
    template_name="pages/about.html"
    title = 'My About Page'
    description = 'This is an awesome about page'
    image = 'img/about.png'
    url = '/about'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutView, self).get_context_data(*args, **kwargs)
        #context['pk'] = kwargs['pk']
        #context['message'] = 'Hello World!'
        return context

about_view = AboutView.as_view()
