# -*- coding: utf-8 -*-
import requests
import json
import time 
import os

# 配置开始
# user = os.environ['1905100211 qwe123 234']
user = os.environ["USER"] = '1905100211 qwe123 234'
account = user.split( )[0] # 账号
password = user.split( )[1] # 密码
school_id = user.split( )[2] # 学校ID
sign_gps = os.environ["SIGN_GPS"] = '115.997108,29.720127'  # 签到坐标（注意小数点取后6位）
longitude = sign_gps.split(",")[0] # 经度
latitude = sign_gps.split(",")[1] # 纬度
SCTKEY=os.environ["SCTKEY"] = 'SCT20612Ts491iJGdefPz7Q2nWKYV4tua'
address = os.environ["ADDRESS_NAME"]= "江西省九江市浔阳区甘棠街道塔岭南路48号"
address_detail = os.environ["ADDRESS_DETAIL"]= "江西省九江市浔阳区甘棠街道塔岭南路48号"
   
data={'account':account,#账号
      'app_id':'cn.vanber.xixunyun.saas',
      'app_version':'4.9.9',
      'key':'',
      'model':'huawei tag-tl00',
      'password':password,#密码
      'platform':'2',
      'registration_id':'1a0018970a242ca8039',
      'request_source':'3',
      'school_id':school_id,#学校代码
      'system':'5.1.1',
      'uuid':'00:81:24:d9:fc:da'}
login_header={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '258',
        'Host': 'api.xixunyun.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.8.1',

}
login_url=' https://api.xixunyun.com//login/api?from=app&version=4.9.9&platform=android&entrance_year=0&graduate_year=0'
request=requests.post(url=login_url,headers=login_header,data=data)
login_data=json.loads(request.text)#登陆成功后返回的信息
token=login_data['data']['token']
time.sleep(1)

print(login_data)
sign_url='https://api.xixunyun.com/signin_rsa?token='+token+'&from=app&version=4.9.9&platform=android&entrance_year=0&graduate_year=0 '
sign_data={'address':address_detail,#签到地址
           'address_name':address,#签到地点名称
           'change_sign_resource':'0',
           'comment':'',
           'latitude':"jzK0HoHatr7oA8IXMBXANF5yj6SuPYqb9YeQib7reAk9Q+cc5B1iMEJklVqrnExAyiIjrrI64No3zQMmqF7wX02/b4kRCATh/TwSKxlIGpt38S6li+DqSTaIMzeaNgRHXtlwaBEGKn+vZSj10+EFLjSpI4bVpE1m+HxGYCyq/wc=",
           'longitude':"p9SGGB+Ck+mysE5gxwdl9QLggG1i1Gu5xId1aaAvdQ3fldihgyfBH3obF26SlMikdM+4lGxru0cCh48q1aiSDGXbNd3GB+V9ybrGjj5PXZOF55X2aUX++c1ZTkgnWZrHCASKk7tjy7+vNxwBBs4KCZAt4BwCiRjrWDkI6fsrzsc=",
           'remark':'0',
    
    }
sign_request=requests.post(url=sign_url,data=sign_data,headers=login_header)
sign=json.loads(sign_request.text)
print(sign)
