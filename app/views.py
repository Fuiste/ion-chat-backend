# -*- coding: utf-8 -*-
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from app.models import Chatter, Message
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
        post_dict = json.loads(request.body)
        dev_token = post_dict["ios_token"]
        user_id = post_dict["metadata"]["user_id"]
        chatter = Chatter.objects.get(id=user_id)
        chatter.device_token = dev_token
        chatter.save()

        return Response({"Success": "Token saved!"}, status=status.HTTP_200_OK)


class UpdateMessagesView(APIView):
    """
    When a push is received, this view returns new messages to update the history on a user's 'home' page.
    """
    def get(self, request, format=None):
        """
        The API endpoint
        """
        user = Chatter.objects.get(id=request.GET.get("user_id"))
        msgs = Message.objects.filter(msg_to=user)
        ret_dict = {}
        ret_dict["messageHistory"] = []
        if len(msgs) > 5:
            # for m in msgs[len(msgs)-5:]:
            for m in msgs[:5]:
                dict["messageHistory"].append({"text": m.text, "from": m.msg_from.full_name, "fromEmail": m.msg_from.email, "img": m.msg_from.imgur_url})
        else:
            for m in msgs:
                dict["messageHistory"].append({"text": m.text, "from": m.msg_from.full_name, "fromEmail": m.msg_from.email, "img": m.msg_from.imgur_url})
        return Response(ret_dict)
