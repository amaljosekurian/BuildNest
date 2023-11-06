from django.contrib.auth import login, authenticate,get_user_model
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
from django.views.decorators.cache import never_cache
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail



#@never_cache
def index(request):
    return render(request, "index.html")


#@login_required
def index2(request):
    if 'email' in request.session:
       response = render(request, 'index2.html')
       response['Cache-Control'] = 'no-store, must-revalidate'
       return response
    else:
       return redirect('index')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        role = request.POST['role']
        firstname = request.POST['fname']
        email = request.POST['email']
        lastname = request.POST['lname']
        dob = request.POST['dob']
        password = request.POST['password']
        phone = request.POST['phone']

        user = Usertable(first_name=firstname, last_name=lastname, email=email, dob=dob, phone=phone, username=username)
        user.set_password(password)
        
        if role == 'Contractor_user':
            user.is_contractor = True
        elif role == 'Client_user':
            user.is_client = True
        elif role == 'Purchase_manager':
            user.is_purchase_manager = True
        
        user.save()
        return redirect('login')
        # return HttpResponse(role)

    return render(request, "signup.html")

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_client:
                return redirect("client")
            elif user.is_contractor:
                return redirect("contractor")
            elif user.is_admin:
                return redirect("adminreg")
            elif user.is_purchase_manager:
                return redirect("purchase_manager")
            else:
                return HttpResponse("Not Found")
        else:
            return HttpResponse('User Not Avail')
    else:
        return render(request, 'login.html')



def adminreg(request):
    if request.method == 'POST':
        for user in Usertable.objects.exclude(is_admin=True):
            status_field_name = f'user_status_{user.email}'
            user_status = request.POST.get(status_field_name, '')  # Get the value of the checkbox

            if user_status == 'on':
                # If the checkbox is checked, activate the user
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    send_activation_email(user)  # Send an email for activation
            else:
                # If the checkbox is not checked, deactivate the user
                if user.is_active:
                    user.is_active = False
                    user.save()
                    send_deactivation_email(user)  # Send an email for deactivation
    else:
        # Retrieve users based on their roles
        admin_users = Usertable.objects.filter(is_admin=True)
        Purchase_manager = Usertable.objects.filter(is_purchase_manager=True)
        Client_user = Usertable.objects.filter(is_client=True)
        Contractor_user = Usertable.objects.filter(is_contractor=True)
    
    context = {
        'admin_users': admin_users,
        'Purchase_manager': Purchase_manager,
        'Client_user': Client_user,
        'Contractor_user': Contractor_user,
    }

    return render(request, 'adminreg.html', context)


def logout(request):
    auth_logout(request)
    return redirect('index')

def toggle_active(request, user_id, is_active):
    try:
        user = Usertable.objects.get(id=user_id)
        # Convert the "is_active" parameter to a boolean
        is_active = is_active.lower() == 'true'
        # Toggle the active status
        user.is_active = not is_active
        user.save()
        messages.success(request, f'User is now {"Active" if user.is_active else "Inactive"}.')
    except Usertable.DoesNotExist:
        messages.error(request, 'User not found.')
    return redirect('admind')  # Replace 'admind' with your actual admin dashboard URL name


def user_profile(request):
    user = request.user
    formatted_dob = user.dob.strftime('%Y-%m-%d') if user.dob else ''
    context = {'user': user, 'formatted_dob': formatted_dob}
    return render(request, 'user_profile.html', context)


def update_user_details(request):
    if request.method == 'POST':
        new_dob = request.POST.get('new_dob')
        new_first_name = request.POST.get('new_first_name')
        new_last_name = request.POST.get('new_last_name')
        new_phone_number = request.POST.get('new_phone_number')  # Add this line

        # Update the user's details in the database
        user = request.user
        user.dob = new_dob
        user.first_name = new_first_name
        user.last_name = new_last_name
        user.phone_number = new_phone_number  # Add this line
        user.save()

        messages.success(request, 'User details updated successfully.')
        return redirect('user_profile')  # Redirect to the user profile page

    return render(request, 'user_profile')

def contractor(request):
    # Your view logic here, if needed
    return render(request, 'contractor.html')

def client(request):
    # Your view logic here, if needed
    return render(request, 'client.html')

def purchase_manager(request):
    # Add your view logic here if needed
    return render(request, 'purchase_manager.html')

# def contractor_dashboard(request):
#     # Your view logic here
#     return render(request, 'contractor/dashboard.html')

def send_activation_email(user):
    send_mail(
        'Account Activation',
        'Your account has been activated. You can now log in and access your account.',
        'wheelways2@gmail.com',  # Replace with your email address
        [user.email],
        fail_silently=False,
    )

def send_deactivation_email(user):
    send_mail(
        'Account Deactivation',
        'Your account has been deactivated. Please contact the admin for more information.',
        'wheelways2@gmail.com',  # Replace with your email address
        [user.email],
        fail_silently=False,
    )






# def delAdmin(request):
#     id=3
#     Usertable.objects.get(id=id).delete()
#     return HttpResponse('Successfully Deleted')