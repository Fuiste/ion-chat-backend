# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from app.models import Chatter
import logging


logger = logging.getLogger('django')
__author__ = "fuiste"


class DeviceRegisterView(APIView):
    """
    The endpoint for Ionic's push notification service.  will receive a http POST with the device token and user
    metadata.  That's pretty neat.
    """
    authentication_classes = ()

    def post(self, request, format=None):
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

        return Response({"Success": "Token saved!"})

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(DeviceRegisterView, self).dispatch(*args, **kwargs)
