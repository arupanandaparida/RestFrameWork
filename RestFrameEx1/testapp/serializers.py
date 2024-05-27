from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from testapp.models import Employee
def multiples_of_1000(value):
    print('Validation by validator attribute')
    if value%1000 != 0:
        raise serializers.ValidationError('Employee salary should be multiples of 1000')



class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField(validators=[multiples_of_1000])
    eaddr = serializers.CharField(max_length=64)
    
    def validate(self,data):
        print('Object level validation')
        ename = data.get('ename')
        esal = data.get('esal')
        if ename.lower() == 'arupa':
            if esal < 50000:
                raise serializers.ValidationError('Sunny salary should be minimum 50000')
        return data
    def validate_data(self,data):
        print('Field level validation')
        esal = data.get('esal')
        if esal < 5000:
                raise serializers.ValidationError('Sunny salary should be minimum 50000')
        
            
        return data
    
    
    def validate_esal(self,value):
        if value < 5000:
            raise serializers.ValidationError('Employee salary should be minimum 5000')
        return value
    
    
    def create(self, validated_data):

        return Employee.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.eno=validated_data.get('eno',instance.eno)
        instance.ename=validated_data.get('ename',instance.ename)
        instance.esal=validated_data.get('esal',instance.esal)
        instance.eaddr=validated_data.get('eaddr',instance.eaddr)
        instance.save()
        return instance