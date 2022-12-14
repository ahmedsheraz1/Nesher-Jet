Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'Nesher Jet')
m.hexdigest()
'7491c5723ad74007f1da6fb2ec2896f5cd2ad54c7d59b80dbfcb570abfce7e58'
