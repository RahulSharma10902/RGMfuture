from django.shortcuts import render,redirect
from RGMfuture.settings import EMAIL_HOST_USER,EMAIL_RECEIVER
from django.core.mail import send_mail

# from RGM.settings
# Create your views here.
def loading(request):
    return render(request,'loading.html')
def index(request):
    return render(request,'index.html')

def resourceForm(request):
    try :
        if request.method =='POST':
            cname=request.POST.get('name')
            phone=request.POST.get('phone')
            email=request.POST.get('email')
            message=request.POST.get('message')
            country=request.POST.get('country')
            city=request.POST.get('city')
            state=request.POST.get('state')
            product=request.POST.get('product')
            print(cname," ",phone," ",product," ",email," ",message)
            address=city+", "+state+", "+country
            subject="Client Inquiry Alert"
            msg=f"""
Dear,

I hope this message finds you well. I am writing to inform you about a recent inquiry we received from a client regarding one of our products. Below are the details of the inquiry:

Client Information:

Name: {cname}

Phone Number: {phone}

Email Address: {email}

Address:{address}

Product Inquiry:

Product Name: {product}

Special Message/Requirements: {message}

Thank you for your attention.

Best regards,

Team RGMFUTUREVISION 21
                    """
            from_email=EMAIL_HOST_USER
            recipient_list=[EMAIL_RECEIVER]
            send_mail(subject,msg,from_email,recipient_list)
    except Exception as e:
        print(e)
    return redirect('/index/')
def carrer(request):
    return render(request,'career.html')
def contactForm(request):
    try:  
        if request.method=="POST":
            name=request.POST.get("clientName")
            email=request.POST.get('email')
            phone=request.POST.get("phoneNumber")
            service=request.POST.get("option")
            message=request.POST.get("message")
            subject="Client Contact Alert"
            message=f"""
Dear,

I hope this email finds you well.

I am reaching out to share my contact details for any future communication or collaboration opportunities. Below are my contact details:

Phone Number: {phone}

Category: {service}

Email: {email}

Message: {message}

Please feel free to reach out to me at any time. 

Thank you for your attention.

Best regards,

{name}
                        """
            from_email=EMAIL_HOST_USER
            recipient_list=[EMAIL_RECEIVER]
            send_mail(subject,message,from_email,recipient_list)
    except Exception as e:
        print(e)
    return redirect("/index/")
def team(request):
    return render(request,'team.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')