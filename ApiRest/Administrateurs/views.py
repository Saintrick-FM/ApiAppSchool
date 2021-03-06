from ApiRest.Administrateurs.serializer import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerUserOrListOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'post':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


# class UserView(APIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer(queryset, many=True)
#     # def get(self, request, format=None):
#     #     print("dans la methode get de base")
#     #     return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = UserSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserDetail(APIView):
#     def get(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk, format=None):
#         user = self.objects.get(pk)
#         serializer = UserSerializer(user, data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
