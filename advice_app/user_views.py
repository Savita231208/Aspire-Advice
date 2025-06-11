from django.shortcuts import render , redirect
from.models import Counsellor,Student,Tip, Message, Appointment
from django.contrib import messages
from django.http import JsonResponse

def counsellor_logout(request):
    if "session_key" not in request.session.keys():
        return redirect("coun_login")
    request.session.flush() #clearing all the values bind in that session
    return redirect("coun_login")   #redirect to register page after logging out. name of the view

def student_logout(request):
    if "session_key" not in request.session.keys():
        return redirect("student_login")
    request.session.flush() #clearing all the values bind in that session
    return redirect("student_login")   #redirect to register page after logging out. name of the view

def confirm_app(request):
    c_id=request.session["session_key"]
    c_obj=Counsellor.objects.get(c_id=c_id)
        
    appointment_list=Appointment.objects.filter(status='True', cou_detail=c_obj)
    context={
        "appointment_key":appointment_list
    }
    return render(request,'advice_app/user/confirm_app.html',context)
def appo_status(request):
    st_id=request.session["session_key"]
    st_obj=Student.objects.get(st_id=st_id)

    appointment_list=Appointment.objects.filter(stu_detail=st_obj)
    context={
        "appointment_key":appointment_list
    }
    return render(request,'advice_app/student/appo_status.html',context)

def pending_app(request):
    if request.method=='GET':
        c_id=request.session["session_key"]
        c_obj=Counsellor.objects.get(c_id=c_id)
        
        appointment_list=Appointment.objects.filter(status='False', cou_detail=c_obj)
        context={
            "appointment_key":appointment_list
        }
        return render(request,'advice_app/user/pending_app.html',context)
    
    if request.method=='POST':
    
        a_id=request.POST["aid"]
        msg=request.POST["message"]
        Appointment_obj=  Appointment.objects.get(id=a_id)
        Appointment_obj.coun_ans=msg
        Appointment_obj.status='True'
        Appointment_obj.save()
        appointment_list=Appointment.objects.filter(status='False', cou_detail=c_obj)
        context={
            "appointment_key":appointment_list
        }
        messages.success(request,"Status Uploaded !!!")
        return render(request,'advice_app/user/pending_app.html',context)
    


def appointment(request):
    if request.method=='GET':
        counsellor_list=Counsellor.objects.all()
        context={
            "obj_key":counsellor_list
        }
        return render(request,'advice_app/student/appointment.html',context)
    if request.method=='POST':
        stu_id=request.session["session_key"]
        stu_obj=Student.objects.get(st_id=stu_id)
        coun_id=request.POST["select"]
        coun_obj=Counsellor.objects.get(c_id=coun_id)
        message=request.POST["message"]
        date=request.POST["date"]
        appointment_object=Appointment(stu_detail=stu_obj,cou_detail=coun_obj,message=message,date=date)
        appointment_object.save()
        counsellor_list=Counsellor.objects.all()
        context={
            "obj_key":counsellor_list
        }
        messages.success(request,"Appointment request sent successfully...")
        

        return render(request,'advice_app/student/appointment.html',context)
    
def c_compose(request):
    if request.method=='GET':
        return render(request,'advice_app/user/c_compose.html')
    
    
    
    if request.method=='POST':
        sender_id=request.session["session_key"]
        receiver_id=request.POST["receiver_id"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        message_object=Message(sender_id=sender_id,receiver_id=receiver_id,subject=subject,message=message)
        message_object.save()
        messages.success(request,"Message sent successfully...")
        
        return render(request,'advice_app/user/c_compose.html')

def c_inbox(request):
    id=request.session["session_key"]
    msg_list=Message.objects.filter(receiver_id=id) 
    context={
        "obj_key":msg_list
    }
    return render(request,'advice_app/user/c_inbox.html',context)


def s_compose(request):
    if request.method=='GET':
        return render(request,'advice_app/student/s_compose.html')
    
    
    if request.method=='POST':
        sender_id=request.session["session_key"]
        receiver_id=request.POST["receiver_id"]
        subject=request.POST["subject"]
        message=request.POST["message"]
        message_object=Message(sender_id=sender_id,receiver_id=receiver_id,subject=subject,message=message)
        message_object.save()
        messages.success(request,"Message sent successfully...")
        
        return render(request,'advice_app/student/s_compose.html')

def s_inbox(request):
    id=request.session["session_key"]
    msg_list=Message.objects.filter(receiver_id=id) 
    context={
        "obj_key":msg_list
    }
    return render(request,'advice_app/student/s_inbox.html',context)

def showmessage(request,id):
    id=request.GET["msg_id"]
    print("id here is",id)
    m_id=int(id)
    msg_obj=Message.objects.get(id=m_id)
    message_data=msg_obj.message
    context={"m1_key":message_data,
            }
    return JsonResponse(context)

# def logout(request):
#     request.session.flush()#clearing all the values bind in that session
#     return redirect("student_login")#name of the view

def add_tips(request):
     if "session_key" not in request.session.keys():
         return redirect("expert_login")
     
     if request.method == 'GET':
        return render(request,'advice_app/user/add_tips.html')
     
     if request.method == 'POST':
         
         co_id= request.session["session_key"]
         cobj= Counsellor.objects.get(c_id=co_id)

         add_topic= request.POST["topic"]
         add_content= request.POST["contents"]


         add_tips_object=Tip(counsellor=cobj,cu_topic=add_topic,cu_content=add_content)
         add_tips_object.save()
         messages.success(request,"Tip uploaded successfully!!!")

         return render(request,'advice_app/user/add_tips.html')


        

def student_edit_profile(request):
    if request.method =="GET":
        id=request.session["session_key"]
        obj= Student.objects.get(st_id=id)
        context={
        "obj_key":obj
    }
        return render(request,'advice_app/student/student_edit_profile.html',context)
    
    if request.method == 'POST':
        namechange=request.POST["name"]
        emailchange=request.POST["email"]
        phonechange=request.POST["phone"]
        citychange=request.POST["city"]
        qualificationchange=request.POST["qualification"]
        id=request.session["session_key"]
        obj= Student.objects.get(st_id=id)
        obj.st_name=namechange
        obj.st_email=emailchange
        obj.st_phone=phonechange
        obj.st_city=citychange
        obj.st_qualification=qualificationchange
        obj.save()
        context={
        "obj_key":obj
    }
        return render(request,'advice_app/student/student_home.html',context)
    
def coun_edit_profile(request):
    if request.method =="GET":
        id=request.session["session_key"]
        obj= Counsellor.objects.get(c_id=id)
        context={
            "obj_key":obj
        }
        return render(request,'advice_app/user/coun_edit_profile.html',context)
    
    if request.method == 'POST':
        namechange=request.POST["name"]
        emailchange=request.POST["email"]
        phonechange=request.POST["phone"]
        citychange=request.POST["city"]
        qualificationchange=request.POST["qualification"]
        experiencechange=request.POST["experience"]
        genderchange=request.POST["gender"]
        skillschange=request.POST["skills"]
        addresschange=request.POST["address"]
        id=request.session["session_key"]
        obj= Counsellor.objects.get(c_id=id)
        obj.c_name=namechange
        obj.c_email=emailchange
        obj.c_phone=phonechange
        obj.c_city=citychange
        obj.c_qualification=qualificationchange
        obj.c_experience=experiencechange
        obj.c_gender=genderchange
        obj.c_skills=skillschange
        obj.c_address=addresschange
        obj.save()
        context={
        "obj_key":obj
    }
        return render(request,'advice_app/user/coun_home.html',context)


#function for home
def student_home(request):
    id=request.session["session_key"]
    obj= Student.objects.get(st_id=id)
    context={
        "obj_key":obj
    }
    return render (request,'advice_app/student/student_home.html',context)

def coun_home(request):
    id=request.session["session_key"]
    obj= Counsellor.objects.get(c_id=id)
    context={
        "obj_key":obj
    }
    return render (request,'advice_app/user/coun_home.html',context)






def login(request):
    if request.method == 'GET':
        return render (request,'advice_app/student/student_login.html')
    if request.method == 'POST':
        user_id=request.POST["user_id"]
        password=request.POST["password"]

        user_list=Student.objects.filter(st_id=user_id,st_password=password)
        size=len(user_list)
        if size>0:
            print ("user exists")
            #binding id in session
            request.session["session_key"]=user_id
            obj= Student.objects.get(st_id=user_id)
            context={
                     "obj_key":obj
                }
            return render (request,'advice_app/student/student_home.html',context)
        else:
            messages.error(request,"Invalid user")

        return render (request,'advice_app/student/student_login.html')
    
def conlogin(request):
    if request.method == 'GET':
        return render (request,'advice_app/user/coun_login.html')
    if request.method == 'POST':
        user_id=request.POST["user_id"]
        password=request.POST["password"]

        user_list=Counsellor.objects.filter(c_id=user_id,c_password=password)
        size=len(user_list)
        if size>0:
            print ("user exists")
            request.session["session_key"]=user_id
            obj= Counsellor.objects.get(c_id=user_id)
            context={
                     "obj_key":obj
                }
            return render (request,'advice_app/user/coun_home.html',context)
        else:
            messages.error(request,"Invalid user")

        return render (request,'advice_app/user/coun_login.html')

    
def registration(request):
    if request.method == 'GET':
        return render(request,'advice_app/user/user_registration.html')
    if request.method =='POST':
        reg_id= request.POST["id"]
        reg_password= request.POST["password"]
        reg_name= request.POST["name"]
        reg_email= request.POST["email"]
        reg_phone= request.POST["phone"]
        reg_city= request.POST["city"]
        reg_experience= request.POST["experience"]
        reg_qualification= request.POST["qualification"]
        reg_gender= request.POST["gender"]
        reg_skill= request.POST["skill"]
        reg_address= request.POST["address"]

        #print(c_id,c_password,c_name,c_email, c_phone,c_city, c_experience, c_qualification, c_gender, c_skill, c_address)
        

        registration_object=Counsellor(c_id=reg_id, c_password=reg_password, c_name=reg_name, c_email=reg_email, c_phone=reg_phone, c_city=reg_city, c_experience=reg_experience, c_qualification=reg_qualification, c_gender=reg_gender, c_skills=reg_skill, c_address=reg_address)
        #save the object
        registration_object.save()



        return render(request,'advice_app/user/user_registration.html')
    

def stu_registration(request):
    if request.method == 'GET':
        return render(request,'advice_app/student/stu_registration.html')
    if request.method =='POST':
        stu_id= request.POST["id"]
        stu_password= request.POST["password"]
        stu_name= request.POST["name"]
        stu_email= request.POST["email"]
        stu_phone= request.POST["phone"]
        stu_city= request.POST["city"]
        stu_qualification= request.POST["qualification"]
        stu_gender= request.POST["gender"]
        stu_address= request.POST["address"]

        stu_registration_object=Student(st_id=stu_id,st_password=stu_password,st_name=stu_name,st_email=stu_email,st_phone=stu_phone,st_city=stu_city,st_qualification=stu_qualification,st_gender=stu_gender,st_address=stu_address)

        stu_registration_object.save()
        return render(request,'advice_app/student/stu_registration.html')