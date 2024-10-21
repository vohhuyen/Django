import random
import string
import base64
import hashlib

code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
print(f"Code Verifier: {code_verifier}")

code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
print(f"Code Challenge: {code_challenge}")