from PIL import Image

def encrypt_image(image_path, output_path):
    img = Image.open(image_path)
    img = img.convert('RGB')  # Ensure image is in RGB mode to prevent errors with RGBA images
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = (r ^ 123, g ^ 123, b ^ 123)

    img.save(output_path)
    print(f"Image saved to {output_path}!")

def decrypt_image(image_path, output_path):
    encrypt_image(image_path, output_path)  # XOR again = original

print("===== Image Encryption Program =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1/2): ")

if choice == '1':
    img_path = input("Enter the image file name/path to encrypt (e.g., input.jpg): ")
    encrypt_image(img_path, "encrypted.png")
elif choice == '2':
    img_path = input("Enter the image file name/path to decrypt (e.g., encrypted.png): ")
    decrypt_image(img_path, "decrypted.png")
else:
    print("Invalid choice!")