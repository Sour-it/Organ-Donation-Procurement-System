import datetime
import pytz
from io import BytesIO

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
from django.template import loader
from django.http import HttpResponse


@api_view(['GET'])
def get_client(request):
    data = CInfo.objects.raw('SELECT c.Client_ID AS id, c.Client_Name as name, c.Organ_Requesting AS requesting, o.Organ_Id AS available, c.Client_Contact AS contact FROM Client c LEFT JOIN Organ_Available o ON c.Organ_Requesting = o.Organ_Name WHERE c.Client_Type LIKE %s AND c.Client_ID NOT IN (SELECT Client_ID FROM Procurement);', ['%recipient%'])
    serializer = ClientSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def new_client(request):
    cdata = request.data
    cdata['client_dob'] = cdata['client_dob'][:10]
    ins = Insure.objects.latest('insure_id').insure_id
    cdata['staff'], cdata['insure'] = 2, ins
    cdata = NewClientSerializer(data=cdata)
    if cdata.is_valid():
        cdata.save()
    else:
        print(cdata)
    return Response(None, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_job(request):
    data = JobDesigantion.objects.all()
    serializer = JobDesigantionSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_comp(request):
    data = Insurance.objects.all()
    serializer = InsuranceSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_insurance(request):
    insdata = request.data
    insdata['insure_date'] = insdata['insure_date'][:10]
    insdata = InsureSerializer(data=insdata)
    if insdata.is_valid():
        insdata.save()
    else: print(insdata.data)
    return Response(None, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def put_staff(request):
    data = request.data
    data['staff_dob'] = data['staff_dob'][:10]
    data = StaffsSerializer(data=data)
    if data.is_valid():
        data.save()
    else:
        print('error', data.data)
    return Response(None, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_staff(request):
    staff = Staff.objects.raw("SELECT Staff_ID AS id, Staff_Name AS name FROM Staffs WHERE Staff_Designation LIKE %s;", ['%Surgeon%'])
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def new_procurement(request):
    data = request.data
    data['p_date'] = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))[:10]
    data['p_time'] = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))[11:19]
    print(data)
    data = ProcSerializer(data=data)
    if data.is_valid():
        data.save()
    else:
        print('error')
    return Response(None, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_bill(request):
    data = Procurement.objects.latest('p_id')
    sdata = Staffs.objects.get(staff_id=data.staff_id)
    cdata = Client.objects.get(client_id=data.client.client_id)
    print(data.p_id)
    template = loader.get_template('bill.html')
    context = {
        'date': str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))[:10],
        'proc': data,
        'staff': sdata,
        'client': cdata,
        'tamount': data.p_amount + 1050
    }
    temp = template.render(context, request)
    # result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(temp.encode("ISO-8859-1")), result, link_callback=True)
    # if not pdf.err:
    #     response = HttpResponse(result.getvalue(), content_type='application/pdf')
    #     response['Content-Disposition'] = 'attachment; filename="{}".pdf'.format(data.p_id)
    #     return response
    return HttpResponse(temp)


@api_view(['GET', 'POST'])
def organ(request):
    if request.method == 'GET':
        data = OrganAvail.objects.raw('select Organ_Name as name, count(*) as count from Organ_Available where Organ_Available.Organ_Id not in (select Organ_Id from Procurement) group by Organ_Name;')
        serializer = OrganAvailSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        data['date_time'] = str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))[:10] + ' ' + str(datetime.datetime.now(pytz.timezone('Asia/Kolkata')))[11:19]
        data = OrganSerializer(data=data)
        if data.is_valid():
            data.save()
        else:
            print('error')
        return Response(None, status=status.HTTP_200_OK)



@api_view(['GET'])
def avail(request):
    data = OrganAvailable1.objects.raw("SELECT DISTINCT c.Client_ID AS client_id, c.Client_Name AS client_name FROM Client c WHERE c.Client_Type LIKE %s AND c.Client_ID NOT IN (SELECT Organ_Available.Client_ID FROM Organ_Available);", ['%donor%'])
    serializer = Organ1Serializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_rep(request):
    data = Rep.objects.raw("SELECT  Client_ID AS id, Client_Name As name, Client_Gender AS gender, Client_DOB AS dob, Client_Contact AS contact, Client_Blood_Group AS blood_group, Organ_Requesting AS requesting FROM Client WHERE Client_Type LIKE %s;", ['%recipient%'])
    serializer = RepSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_don(request):
    data = Don.objects.raw("SELECT  Client_ID AS id, Client_Name As name, Client_Gender AS gender, Client_DOB AS dob, Client_Contact AS contact, Client_Blood_Group AS blood_group, Organ_Donating AS donating FROM Client WHERE Client_Type LIKE %s;", ['%donor%'])
    serializer = DonSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_staffs(request):
    data = Staffs.objects.all()
    serializer = StaffsSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
