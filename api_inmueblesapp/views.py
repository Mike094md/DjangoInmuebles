
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User, Property
from .serializers import UserSerializer, PropertySerializer

# Create your views here.
@api_view(['GET', 'POST'])
def user_list(request):
    #Obtenemos todos los usuarios
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    #Creamos un usuario nuevo
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Obtenemos un usuario
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    #modificamos un usuario
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Eliminamos un usuario
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


############ PROPERTY ##################################
########################################################

@api_view(['GET', 'POST'])
def property_list(request):
    #Obtenemos todos los inmuebles
    if request.method == 'GET':
        properties = Property.objects.all()
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    #Creamos un inmueble nuevo
    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def property_detail(request, pk):

    try:
        property = Property.objects.get(pk=pk)
    except property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #Obtenemos un inmueble
    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data)

    #modificamos un inmuelbe
    elif request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Eliminamos un inmueble
    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)