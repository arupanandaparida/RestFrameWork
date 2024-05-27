from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView




class EmployeeListView(APIView):
    def get(self,request):
        qs=Employee.objects.all()
        serializer=EmployeeSerializer(qs,many=True)
        return Response(serializer.data)
    # queryset=Employee.objects.all()
    # serializer_class=EmployeeSerializer
class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
class EmployeeRetraiveAPIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    #lookup_field='id'
class EmployeeUpdateApiview(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'
class EmployeeDeleteAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='id'

