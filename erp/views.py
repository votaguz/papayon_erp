from erp.models import PurchaseOrderEntity, ContactProvider
from django_decorators.decorators import json_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@json_response
def login_service(request):
    data = {}
    email = request.POST.get('email', None)
    password = request.POST.get('password', None)
    print email, password

    try:
        contact = ContactProvider.objects.get(email=email, password=password)
        data['success'] = True
        data['user'] = contact.to_json_dict()
        #Metemos en la sesion el usuario logueado
        request.session['logged_user'] = data['user']

    except Exception, e:
        data['success'] = False
        data['user'] = None
    return data

@csrf_exempt
@json_response
def logout(request):
    request.session['logged_user'] = None
    return {'success': True}


@csrf_exempt
@json_response
def list_purchase_orders(request):
    user = request.session.get('logged_user', '')
    if user:
        data = {}
        provider_id = user['provider_id']
        data['orders'] = [p.to_json() for p in PurchaseOrderEntity.objects.filter(provider=provider_id)]
        data['success'] = True
        data['user'] = user
        return data
    else:
        return {'success': False, 'user': None, 'orders': None}


@csrf_exempt
@json_response
def update_status_purchase_order(request):
    data = {}

    order_id = request.POST.get('order_id', None)
    status = request.POST.get('status', None)
    try:
        purchase_order = PurchaseOrderEntity.objects.get(id=order_id)
        purchase_order.status = status
        purchase_order.save()
        data['success'] = True
    except:
        data['success'] = False

    return data
