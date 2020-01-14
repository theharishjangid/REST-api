from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET', 'POST'])
def index(request):
    print(request.user)
    print(request.auth)
    if request.method == 'GET':
        message = 'this is test url'
        return Response(data=message, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response(data = request.data, status= status.HTTP_200_OK)
    else:
        return Response(data="this request is invalid")


class Message(APIView):

    def get(self, request):
        print('hit by get request')
        return Response(data="This is class based view hit by get", status= status.HTTP_200_OK)

    def post(self, request):
        print('hit by post request')
        print(request.data)
        return Response(data="This is class based view hit by post", status= status.HTTP_200_OK)