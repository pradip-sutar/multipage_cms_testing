from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Menu, Submenu
from .serializers import MenuSerializer, SubmenuSerializer

@api_view(['GET', 'POST'])
def menu_create(request):
    if request.method == 'GET':
        id = request.query_params.get('id', None)
        if id:
            menus = Menu.objects.filter(id__icontains=id)
        else:
            menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def sub_menu_create(request):
    if request.method == 'GET':
        id = request.query_params.get('id', None)
        if id:
            submenus = Submenu.objects.filter(menu_id=id)
        else:
            submenus = Submenu.objects.all()
        serializer = SubmenuSerializer(submenus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubmenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

