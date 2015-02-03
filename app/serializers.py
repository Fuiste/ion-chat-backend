from django.http import Http404
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Message, Chatter
from rest_framework import parsers, renderers, status
from rest_framework.authtoken.models import Token


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
        return Response(serializer.validate(request.DATA).id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = MessageSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
            serializer.save()
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