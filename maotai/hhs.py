import requests
from maotai.jd_logger import logger


def go_qishi():
  url = "https://marathon.jd.com/seckillnew/orderService/submitOrder.action?skuId=100012043978"

  payload='num=1&addressId=7113054388&name=%E9%BB%84%E6%B1%89%E6%9E%A2&provinceId=19&provinceName=%E5%B9%BF%E4%B8%9C&cityId=1655&cityName=%E4%B8%9C%E8%8E%9E%E5%B8%82&countyId=3105&countyName=%E4%BC%81%E7%9F%B3%E9%95%87&townId=0&townName=&addressDetail=%E6%B9%96%E6%BB%A8%E5%8C%97%E8%B7%AF%E4%B8%80%E4%B9%9D%E4%B8%89%E5%8F%B7%E5%B9%BF%E8%A3%95%E9%80%9A%E5%85%AC%E4%BA%A4%E7%AB%99&mobile=136****7481&mobileKey=cf346e00cb7a90d9850aa6b61731a0e6&invoiceTitle=4&invoiceContent=1&invoicePhone=180****6583&invoicePhoneKey=8e603d606af69d0b8abc0d5d3825da3e&invoice=true&password=&codTimeType=3&paymentType=4&overseas=0&phone=&areaCode=&token=b1a396babb0a6099dca7b1b4e71874ed&sk=q1Ted5oC716plfhmxwe&skuId=100012043978'
  headers = {
    'Host': 'marathon.jd.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://marathon.jd.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '__jd_ref_cls=MSecKillBalance_Order_Submit; mba_muid=16622559079581160868085.202.1663387226890; mba_sid=202.27; seckillSid=; seckillSku=100012043978; __jda=237926171.16622559079581160868085.1662255907.1663301699.1663387203.13; __jdb=237926171.5.16622559079581160868085|13.1663387203; __jdc=237926171; __jdv=237926171%7Ckong%7Ct_1000170136%7Ctuiguang%7Cnotset%7C1663387027782; pre_seq=11; pre_session=40293b5da3c185c7cb359342fbc028b286f024b5|378; unpl=JF8EAPFnNSttWE4AUhIHGRIXTQoEW1sOSEQEPGcEAA9aTlQBTgAdEEJ7XlVdXhRKER9sYBRUX1NPUA4ZAysiEEpcVFpYC0gRAl9XQBcNCh9IBR8AHxEXS1tSXl8NSxELZ2IGUUFbS1UDGQIYEhFNX1RuXgh7FjNvYAFXVV1OVgEeAx8UEEteUF5cCUsQAV9XBVxZaE5QBx4DHBUQTlxQbl4JSxIGb2YEUVs2TlQEGgcYFBRKXjpcXAlJEARpbg1XbVhCVAcTAxoSF0htVW5cOAp5A25nBVBUX0wZBRwGGBoVTl9QW1wMTRcDbGMFVVxYTFY1GjIY; seckill100012043978=n3P72RqYCWQu6mGsuER2cmU0AGvIY/s1Yn7jE5cJwaP+Sh/GXVw3wTLU1ZMHlNw5eEsy/Mal3GA44wONlc0mZWfnyuVU+oxWso+XcYiwmXjoRM9rMj4vCpzRYdGpnYdFL5fo480BBPXtkKOuQGVFCAnggJWCknpWlnBOpvrbIuavftCcpOYxacfZ8H+6ibEWRghr4TN6ewDM/nCj; mid=EDR9ITgR4-Gv3tRe42c8j3Tkm-010Okoat99hpyElUc; pt_key=app_openAAJjJSo_ADCqH0gqr3kiuYzFUZ4Knz2aqB6OhYKRv6vO-TfBDbYYZ_UCWZx6sba_DwUPHuNnaQg; pt_pin=A154630877; pwdt_id=A154630877; sid=5c769726d65ae0051819735ad565566w; shshshfpb=xf7YCAtQtkJLNzPUOUmBKPg; joyya=1662784375.0.21.15e17gh; shshshfpv=JD0111d47dFRX2xq0mAo1662784328975050sm9H1jYp5S4YPTUJkV1RbzeMhE0MJCvqVRA-CYdPnpb2k0IfGzi19-SEvtua31xddTjG5Hr82P-KW4CZQKEdLtAcTNgB0w1ia_xgx_rKmY1ae9jr4~fHpJ/yx18MVVHLOR6xrCwQPev8N+bKQwLWFHJdCrWjxuCfcHrWniW9aKmMsEx4+zJCcLXsvyvlirYX5vl2rhojw==; __jdu=16622559079581160868085; visitkey=11120535259060949',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'jdapp;iPhone;11.2.6;;;M/5.0;appBuild/168304;jdSupportDarkMode/0;ef/1;ep/%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22ud%22%3A%22DNKyEJDsDWHrC2CnENVtD2DsCzU5CzGyZwTtCNS4YtS4DwYmCtHsDG%3D%3D%22%2C%22sv%22%3A%22CJUkDs4n%22%2C%22iad%22%3A%22CNO2COG4HUSjDuO2Cy00DzDOBJq5DuYjGtdOHJKmCzG1DzC4%22%7D%2C%22ts%22%3A1663387219%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D;Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;',
    'Referer': 'https://marathon.jd.com/seckillM/seckill.action?skuId=100012043978&num=1&rid=1663387220',
    'Content-Length': '711',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  logger.info(response.text)

