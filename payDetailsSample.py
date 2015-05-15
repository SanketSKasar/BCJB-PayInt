import requests
import json


url = 'https://api.razorpay.com/v1/payments/pay_3Bbbj1QyvGw24u'

resp = requests.get(url, data={}, auth=('rzp_test_EfogleCA7FR9O2', 'nrfztZ3weNdpipS3u8vZCttD'))

jsonresp = resp.json()

amount=0
for x in jsonresp:
    if jsonresp[x] :
        print(x + " : " + str(jsonresp[x]))
        if x=='amount' :
            amount=jsonresp[x]

print(amount)

url = 'https://api.razorpay.com/v1/payments/pay_3Bbbj1QyvGw24u/capture'

resp = requests.post(url, data={ 'amount':amount }, auth=('rzp_test_EfogleCA7FR9O2', 'nrfztZ3weNdpipS3u8vZCttD'))

jsonresp = resp.json()

for x in jsonresp:
    if jsonresp[x] :
        print(x + " : " + str(jsonresp[x]))


url = 'https://api.razorpay.com/v1/payments/pay_3Bbbj1QyvGw24u/refund'

resp = requests.post(url, data={ 'amount':amount }, auth=('rzp_test_EfogleCA7FR9O2', 'nrfztZ3weNdpipS3u8vZCttD'))

jsonresp = resp.json()

for x in jsonresp:
    if jsonresp[x] :
        print(x + " : " + str(jsonresp[x]))
