import requests
abc=requests.session()
loginUrl="https://www.cangqionglongqi.com/login.php?do=submit&action=login&usecookie=1&jumpurl="
loginData={'username':'468464654','password':'123456'}
resp=abc.post(loginUrl,loginData,verify=False)
print(resp.text)

cartUrl="https://www.cangqionglongqi.com/modules/article/addbookcase.php?bid=8172&ajax_request=1"
resp=abc.get(cartUrl,verify=False)
print(resp.text)

remUrl="https://www.cangqionglongqi.com/modules/article/bookcase.php?uid=35456&delid=216855"
resp=abc.get(remUrl,verify=False)
print(resp.text)