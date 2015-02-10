from django.http import Http404
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, status, renderers, parsers
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Message, Chatter
from rest_framework.authtoken.models import Token
from django.utils import timezone
import logging
import urllib2
import json


logger = logging.getLogger('django')
__author__ = 'fuiste'


class EmailUserAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
                attrs['user'] = user
                return user
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "email" and "password"')
            raise serializers.ValidationError(msg)


class EmailUserObtainAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = EmailUserAuthTokenSerializer
    model = Token

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        usr = serializer.validate(request.DATA)
        c_serializer = ChatterSerializer(usr)
        dict = c_serializer.data
        msgs = Message.objects.filter(msg_to=usr)
        dict["messageHistory"] = []
        if len(msgs) > 5:
            for m in msgs[len(msgs)-5:]:
                dict["messageHistory"].append({"text": m.text, "from": m.msg_from.full_name, "img": m.msg_from.imgur_url})
        else:
            for m in msgs:
                dict["messageHistory"].append({"text": m.text, "from": m.msg_from.full_name, "img": m.msg_from.imgur_url})
        return Response(dict)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class ChatterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatter


class MessageList(APIView):
    model = Message
    serializer_class = MessageSerializer

    def get(self, request, format=None):
        messages = Message.objects.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try:
            to_user = Chatter.objects.get(email=request.DATA['username'])
            from_user = Chatter.objects.get(email=request.DATA['userfrom'])
            msg = Message(msg_from=from_user, msg_to=to_user, text=request.DATA['message'], created_at=timezone.now())
            msg.save()

            # If recipient has a token stored, send them a push notification
            if to_user.device_token:
                # Build the payload
                push_dict = {}
                notification_dict = {}
                ios_dict = {}
                push_dict["platform"] = "ios"
                push_dict["tokens"] = [to_user.device_token]
                notification_dict["alert"] = "{0} says: \n{1}".format(from_user.full_name, msg.text)
                ios_dict["badge"] = 1
                ios_dict["sound"] = ""
                notification_dict["ios"] = ios_dict
                push_dict["notification"] = notification_dict

                # Build the POST
                url = "https://push.ionic.io/api/v1/push"
                opener = urllib2.build_opener(urllib2.HTTPHandler)
                req = urllib2.Request(url, data=json.dumps(data))
                req.add_header("Content-Type", "application/json")
                req.add_header("X-Ionic-Application-Id", "92e87c0b")
                req.add_header("X-Ionic-API-Key", "c34a09a9d3a5fbbdda83078daef693806d15d3435b2996ee")
                opener.open(req)


            serializer = MessageSerializer(msg)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Chatter.DoesNotExist:
            raise Http404


class ChatterList(APIView):
    model = Chatter
    serializer_class = ChatterSerializer

    def get(self, request, format=None):
        chatters = Chatter.objects.all()
        serializer = ChatterSerializer(chatters, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChatterSerializer(data=request.DATA)
        if serializer.is_valid():
            usr = serializer.save()
            usr.set_password(request.DATA['password'])
            usr.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageDetail(APIView):
    model = Message
    serializer_class = MessageSerializer

    def get_object(self, pk):
        try:
            return Message.objects.get(id=pk)
        except Message.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        message = self.get_object(pk)
        serializer = MessageSerializer(message)
        return Response(serializer.data)


class ChatterDetail(APIView):
    model = Chatter
    serializer_class = ChatterSerializer

    def get_object(self, pk):
        try:
            return Chatter.objects.get(id=pk)
        except Chatter.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        chatter = self.get_object(pk)
        serializer = ChatterSerializer(chatter)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        if "id" not in request.DATA:
             request.DATA["id"] = pk
        chatter = self.get_object(pk)
        serializer = ChatterSerializer(chatter, data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)