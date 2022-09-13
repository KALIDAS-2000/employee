from django.shortcuts import render
from rest_framework.viewsets import ViewSet,ModelViewSet
from api.serializer import DataSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import authentication,permissions
from api.models import Data


class DataModelViews(ViewSet):
        # authentication_classes = [authentication.BasicAuthentication]
        authentication_classes = [authentication.TokenAuthentication]
        permission_classes = [permissions.IsAuthenticated]

        def list(self,request,*args,**kwargs):
            qs=Data.objects.all()
            serializer=DataSerializer(qs,many=True)
            return  Response(data=serializer.data)

        def create(self,request,*args,**kwargs):
            serializer=DataSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)

        def retrieve(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Data.objects.get(id=id)
            serializer=DataSerializer(qs)
            return  Response(data=serializer.data)

        def update(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Data.objects.get(id=id)
            serializer=DataSerializer(instance=qs,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return  Response(data=serializer.data)
            else:
                return Response(data=serializer.errors)

        def destroy(self,request,*args,**kwargs):
            id=kwargs.get("pk")
            qs=Data.objects.get(id=id)
            qs.delete
            return Response({"msg":"deleted"})

class UserViews(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class DataModelView(ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]