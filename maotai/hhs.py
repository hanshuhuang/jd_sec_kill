import requests
from jd_logger import logger

def go_shenzhen():
  url = "https://marathon.jd.com/seckillnew/orderService/submitOrder.action?skuId=100012043978"

  payload='num=1&addressId=7113054388&name=%E9%BB%84%E6%B1%89%E6%9E%A2&provinceId=19&provinceName=%E5%B9%BF%E4%B8%9C&cityId=1655&cityName=%E4%B8%9C%E8%8E%9E%E5%B8%82&countyId=3105&countyName=%E4%BC%81%E7%9F%B3%E9%95%87&townId=0&townName=&addressDetail=%E6%B9%96%E6%BB%A8%E5%8C%97%E8%B7%AF%E4%B8%80%E4%B9%9D%E4%B8%89%E5%8F%B7%E5%B9%BF%E8%A3%95%E9%80%9A%E5%85%AC%E4%BA%A4%E7%AB%99&mobile=136****7481&mobileKey=cf346e00cb7a90d9850aa6b61731a0e6&invoiceTitle=4&invoiceContent=1&invoicePhone=180****6583&invoicePhoneKey=8e603d606af69d0b8abc0d5d3825da3e&invoice=true&password=&codTimeType=3&paymentType=4&overseas=0&phone=&areaCode=&token=b1a396babb0a6099dca7b1b4e71874ed&sk=PZKNXMGGGBthgfb5rwe&skuId=100012043978'
  headers = {
    'Host': 'marathon.jd.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://marathon.jd.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '__jd_ref_cls=MSecKillBalance_Order_Submit; mba_muid=16622559079581160868085.194.1663214424556; mba_sid=194.34; __jda=237926171.16622559079581160868085.1662255907.1663128002.1663214404.11; __jdb=237926171.5.16622559079581160868085|11.1663214404; __jdc=237926171; __jdv=237926171%7Ckong%7Ct_1000170136%7Ctuiguang%7Cnotset%7C1663127891653; pre_seq=16; pre_session=40293b5da3c185c7cb359342fbc028b286f024b5|363; unpl=JF8EAPFnNSttWE4AUhIHGRIXTQoEW1sOSEQEPGcEAA9aTlQBTgAdEEJ7XlVdXhRKER9sYBRUX1NPUA4ZAysiEEpcVFpYC0gRAl9XQBcNCh9IBR8AHxEXS1tSXl8NSxELZ2IGUUFbS1UDGQIYEhFNX1RuXgh7FjNvYAFXVV1OVgEeAx8UEEteUF5cCUsQAV9XBVxZaE5QBx4DHBUQTlxQbl4JSxIGb2YEUVs2TlQEGgcYFBRKXjpcXAlJEARpbg1XbVhCVAcTAxoSF0htVW5cOAp5A25nBVBUX0wZBRwGGBoVTl9QW1wMTRcDbGMFVVxYTFY1GjIY; mid=R-OIEWd2RycLA0HfVHIdJ_DX8M8DMyUQ66DJePzk3jY; seckill100012043978=6BmI3VMuNqSLbkZyghszsDretbFmCvxp/eiIAnIIYYHoBdD40i2uhhCu3dQFoh9w9eTL7lOG7f+QK7UVaSyHR3BTUPZlNAvmmntPTYRZDFbzJwu8da8N5cT6BKZNvfYAmS8hO0MdgORRVcM8VPDG3QD7gGwm2J4xXAnX4Ysi6+57pZsuumfr6MuU1bfbtmy4B3fayQskUaFbzGNg; seckillSid=; seckillSku=100012043978; pt_key=app_openAAJjIVFMADALppP4S6fPKClla0IIOuc9VVp09YYLDAQ7vYrQTG1jpVCSfeD7Cc87zy4jl1u2Cfo; pt_pin=A154630877; pwdt_id=A154630877; sid=850b2910c30ba17b42b94aecf62cf30w; shshshfpb=xf7YCAtQtkJLNzPUOUmBKPg; joyya=1662784375.0.21.15e17gh; shshshfpv=JD0111d47dFRX2xq0mAo1662784328975050sm9H1jYp5S4YPTUJkV1RbzeMhE0MJCvqVRA-CYdPnpb2k0IfGzi19-SEvtua31xddTjG5Hr82P-KW4CZQKEdLtAcTNgB0w1ia_xgx_rKmY1ae9jr4~fHpJ/yx18MVVHLOR6xrCwQPev8N+bKQwLWFHJdCrWjxuCfcHrWniW9aKmMsEx4+zJCcLXsvyvlirYX5vl2rhojw==; 3AB9D23F7A4B3C9B=PFWHFAHLNNZVAMO3LXN5D2CPHSCD6D3EBISFIU6YNXQDPVEZOCJUAHUFAOB5Q7FSACVMYRACLIKKKO46HH76QJFNDM; BATQW722QTLYVCRD={"tk":"jdd01POXEV43JAWD36ZK5U7ERHJO65RQKIIBOYF6F3DC7K752OMPI2RBEKB7WAZLY4N27UPMMVAZ7NBCNOQLHOY5RMND25FR54J5MHX6XRKY01234567","t":1662781165228}; _gia_s_e_joint={"eid":"PFWHFAHLNNZVAMO3LXN5D2CPHSCD6D3EBISFIU6YNXQDPVEZOCJUAHUFAOB5Q7FSACVMYRACLIKKKO46HH76QJFNDM","ma":"","im":"","os":"iOS","osv":"","ip":"113.78.115.243","apid":"jdapp","ia":"","uu":"","cv":"11.2.5","nt":"UNKNOW","at":"1"}; _gia_s_local_fingerprint=668baa23d440bccdac390a1c9b3c3ae4; ipLoc-djd=19_1655_3105_0; __jdu=16622559079581160868085; visitkey=11120535259060949',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'jdapp;iPhone;11.2.5;;;M/5.0;appBuild/168271;jdSupportDarkMode/0;ef/1;ep/%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22ud%22%3A%22DNKyEJDsDWHrC2CnENVtD2DsCzU5CzGyZwTtCNS4YtS4DwYmCtHsDG%3D%3D%22%2C%22sv%22%3A%22CJUkDs4n%22%2C%22iad%22%3A%22CNO2COG4HUSjDuO2Cy00DzDOBJq5DuYjGtdOHJKmCzG1DzC4%22%7D%2C%22ts%22%3A1663214420%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D;Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;',
    'Referer': 'https://marathon.jd.com/seckillM/seckill.action?skuId=100012043978&num=1&rid=1663214423',
    'Content-Length': '711',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  logger.info(response.text)


def go_qishi():
  url = "https://marathon.jd.com/seckillnew/orderService/submitOrder.action?skuId=100012043978"

  payload='num=1&addressId=7113054388&name=%E9%BB%84%E6%B1%89%E6%9E%A2&provinceId=19&provinceName=%E5%B9%BF%E4%B8%9C&cityId=1655&cityName=%E4%B8%9C%E8%8E%9E%E5%B8%82&countyId=3105&countyName=%E4%BC%81%E7%9F%B3%E9%95%87&townId=0&townName=&addressDetail=%E6%B9%96%E6%BB%A8%E5%8C%97%E8%B7%AF%E4%B8%80%E4%B9%9D%E4%B8%89%E5%8F%B7%E5%B9%BF%E8%A3%95%E9%80%9A%E5%85%AC%E4%BA%A4%E7%AB%99&mobile=136****7481&mobileKey=cf346e00cb7a90d9850aa6b61731a0e6&invoiceTitle=4&invoiceContent=1&invoicePhone=180****6583&invoicePhoneKey=8e603d606af69d0b8abc0d5d3825da3e&invoice=true&password=&codTimeType=3&paymentType=4&overseas=0&phone=&areaCode=&token=b1a396babb0a6099dca7b1b4e71874ed&sk=PZKNXMGGGBthgfb5rwe&skuId=100012043978'
  headers = {
    'Host': 'marathon.jd.com',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://marathon.jd.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Cookie': '__jd_ref_cls=MSecKillBalance_Order_Submit; mba_muid=16622559079581160868085.194.1663214424556; mba_sid=194.34; __jda=237926171.16622559079581160868085.1662255907.1663128002.1663214404.11; __jdb=237926171.5.16622559079581160868085|11.1663214404; __jdc=237926171; __jdv=237926171%7Ckong%7Ct_1000170136%7Ctuiguang%7Cnotset%7C1663127891653; pre_seq=16; pre_session=40293b5da3c185c7cb359342fbc028b286f024b5|363; unpl=JF8EAPFnNSttWE4AUhIHGRIXTQoEW1sOSEQEPGcEAA9aTlQBTgAdEEJ7XlVdXhRKER9sYBRUX1NPUA4ZAysiEEpcVFpYC0gRAl9XQBcNCh9IBR8AHxEXS1tSXl8NSxELZ2IGUUFbS1UDGQIYEhFNX1RuXgh7FjNvYAFXVV1OVgEeAx8UEEteUF5cCUsQAV9XBVxZaE5QBx4DHBUQTlxQbl4JSxIGb2YEUVs2TlQEGgcYFBRKXjpcXAlJEARpbg1XbVhCVAcTAxoSF0htVW5cOAp5A25nBVBUX0wZBRwGGBoVTl9QW1wMTRcDbGMFVVxYTFY1GjIY; mid=R-OIEWd2RycLA0HfVHIdJ_DX8M8DMyUQ66DJePzk3jY; seckill100012043978=6BmI3VMuNqSLbkZyghszsDretbFmCvxp/eiIAnIIYYHoBdD40i2uhhCu3dQFoh9w9eTL7lOG7f+QK7UVaSyHR3BTUPZlNAvmmntPTYRZDFbzJwu8da8N5cT6BKZNvfYAmS8hO0MdgORRVcM8VPDG3QD7gGwm2J4xXAnX4Ysi6+57pZsuumfr6MuU1bfbtmy4B3fayQskUaFbzGNg; seckillSid=; seckillSku=100012043978; pt_key=app_openAAJjIVFMADALppP4S6fPKClla0IIOuc9VVp09YYLDAQ7vYrQTG1jpVCSfeD7Cc87zy4jl1u2Cfo; pt_pin=A154630877; pwdt_id=A154630877; sid=850b2910c30ba17b42b94aecf62cf30w; shshshfpb=xf7YCAtQtkJLNzPUOUmBKPg; joyya=1662784375.0.21.15e17gh; shshshfpv=JD0111d47dFRX2xq0mAo1662784328975050sm9H1jYp5S4YPTUJkV1RbzeMhE0MJCvqVRA-CYdPnpb2k0IfGzi19-SEvtua31xddTjG5Hr82P-KW4CZQKEdLtAcTNgB0w1ia_xgx_rKmY1ae9jr4~fHpJ/yx18MVVHLOR6xrCwQPev8N+bKQwLWFHJdCrWjxuCfcHrWniW9aKmMsEx4+zJCcLXsvyvlirYX5vl2rhojw==; 3AB9D23F7A4B3C9B=PFWHFAHLNNZVAMO3LXN5D2CPHSCD6D3EBISFIU6YNXQDPVEZOCJUAHUFAOB5Q7FSACVMYRACLIKKKO46HH76QJFNDM; BATQW722QTLYVCRD={"tk":"jdd01POXEV43JAWD36ZK5U7ERHJO65RQKIIBOYF6F3DC7K752OMPI2RBEKB7WAZLY4N27UPMMVAZ7NBCNOQLHOY5RMND25FR54J5MHX6XRKY01234567","t":1662781165228}; _gia_s_e_joint={"eid":"PFWHFAHLNNZVAMO3LXN5D2CPHSCD6D3EBISFIU6YNXQDPVEZOCJUAHUFAOB5Q7FSACVMYRACLIKKKO46HH76QJFNDM","ma":"","im":"","os":"iOS","osv":"","ip":"113.78.115.243","apid":"jdapp","ia":"","uu":"","cv":"11.2.5","nt":"UNKNOW","at":"1"}; _gia_s_local_fingerprint=668baa23d440bccdac390a1c9b3c3ae4; ipLoc-djd=19_1655_3105_0; __jdu=16622559079581160868085; visitkey=11120535259060949; seckillSid=; seckillSku=100012043978',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'jdapp;iPhone;11.2.5;;;M/5.0;appBuild/168271;jdSupportDarkMode/0;ef/1;ep/%7B%22ciphertype%22%3A5%2C%22cipher%22%3A%7B%22ud%22%3A%22DNKyEJDsDWHrC2CnENVtD2DsCzU5CzGyZwTtCNS4YtS4DwYmCtHsDG%3D%3D%22%2C%22sv%22%3A%22CJUkDs4n%22%2C%22iad%22%3A%22CNO2COG4HUSjDuO2Cy00DzDOBJq5DuYjGtdOHJKmCzG1DzC4%22%7D%2C%22ts%22%3A1663214420%2C%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22version%22%3A%221.0.3%22%2C%22appname%22%3A%22com.360buy.jdmobile%22%2C%22ridx%22%3A-1%7D;Mozilla/5.0 (iPhone; CPU iPhone OS 15_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1;',
    'Referer': 'https://marathon.jd.com/seckillM/seckill.action?skuId=100012043978&num=1&rid=1663214423',
    'Content-Length': '711',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  logger.info(response.text)

if __name__ == '__main__':
  go_shenzhen()
  go_qishi()
