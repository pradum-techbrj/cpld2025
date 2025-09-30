from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from app.models import Customer
from rest_framework.authtoken.models import Token


class TestApi(APIView):
    def get(self, request, *args, **kwargs):
        return Response("ok", status=status.HTTP_200_OK)


class Register(APIView):
    def post(self, request, *args, **kwargs):
        response = {
            "error": False,
            "error_msg": ""
            }
        try:
            data = request.data
            obj=Customer.objects.create(
                first_name=data['first_name'],
                last_name=data['last_name'],
                country=data['country'],
                state=data['state'],
                email=data['email'],
                contact=data['contact'],
                institution=data['institution'],
                department=data['department'],
                utrNo=data['utrNo'],
                paymentSS=data['paymentSS'],
                amount=data['amount'],
                isPosterPresentation=data['isPosterPresentation']
            )
            response['register_id']=obj.id
        except Exception as e:
            response['error'] = True
            response['error_msg'] = str(e)
        return Response(response)


class AdminLogin(APIView):
    def post(self, request, *args, **kwargs):
        response = {
            "error": False, 
            "error_msg": ""
            }
        try:
            data = request.data
            username = data['username']
            password = data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                response["message"] = "Login successful"
                response["token"] = token.key
            else:
                response['error'] = True
                response['error_msg'] = "Invalid Credentials"
        except Exception as e:
            response['error'] = True
            response['error_msg'] = str(e)
        return Response(response)

class GetAllRegister(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get(self, request, *args, **kwargs):
        response = {
            "error": False, 
            "error_msg": "", 
            "data": []
            }
        try:
            customers = Customer.objects.all().order_by('-created_at')
            for customer in customers:
                response['data'].append({
                    "register_id":customer.id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "country": customer.country,
                    "state": customer.state,
                    "email": customer.email,
                    "contact": customer.contact,
                    "institution": customer.institution,
                    "department": customer.department,
                    "utrNo": customer.utrNo,
                    "paymentSS": str(customer.paymentSS),
                    "amount": customer.amount,
                    "isPosterPresentation":customer.isPosterPresentation,
                    "created_at": customer.created_at,
                })
        except Exception as e:
            response['error'] = True
            response['error_msg'] = str(e)
        return Response(response)
