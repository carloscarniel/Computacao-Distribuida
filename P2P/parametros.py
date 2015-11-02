import hashlib
import binascii

hasher= hashlib.sha256()
meuHash = hasher.hexdigest()
ipServer = "127.0.0.1"
portServer = 5000
ipClient = "127.0.0.1"
portClient = 5000