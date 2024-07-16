from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,JsonResponse
import json
from .models import MpesaCB
#--
from django_daraja.mpesa.core import MpesaClient
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def welcome(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def show(request):
    template = loader.get_template('show.html')
    records = MpesaCB.objects.all()
    context = {
        'records':records,
    }
    return HttpResponse(template.render(context,request))

def initiate_payment(request):
    phone_number = '0113509132'
    amount = 1
    account_reference = 'ref101'
    transaction_desc = 'descp'
    callback_url = 'https://mpesa-eight.vercel.app/callback/'

    cl = MpesaClient()
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)

    return HttpResponse(response)

@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            print('Callback data received:', data)
            MpesaCB.objects.create(data=data)
            # Process the data
            # For example, save the data to the database or trigger some other action
            return JsonResponse({'status': 'success'}, status=200)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {str(e)}")
            return JsonResponse({'error': f'Invalid JSON: {str(e)}'}, status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({'error': f'Unexpected error: {str(e)}'}, status=500)
