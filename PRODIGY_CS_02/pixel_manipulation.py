from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key, output_path):
    try:
        
        if not os.path.exists(image_path):
            print(f"Error: The input image path '{image_path}' does not exist.")
            return
                
        image = Image.open(image_path)
        image_array = np.array(image)        
        key = 200       
        encrypted_array = (image_array + key) % 255        
        encrypted_image = Image.fromarray(np.uint8(encrypted_array))
        
        encrypted_image.save(output_path)
        print(f"Image encrypted and saved as '{output_path}'.")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")

if __name__ == "__main__":
    key=50 
    input_image_path = r'C:\Users\user\Desktop\Prodigy intern\PRODIGY_CS_02\Image.png' 
    encrypted_image_path = r'C:\Users\user\Desktop\Prodigy intern\PRODIGY_CS_02\manipulated_image.png'         
    encrypt_image(input_image_path, key, encrypted_image_path)

    