#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse

from omeroweb.webgateway import views as webgateway_views

from omeroweb.webclient.decorators import login_required, render_response

from io import BytesIO

import logging
import omero
from omero.rtypes import rstring
import omero.gateway
import random


logger = logging.getLogger(__name__)


try:
    from PIL import Image
except ImportError:
    try:
        import Image
    except ImportError:
        logger.error('No Pillow installed,\
            line plots and split channel will fail!')

@login_required()
def iframe(request, conn=None, **kwargs):
    """ Simply shows a page of scripts from an iFrame for the specified image """
    # Get image ids from params
    id_list = request.GET.get('imageIds', None)  # comma - delimited list
    id_list = request.GET.get('Image', id_list)  # we also support 'Image'
    if id_list:
        image_ids = [int(i) for i in id_list.split(",")]
    else:
        image_ids = []
    
    # roi_service = conn.getRoiService()
    # roi_ids = []
    for iid in image_ids:
        image = conn.getObject("Image", iid)
        if image is None:
            continue
        # result = roi_service.findByImage(int(iid), None, conn.SERVICE_OPTS)
        # roi_ids += [r.getId().getValue() for r in result.rois]
    return render(request, 'webtest/demo_viewers/iframe.html',
                  {'imageIds': id_list})
