from django.shortcuts import render
from.models import Contact, FeedBack, Event, College, Course, Tip
from django.contrib import messages

def more_feedback(request):
    feedback_list=FeedBack.objects.all()
    context={
        "feedback_key":feedback_list

    }
    return render(request,'advice_app/html/all_feedbacks.html',context)
    

def home(request):
    feedback_list=FeedBack.objects.all()[:3]

    context={
        "feedback_key":feedback_list
    }
    return render(request,'advice_app/html/index.html',context)
def feedback(request):
    if request.method =='GET':
        return render(request,'advice_app/html/feedback.html')
    if request.method =='POST':
        user_name= request.POST["name"]
        user_email= request.POST["email"]
        user_remarks= request.POST["remarks"]
        user_ratings= request.POST["ratings"]
        #print(user_email,user_name,user_rating,user_remarks)
        #creating object of FeedBack Model

        feedback_object=FeedBack(name=user_name, email=user_email, remarks=user_remarks, ratings=user_ratings)
        #save the object
        feedback_object.save()
        messages.success(request,"Thank for your Feedback and Time!!!")



        return render(request,'advice_app/html/feedback.html')
    

def aboutus(request):
    return render(request,'advice_app/html/about_us.html')


def contactus(request):
    if request.method =='GET':
        return render(request,'advice_app/html/contact_us.html')
    if request.method =='POST':
        user_name= request.POST["name"]
        user_phone= request.POST["phone"]
        user_email= request.POST["email"]
        user_question= request.POST["question"]
        

        contactus_object=Contact(name=user_name, phone=user_phone, email=user_email, question=user_question)

        contactus_object.save()

        return render(request,'advice_app/html/contact_us.html')

# Create your views here.
    
def event_update (request):

    event_list=Event.objects.all()#Select*from event
    #print(type(event_list))
    #how to send data from views to templetes

    context={
        "event_key":event_list
    }


    return render(request,'advice_app/html/events_updates.html',context)

def view_college (request):
    college_list=College.objects.all()#select*from event
    #print(type(college_list))
    #how to send data from views to templetes

    context={
        "college_key":college_list
    }

    return render(request,'advice_app/html/college.html',context)


def course (request):
    course_list=Course.objects.all()#select*from event
    #print(type(course_list))
    #how to send data from views to templetes

    context={
        "course_key":course_list
    }

    return render(request,'advice_app/html/course.html',context)

def tips (request):
    tips_list=Tip.objects.all()

    context={
        "tips_key":tips_list
    }

    return render(request,'advice_app/html/tips.html',context)
    
