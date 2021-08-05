from django.db import models


class Client(models.Model):
    client_id = models.AutoField(db_column='Client_ID', primary_key=True)  # Field name made lowercase.
    client_name = models.CharField(db_column='Client_Name', max_length=40)  # Field name made lowercase.
    client_dob = models.DateField(db_column='Client_DOB')  # Field name made lowercase.
    client_email = models.CharField(db_column='Client_Email', max_length=40)  # Field name made lowercase.
    client_address = models.CharField(db_column='Client_Address', max_length=150)  # Field name made lowercase.
    client_contact = models.CharField(db_column='Client_Contact', max_length=10)  # Field name made lowercase.
    client_type = models.CharField(db_column='Client_Type', max_length=20)  # Field name made lowercase.
    client_blood_group = models.CharField(db_column='Client_Blood_Group', max_length=20)  # Field name made lowercase.
    client_medical_record = models.CharField(db_column='Client_Medical_Record', max_length=150, blank=True, null=True)  # Field name made lowercase.
    organ_donating = models.CharField(db_column='Organ_Donating', max_length=50, blank=True, null=True)  # Field name made lowercase.
    organ_requesting = models.CharField(db_column='Organ_Requesting', max_length=50, blank=True, null=True)  # Field name made lowercase.
    staff = models.ForeignKey('Staffs', models.DO_NOTHING, db_column='Staff_ID')  # Field name made lowercase.
    insure = models.ForeignKey('Insure', models.DO_NOTHING, db_column='Insure_ID')  # Field name made lowercase.
    client_gender = models.CharField(db_column='Client_Gender', max_length=25, blank=True, null=True)  # Field name made lowercase.
    client_height = models.CharField(db_column='Client_Height', max_length=25, blank=True, null=True)  # Field name made lowercase.
    client_weight = models.CharField(db_column='Client_Weight', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class Insurance(models.Model):
    ins_company_id = models.AutoField(db_column='Ins_Company_Id', primary_key=True)  # Field name made lowercase.
    ins_company_name = models.CharField(db_column='Ins_Company_Name', max_length=50)  # Field name made lowercase.
    ins_company_contact = models.CharField(db_column='Ins_Company_Contact', max_length=10)  # Field name made lowercase.
    ins_contact_name = models.CharField(db_column='Ins_Contact_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insurance'


class Insure(models.Model):
    insure_id = models.AutoField(db_column='Insure_ID', primary_key=True)  # Field name made lowercase.
    insure_type = models.CharField(db_column='Insure_Type', max_length=50)  # Field name made lowercase.
    insure_amount = models.FloatField(db_column='Insure_Amount')  # Field name made lowercase.
    insure_date = models.DateField(db_column='Insure_Date')  # Field name made lowercase.
    ins_company = models.ForeignKey(Insurance, models.DO_NOTHING, db_column='Ins_Company_Id')  # Field name made lowercase.
    insure_no = models.CharField(db_column='Insure_No', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Insure'


class JobDesigantion(models.Model):
    designation = models.CharField(db_column='Designation', primary_key=True, max_length=50)  # Field name made lowercase.
    salary = models.FloatField(db_column='Salary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Job_Desigantion'


class OrganAvailable(models.Model):
    organ_id = models.AutoField(db_column='Organ_Id', primary_key=True)  # Field name made lowercase.
    organ_name = models.CharField(db_column='Organ_Name', max_length=50)  # Field name made lowercase.
    date_time = models.DateTimeField(db_column='Date_time', blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Organ_Available'


class Procurement(models.Model):
    p_id = models.AutoField(db_column='P_ID', primary_key=True)  # Field name made lowercase.
    p_date = models.DateField(db_column='P_date', blank=True, null=True)  # Field name made lowercase.
    p_time = models.TimeField(db_column='P_time', blank=True, null=True)  # Field name made lowercase.
    p_description = models.CharField(db_column='P_description', max_length=150, blank=True, null=True)  # Field name made lowercase.
    p_amount = models.FloatField(db_column='P_amount', blank=True, null=True)  # Field name made lowercase.
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='Client_ID')  # Field name made lowercase.
    organ = models.ForeignKey(OrganAvailable, models.DO_NOTHING, db_column='Organ_Id')  # Field name made lowercase.
    staff = models.ForeignKey('Staffs', models.DO_NOTHING, db_column='Staff_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Procurement'


class Staffs(models.Model):
    staff_id = models.AutoField(db_column='Staff_ID', primary_key=True)  # Field name made lowercase.
    staff_name = models.CharField(db_column='Staff_Name', max_length=50)  # Field name made lowercase.
    staff_email = models.CharField(db_column='Staff_Email', max_length=50)  # Field name made lowercase.
    staff_address = models.CharField(db_column='Staff_Address', max_length=150)  # Field name made lowercase.
    staff_contact = models.CharField(db_column='Staff_Contact', max_length=10)  # Field name made lowercase.
    staff_designation = models.ForeignKey(JobDesigantion, models.DO_NOTHING, db_column='Staff_Designation', blank=True, null=True)  # Field name made lowercase.
    staff_dob = models.DateField(db_column='Staff_DOB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Staffs'


class CInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    requesting = models.CharField(max_length=50)
    available = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=10)


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class OrganAvailable1(models.Model):
    client_id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    client_name = models.CharField(max_length=50)


class Rep(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=25, blank=True, null=True)
    dob = models.DateField()
    contact = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=20)
    requesting = models.CharField(max_length=50, blank=True, null=True)


class Don(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    gender = models.CharField(max_length=25, blank=True, null=True)
    dob = models.DateField()
    contact = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=20)
    donating = models.CharField(max_length=50, blank=True, null=True)


class OrganAvail(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    count = models.IntegerField()
