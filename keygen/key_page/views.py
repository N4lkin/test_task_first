import hashlib
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


def get_hash_data(my_data):
    try:
        byte_code = my_data.encode('ascii', errors='xmlcharrefreplace')
        return hashlib.sha1(byte_code).hexdigest()
    except AttributeError:
        pass


class SetSecretAPIView(APIView):
    def post(self, request):
        serializer = SetSecretCode(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(phrase=get_hash_data(request.POST.get('phrase')), code=get_hash_data(request.POST.get('code')))
        return Response(serializer.data['secret_key'])


# Класс для чтения код-фразы и выдачи сообщения
class GetSecretAPIView(APIView):
    def get(self, request, secret_key):
        code = request.GET.get('code')
        model = SecretKey.objects.get(pk=secret_key)
        if model.code == get_hash_data(code):
            model.delete()
            return Response(request.POST.get('phrase'))
        else:
            return Response('wrong code')
