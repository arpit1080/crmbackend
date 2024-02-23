from rest_framework import viewsets
from .serializers import UserSerializers
from .models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.crypto import get_random_string


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

@csrf_exempt
def delete_user_by_id(request, user_id):
    if request.method == 'DELETE':
        user = get_object_or_404(User, id=user_id)
        user.delete()
        return JsonResponse({'success': True, 'message': 'User deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

# def get_user_by_id(request, user_id):
#     try:
#         user = User.objects.get(id=user_id)
#         serialized_user = UserSerializers(user)  # Assuming you have a serializer for your User model named UserSerializer
#         return JsonResponse({'success': True, 'user': serialized_user.data})
#     except User.DoesNotExist:
#         return JsonResponse({'error': 'User not found'}, status=404)
    
def get_user_by_id(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        serialized_user = UserSerializers(user)
        return JsonResponse({'success': True, 'user': serialized_user.data})
    except Exception as e:
        return JsonResponse({'error': 'user not found'}, status=404)
    
def get_all_user(request):
    try:
        user = User.objects.all()
        serialized_users = UserSerializers(user)  # Assuming you have a serializer for your User model named UserSerializer
        return JsonResponse({'success': True, 'user': serialized_users.data})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


    
@csrf_exempt
def update_user_by_id(request, user_id):
    if request.method == 'PUT':
        user = get_object_or_404(User, id=user_id)
        try:
            data = json.loads(request.body.decode('utf-8'))
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        email = data.get('Email', user.Email)
        if User.objects.exclude(id=user_id).filter(Email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        mobile_number = data.get('Mobile_Number', user.Mobile_Number)
        if User.objects.exclude(id=user_id).filter(Mobile_Number=mobile_number).exists():
            return JsonResponse({'error': 'Mobile_Number already exists'}, status=400)
        



        
        # Update the user object based on the data received in the request body
        user.Username = data.get('Username', user.Username)
        user.DOB = data.get('DOB', user.DOB)
        user.Email = data.get('Email', user.Email)
        user.Mobile_Number = data.get('Mobile_Number', user.Mobile_Number)
        user.Profile_Photo = data.get('Profile_Photo', user.Profile_Photo)
        user.First_Name = data.get('First_Name', user.First_Name)
        user.Last_Name = data.get('Last_Name', user.Last_Name)
        user.save()
        
        return JsonResponse({'success': True, 'message': 'User updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)    
    

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print("Received data:", data)

        username = data.get('Username', '')
        password = data.get('Password', '')
        print("Username and password:", username, password)
        
        if username and password:  # Check if username and password are provided
            try:
                user = authenticate(request, username=username, password=password)
                print("Authenticated user:", user)
                if user:
                    # Authentication successful
                    return JsonResponse({'message': 'Login successful'})
                else:
                    # Authentication failed
                    return JsonResponse({'message': 'Invalid credentials'}, status=401)
            except Exception as e:
                print('Authentication error:', e)
                return JsonResponse({'message': 'Internal server error'}, status=500)
        else:
            return JsonResponse({'message': 'Username or password missing'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)



@csrf_exempt
def forgot_password(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        email = data.get('Email', '')

        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return JsonResponse({'message': 'User not found'}, status=404)

            # Generate a reset password token
            token = get_random_string(length=20)

            # Update user's reset password token in database
            user.reset_password_token = token
            user.save()

            # Send email with reset password link
            reset_password_link = f"http:///resetpassword?token={token}"
            message = f"Please click the following link to reset your password: {reset_password_link}"
            send_mail(
                'Password Reset',
                message,
                'dtest6366@example.com',
                [email],
                fail_silently=False,
            )

            return JsonResponse({'message': 'Reset password link sent to your email'})
        else:
            return JsonResponse({'message': 'Email is required'}, status=400)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)



# @csrf_exempt

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('Username')
#         password = request.POST.get('Password')

#         print("Username:", username)  # Debugging
#         print("Password:", password) 

#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             # Authentication successful
#             return JsonResponse({'message': 'Login successful'})
#         else:
#             # Authentication failed
#             return JsonResponse({'message': 'Invalid credentials'}, status=401)
#     else:
#         return JsonResponse({'message': 'Method not allowed'}, status=405)


# @csrf_exempt
# def login(request):
#     if request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         print("User Data:", data)  # Debugging
#         username = data.get('Username')
#         password = data.get('Password')
#         print("Username:", username)  # Debugging
#         print("Password:", password)  # Debugging
        
#         if username and password:  # Ensure both username and password are provided
#             try:
#                 user = authenticate(request, username=username, password=password)
#                 print("Authenticated User:", user)  # Debugging
#             except Exception as e:
#                 print('Authentication Error:', e)  # Log the authentication error
#                 return JsonResponse({'message': 'Authentication error'}, status=500)
            
#             if user is not None:
#                 # Authentication successful
#                 return JsonResponse({'message': 'Login successful'})
#             else:
#                 # Authentication failed
#                 return JsonResponse({'message': 'Invalid credentials'}, status=401)
#         else:
#             return JsonResponse({'message': 'Username or password missing'}, status=400)
#     else:
#         return JsonResponse({'message': 'Method not allowed'}, status=405)
    
# Define test_database_connection function here

