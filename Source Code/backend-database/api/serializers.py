from rest_framework import serializers
from .models import Client, CInfo, JobDesigantion, Insurance, Insure, Staffs, Staff, Procurement, OrganAvailable, OrganAvailable1, Rep, Don, OrganAvail


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CInfo
        fields = '__all__'


class NewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class JobDesigantionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDesigantion
        fields = '__all__'


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['ins_company_name', 'ins_company_id']


class InsureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insure
        fields = '__all__'


class StaffsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staffs
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class ProcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procurement
        fields = '__all__'


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganAvailable
        fields = '__all__'


class Organ1Serializer(serializers.ModelSerializer):
    class Meta:
        model = OrganAvailable1
        fields = '__all__'


class DonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Don
        fields = '__all__'


class RepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rep
        fields = '__all__'


class OrganAvailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganAvail
        fields = '__all__'
