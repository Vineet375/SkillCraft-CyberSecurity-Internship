def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            shift_amount = shift % 26

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            result += chr((ord(char) - base + shift_amount) % 26 + base)

        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== Caesar Cipher Program =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == '1':
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == '2':
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice!")