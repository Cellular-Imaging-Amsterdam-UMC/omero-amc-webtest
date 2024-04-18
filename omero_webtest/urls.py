#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.urls import re_path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    # Params are passed in request, E.g. imageIds
    re_path(r'^iframe/$', views.iframe,
            name="webtest_scripts"),
]
