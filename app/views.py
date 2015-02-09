# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from app.models import Chatter
import logging


logger = logging.getLogger('testlogger')
__author__ = "fuiste"


class DeviceRegisterView(View):
    """
    The endpoint for Ionic's push notification service.  will receive a http POST with the device token and user
    metadata.  That's pretty neat.
    """

    def post(self, request):
        """
        The endpoint.  Adds the token to the Chatter model.
        """
        logger.info("Got a POST")
        logger.info(request.POST)

        dev_token = request.POST['ios_token']
        user_id = request.POST['metadata']['user_id']
        chatter = Chatter.objects.get(id=user_id)
        chatter.device_token = dev_token
        chatter.save()

        return HttpResponse(json.dumps({"Success": "Token saved!"}), content_type="application/json")

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(DeviceRegisterView, self).dispatch(*args, **kwargs)