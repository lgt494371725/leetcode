import hashlib

m=hashlib.md5()
m.update("hello world!".encode("utf-8"))
print(m.hexdigest())
