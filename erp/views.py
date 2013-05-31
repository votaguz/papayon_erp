import string
import random

from erp.models import PurchaseOrderEntity, ContactProvider
from django_decorators.decorators import json_response, add_http_var
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

def session_token_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

@csrf_exempt
@json_response
def login_service(request):
    data = {}
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    print email, password

    try:
        contact = ContactProvider.objects.get(email=email, password=password)
        contact.session_token = session_token_generator()
        contact.save()

        data['success'] = True
        data['user'] = contact.to_json_dict()
        data['session_token'] = contact.session_token
    except Exception, e:
        data['success'] = False
        data['user'] = None
    return data


@csrf_exempt
@json_response
@add_http_var('session_token')
def logout_service(request, session_token):
    session_token = request.POST.get('session_token', None)
    contact = get_object_or_404(ContactProvider, session_token=session_token)
    contact.session_token = ''
    contact.save()
    return {'success': True}


@csrf_exempt
@json_response
@add_http_var('session_token')
def list_purchase_orders(request, session_token):
    session_token = request.POST.get('session_token', None)
    user = get_object_or_404(ContactProvider, session_token=session_token)

    if user:
        data = {}
        provider_id = user.provider.id
        data['orders'] = [p.to_json() for p in PurchaseOrderEntity.objects.filter(provider=provider_id)]
        data['success'] = True
        data['user'] = user.to_json_dict()
        data['provider'] = user.provider.to_json_dict()
        return data
    else:
        return {'success': False, 'user': None, 'orders': None}


@csrf_exempt
@json_response
@add_http_var('session_token')
def update_status_purchase_order(request, session_token):
    data = {}
    session_token = request.POST.get('session_token', None)
    user = get_object_or_404(ContactProvider, session_token=session_token)
    order_id = request.POST.get('order_id', None)
    status = request.POST.get('status', None)

    try:
        purchase_order = PurchaseOrderEntity.objects.get(id=order_id)
        purchase_order.status = status
        purchase_order.modified_by = user
        purchase_order.save()
        data['success'] = True
    except Exception, e:
        data['success'] = False
        data['errors'] = e.message
    return data
