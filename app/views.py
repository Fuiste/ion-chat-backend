# -*- coding: utf-8 -*-
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from app.models import Chatter
import logging


logger = logging.getLogger('django')
__author__ = "fuiste"


class DummySessionAuthentication(SessionAuthentication):

    def authenticate(self, request):
        return None


class DeviceRegisterView(APIView):
    """
    The endpoint for Ionic's push notification service.  will receive a http POST with the device token and user
    metadata.  That's pretty neat.
    """
    authentication_classes = (DummySessionAuthentication,)

    def post(self, request, format=None):
        """
        The endpoint.  Adds the token to the Chatter model.
        """
        print "Got a POST"
        print request.POST
        print request.POST.get('metadata')

        dev_token = request.POST.get("ios_token")
        user_id = request.POST.get("metadata")["user_id"]
        chatter = Chatter.objects.get(id=user_id)
        chatter.device_token = dev_token
        chatter.save()

        return Response({"Success": "Token saved!"}, status=status.HTTP_200_OK)
