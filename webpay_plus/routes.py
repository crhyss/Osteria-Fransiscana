from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
import datetime as dt
from transbank.error.transbank_error import TransbankError
from transbank.webpay.webpay_plus.transaction import Transaction
from transbank.common.options import WebpayOptions
from transbank.common.integration_commerce_codes import IntegrationCommerceCodes
from transbank.common.integration_api_keys import IntegrationApiKeys
from web.models import Carrito,Seleccion,Venta 
import random


def webpay_plus_create(request):
    print(request.POST)
    print("Webpay Plus Transaction.create")
    amount = request.POST.get('amount')
    tipoventa = str(request.POST.get('tipoventa'))
    buy_order = str(random.randrange(1, 1000))+'-'+tipoventa
    session_id = request.session.session_key
    return_url = request.build_absolute_uri(location='commit-pay/')
    print('buy_order: {0}'.format(buy_order))
    print('session_id: {0}'.format(session_id))
    print('amount: {0}'.format(amount))
    print('return_url: {0}'.format(return_url))
    print('request.headers: {0}'.format(request.headers))

    tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY))
    response = tx.create(buy_order, session_id, amount, return_url)
    print('response: {0}'.format(response))

    return render(request, 'webpay/send-pay.html', {'response': response, 'amount': amount,'tipoventa':tipoventa}) 

@csrf_exempt
def commitpay(request):
    print('commitpay')
    print('request: ', request.POST)
    token = request.GET.get('token_ws')
    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESSION = request.POST.get('TBK_ID_SESSION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')
    if request.user.is_authenticated:
        carrito = Carrito.llamar_carrito(request.user.id_user)
        listar= (Seleccion.objects.filter(id_carrito = carrito.id_carrito).select_related('id_prod').values('id_seleccion','cantidad','id_prod__id_producto','id_prod__prod_nombre','id_prod__prod_imagen','id_prod__prod_precio_of','id_prod__id_producto')) 
    else:
        carrito = None
        listar = None    
    #TRANSACCIÓN REALIZADA
    if TBK_TOKEN is None and TBK_ID_SESSION is None  and TBK_ORDEN_COMPRA is None and token is not None:
        #APROBAR TRANSACCION
        tx = Transaction(WebpayOptions(IntegrationCommerceCodes.WEBPAY_PLUS, IntegrationApiKeys.WEBPAY))
        response = tx.commit(token=token)
        status = response.get('status')
        buy_order = str(response.get('buy_order'))
        session_id = response.get('session_id')
        print('id_venta:'+buy_order)
        tipoventa = int(buy_order[-1])
        print('status: ', status)
        response_code = response.get('response_code')
        print('response_code: ', response_code)
        #TRANSACCIÓN APROBADA
        if status == 'AUTHORIZED' and response_code == 0:
            state = ''
            if response.get('status') == 'AUTHORIZED':
                state = 'Aceptado'
            pay_type = ''
            if response.get('payment_type_code') == 'VD':
                pay_type = 'Tarjeta de Débito'
            amount = int(response.get('amount'))
            amount2 = amount
            amount = f'{amount:,.0f}'.replace(',', '.')
            carrito = Carrito.eliminar_carrrito(id_carrito = carrito.id_carrito)
            transaction_date = dt.datetime.strptime(response.get('transaction_date'), '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H%M:%S}'.format(transaction_date)
            venta =  Venta.venta_retiro(bruto = amount2,date =transaction_date,vta_tipo_id = tipoventa)
            transaction_detail = {
                'card_number': response.get('card_detail').get('card_number'),
                'transaction_date': transaction_date,
                'state': state,
                'pay_type': pay_type,
                'amount': amount,
                'authorization_code': response.get('authorization_code'),
                'buy_order': response.get('buy_order'),
                'carrito':carrito,
                'listar':listar  , 
                'venta':venta,             
            }
            #crear una venta, tranformar carrito pedido asociado a la venta
            return render(request, 'carrito/confirmacion-retiro.html',transaction_detail)
        else:
            transaction_detail = {
                'carrito':carrito,
                'listar':listar  ,          
            }
            return render(request,'carrito/pago-rechazado.html',transaction_detail)
    else:
        transaction_detail = {
            'carrito':carrito,
            'listar':listar  ,            
        }                             
        return render(request,'carrito/pagofallido.html',transaction_detail)
