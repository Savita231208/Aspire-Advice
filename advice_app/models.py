from django.db import models 
from django.utils import timezone

# Create your models here.
#feedback model
class FeedBack(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    remarks = models.TextField(null=True)
    ratings = models.CharField(max_length=5)
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

    #contact model

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone=models.CharField(max_length=10)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.name

class Event(models.Model):
    event_name=models.CharField(max_length=55,primary_key=True)
    event_venue=models.CharField(max_length=60,default="Auditorium")
    event_date=models.DateField(default=timezone.now)
    event_description=models.TextField()
    event_pic=models.FileField(max_length=100,upload_to="advice_app/event_images",default="")
    def __str__(self):
        return self.event_name

class Counsellor(models.Model):
    c_id=models.CharField(max_length=50,primary_key=True)
    c_password=models.CharField(max_length=50)
    c_name=models.CharField(max_length=100)
    c_email=models.EmailField(max_length=100)
    c_phone=models.CharField(max_length=50)
    c_city=models.CharField(max_length=50)
    c_experience=models.CharField(max_length=100)
    c_qualification=models.CharField(max_length=100)
    c_gender=models.CharField(max_length=10)
    c_skills=models.TextField()
    c_address=models.TextField()
    c_date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.c_name

class Student(models.Model):
    st_id=models.CharField(max_length=50,primary_key=True)
    st_password=models.CharField(max_length=50)
    st_name=models.CharField(max_length=50)
    st_email=models.EmailField(max_length=100)
    st_phone=models.CharField(max_length=50)
    st_city=models.CharField(max_length=50)
    st_qualification=models.CharField(max_length=100)
    st_gender=models.CharField(max_length=10)
    st_address=models.TextField()
    st_date=models.DateField(default=timezone.now)
    def __str__(self):
        return self.st_name

class Tip(models.Model):
    counsellor = models.ForeignKey(Counsellor, on_delete=models.DO_NOTHING)
    cu_topic = models.CharField(max_length=50)
    cu_content = models.TextField()
    cu_date = models.DateField(default=timezone.now)
    def __str__(self):
        return self.counsellor

class College(models.Model):
    college_code=models.CharField(max_length=50,null=False)
    college_name=models.CharField(max_length=100,null=False)
    college_city=models.CharField(max_length=50,null=False)
    college_email=models.EmailField(max_length=100,null=False)
    college_phone=models.CharField(max_length=50,null=False)
    college_address=models.TextField()
    college_website=models.CharField(max_length=100,null=False)
    college_icon=models.FileField(max_length=50,upload_to="advice_app/college_photo",default="")
    college_rating=models.CharField(max_length=10,null=False)
    def __str__(self):
        return self.college_name

class Course(models.Model):
    course_name=models.CharField(max_length=100,null=False,primary_key=True)
    duration=models.CharField(max_length=50,null=False)
    fees=models.CharField(max_length=100,null=False)
    about_course=models.TextField()
    career_option=models.TextField()
    eligibility_criteria=models.TextField()
    subjects_offered=models.TextField()
    def __str__(self):
        return self.course_name

class Message(models.Model):
    sender_id=models.CharField(max_length=20)
    receiver_id=models.CharField(max_length=20)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateField(default=timezone.now)
    
class Appointment(models.Model):
    stu_detail=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    cou_detail=models.ForeignKey(Counsellor,on_delete=models.DO_NOTHING)
    message=models.CharField(max_length=200)
    date=models.DateField(max_length=100)
    count_ans=models.TextField(null=True,blank=True)
    status=models.CharField(max_length=50,default=False)
    def __str__(self):
        return self.message
    

    




