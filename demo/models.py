from django.db import models
from django.core.exceptions import ValidationError
from os.path import splitext

# Create your models here.
class Sequence(models.Model):
    seq_type = models.CharField(max_length=3, primary_key=True)
    prefix = models.CharField(max_length=2)
    last_number = models.IntegerField()
    
class Doctor(models.Model):
    def validate_duration(duration):
        print("validate_duration called")
        if not(duration < 10 and duration > 120 and duration%5 != 0):
            raise ValidationError("Duration should be between 10 and 120 and a multiple of 5")
        return duration
    def generateCertFileNameWithPath(instance, filename):
        # dirPath = "uploads\certificates\\"
        dirPath = "uploads/certificates//"
        _, fileExt = splitext(filename)
        board_reg_no = instance.board_reg_no
        doctor_name = instance.first_name + "-" + instance.last_name
        finalFileName = dirPath+doctor_name+"-"+board_reg_no+fileExt
        print("**********finalFileName: ", finalFileName)
        return finalFileName
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=[('M','Male'), ('F','Female')])
    speciality = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=15)
    board_reg_no = models.CharField(max_length=100, unique=True)
    system_reg_no = models.CharField(max_length=20, unique=True)
    average_time_per_patient = models.IntegerField(validators=[validate_duration], default=20)
    active = models.CharField(max_length=1, choices=[('Y','Yes'), ('N','No')])
    # profile_pic = models.ImageField()
    # board_reg_cert = models.FileField(null=True, blank=True, max_length=100, upload_to='uploads\certificates\\')
    board_reg_cert = models.FileField(null=True, blank=True, max_length=100, upload_to=generateCertFileNameWithPath)

    def __str__(self):
        return " ".join([self.first_name, self.last_name, "-", self.speciality])
