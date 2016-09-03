from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions


class PublicWechat(APIView):
    renderer_classes = (JSONRenderer, )
    parser_classes = (JSONParser, )
    authentication_classes = (permissions.AllowAny, )

    def get(self, request):
        return Response({"detail": "微信公众号开发"})
