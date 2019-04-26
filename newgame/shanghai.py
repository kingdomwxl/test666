import requests
client=requests.session()
url="http://www.shwzoo.com/tools/submit_ajax.ashx?action=user_login"
loginData={'txtUserName':'315835895@qq.com','txtPassword':123456}
abc=client.post(url,loginData)
print(abc.text)


