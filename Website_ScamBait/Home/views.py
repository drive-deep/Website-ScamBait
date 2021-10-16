from django.shortcuts import render
from django.http import HttpResponse
from .models import scam

# Create your views here.
def Home(request):
    res = request.GET
    input_data = res.get('input_data')

    if input_data:
        data = scam.objects.get(phone=input_data)
        if data:
            return_val = {
                "upi_id": data.upi_id,
                "accont_no": data.account_no,
                "mobile_no": data.phone
            }
            
            return HttpResponse(str(return_val))
    else:
        return HttpResponse('No data available')

    if res.get('upi_id'):
        account_no = res.get('account_no')
        inlineRadioOptions = res.get('inlineRadioOptions')
        online = res.get('online')
        offline = res.get('offline')
        phone = res.get('phone')
        upi_id = res.get('upi_id')

        obj = scam()

        obj.account_no = account_no
        obj.inlineRadioOptions = inlineRadioOptions
        if online:
            obj.online = online
        if offline:
            obj.offline = offline
        obj.phone = phone
        obj.upi_id = upi_id

        obj.save()
        return HttpResponse('data saved successfully')

    return render(request, 'index.html')




