from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        company_name = request.POST.get('company-name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        team_size = request.POST.get('team-size')
        products = request.POST.get('products')
        requirements = request.POST.get('requirements')

        # Compose the email content
        subject = f"New Enquiry from {name}"
        message = f"""
        Name: {name}
        Company Name: {company_name}
        Email: {email}
        Mobile: {mobile}
        Team Size: {team_size}
        Products: {products}
        Requirements: {requirements}
        """
        recipient_email = ['payrollhroperations@thrivetech.info']  # Replace with the recipient's email

        try:
            send_mail(
                subject,
                message,
                email,  # Use EMAIL_HOST_USER from settings
                recipient_list=recipient_email,       # Recipients must be in a list
                fail_silently=False,
            )
            messages.success(request, "Request sent successfully! Please wait for our response. Our admin will reach you soon.")  # Success message
        except Exception as e:
            messages.error(request, f"Email failed to send: {e}")  # Error message

        # Render the home page after processing the request
        return render(request, "home.html")
    

    # Render the home page for GET requests
    return render(request, "home.html")

def whoweare(request):
    return render(request,"test.html")
def migration(request):
    return render(request,"migration1.html")
from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
from django.http import HttpResponse

def career(request):
    try:
        # MongoDB connection
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.MONGO_DB_NAME]
        collection = db["job"]

        # Initialize an empty projection dictionary
        projection = {}
        
        # Use a while loop to build the projection dictionary
        i = 1
        while i <= 8:
            projection[f"title{i}"] = 1
            projection[f"dis{i}"] = 1
            i += 1
        
        # Fetch job data with the correct projection
        raw_jobs = collection.find({}, projection)

        # List comprehension to process the job data
        jobs = [
            {"title": job[f"title{i}"], "description": job[f"dis{i}"]}
            for job in raw_jobs
            for i in range(1, 9)
            if f"title{i}" in job and f"dis{i}" in job
        ]

        return render(request, "career.html", {"jobs": jobs})

    except Exception as e:
        # Log and return the error for debugging
        return HttpResponse(f"Error: {e}")





def helpdesk(request):
    return render(request,"helpdesk.html")

def customersupport(request):
    return render(request,"customersupport.html")
def uiux(request):
    return render(request,"uiux.html")
def website(request):
    return render(request,"website.html")

def forge(request):
    return render(request,"forge.html")
def form(request):
     if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first', '')
        last_name = request.POST.get('last', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        position = request.POST.get('position', '')
        location = request.POST.get('location', '')
        experience = request.POST.get('experience', '')
        work = request.POST.get('work', '')
        resume = request.FILES.get('resume', None)  # Handle uploaded file

        # Prepare email content
        subject = f"Job Application from {first_name} {last_name}"
        message = f"""
        A new job application has been submitted:

        Name: {first_name} {last_name}
        Email: {email}
        Phone: {phone}
        Position Applied For: {position}
        Current Location: {location}
        Years of Experience: {experience}
        Work Flexibility Preferences: {work}
        """

        recipient_list = ['payrollhroperations@thrivetech.info']  # Replace with the recipient's email
        sender = 'thrivetech1991@gmail.com'  # Replace with the sender's email (configured in Django settings)

        try:
            # Attach resume if uploaded
            if resume:
                email_message = EmailMessage(subject, message, sender, recipient_list)
                email_message.attach(resume.name, resume.read(), resume.content_type)
                email_message.send()
            else:
                send_mail(subject, message, sender, recipient_list)

            messages.success(request, "Form submitted successfully!")
        except Exception as e:
            messages.error(request, f"Failed to submit the form: {e}")

          # Replace 'form' with the name of your form URL pattern

     return render(request, "form.html")  
 


     
    
    
    