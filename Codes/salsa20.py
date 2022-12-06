from Crypto.Cipher import Salsa20

c = """
CRE7YL2BDD24LV5FFGE47
76QMV7PCTRPRSPOSOFGZ
AY3COMSINODX5X2BA3DJ5
B56MPWEPTKXFHP74RLQF
44GV4EWAKCGG5JQTGNLJ3
"""
secret = b'17c872fdaeb368a66d7ce782419e375077f70ce972fc14c455b65b98745da22f'
msg_nonce = 'CALOSOMA'
cipher = Salsa20.new(key=secret, nonce=msg_nonce)
message = cipher.decrypt(c)

print(message)