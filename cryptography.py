from cryptography.fernet import Fernet

def generate_key():
    """Gera uma chave e a salva em um arquivo."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva como 'secret.key'")
    return key

def load_key():
    """Carrega a chave do arquivo 'secret.key'."""
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """Criptografa uma mensagem usando a chave."""
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    """Descriptografa uma mensagem usando a chave."""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def main():
    # Se você ainda não tem uma chave, descomente a linha abaixo para gerar uma nova chave
    # generate_key()

    # Mensagem para criptografar
    message = input("Digite a frase que deseja criptografar: ")
    
    # Criptografar mensagem
    encrypted = encrypt_message(message)
    print(f"Mensagem criptografada: {encrypted.decode()}")

    # Descriptografar mensagem
    decrypted = decrypt_message(encrypted)
    print(f"Mensagem descriptografada: {decrypted}")

if __name__ == "__main__":
    main()
