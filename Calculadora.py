from cryptography.fernet import Fernet

def generate_key():
    """Gera uma chave e a salva em um arquivo"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    """Carrega a chave do arquivo"""
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """Criptografa uma mensagem"""
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    """Descriptografa uma mensagem"""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

# Gerar chave (executar apenas uma vez)
# generate_key()

# Mensagem para criptografar
message = "Olá, mundo!"
encrypted = encrypt_message(message)
print(f"Mensagem criptografada: {encrypted}")

# Descriptografar mensagem
decrypted = decrypt_message(encrypted)
print(f"Mensagem descriptografada: {decrypted}")
