import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO

# Your mappings
mapping = {
    ' ': 0, 'a': 1, 'b': 7, 'c': 13, 'd': 19, 'e': 25, 'f': 31, 'g': 37, 'h': 43,
    'i': 49, 'j': 55, 'k': 61, 'l': 67, 'm': 73, 'n': 79, 'o': 85, 'p': 91, 'q': 97,
    'r': 103, 's': 109, 't': 115, 'u': 121, 'v': 127, 'w': 133, 'x': 139, 'y': 145, 'z': 151,
    '!': 313, '.': 317, ',': 331, '?': 337, '-': 347, '_': 349, '@': 353, '#': 359, 
    '$': 367, '%': 373, '^': 379, '&': 383, '*': 389, '(': 397, ')': 401, 
    'A': 157, 'B': 163, 'C': 167, 'D': 173, 'E': 179, 'F': 181, 'G': 191, 
    'H': 193, 'I': 197, 'J': 199, 'K': 211, 'L': 223, 'M': 227, 'N': 229, 
    'O': 233, 'P': 239, 'Q': 241, 'R': 251, 'S': 257, 'T': 263, 'U': 269, 
    'V': 271, 'W': 277, 'X': 281, 'Y': 283, 'Z': 293
}

rmapping = {v: k for k, v in mapping.items()}

# Function to generate prime numbers
def sieve_of_eratosthenes(n):
    sieve = [True] * (n + 1)
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sorted(p for p in range(2, n + 1) if sieve[p])

# Generate the sorted list of primes up to 2,073,600
prime_numbers = sieve_of_eratosthenes(2073600)

# Image to 1D array
def image_to_1d_array(image):
    img = Image.open(image).convert('L')
    img_array = np.array(img)
    return img_array.flatten()

# Convert 1D array back to image
def array_to_image(img_1d_array, width, height):
    img_2d_array = img_1d_array.reshape((height, width))
    img_rgb_array = np.stack([img_2d_array] * 3, axis=-1)
    return Image.fromarray(img_rgb_array.astype(np.uint8), mode='RGB')

# Map text to result array
def map_text_to_result_array(text, prime_set, mapping, result):
    for i, char in enumerate(text):
        result[prime_set[i]] = mapping.get(char, 0)
    result[prime_set[i + 1]] = -1  # Mark the end of the message with -1
    return result

# Encode function
def encode(prime_numbers, rmapping, result):
    ans = ''
    i = 0
    
    while i < len(prime_numbers) and prime_numbers[i] < len(result) and result[prime_numbers[i]] != -1:
        ind = prime_numbers[i]
        if result[ind] in rmapping:
            ans += rmapping[result[ind]]
        else:
            break
        i += 1
    
    return ans

# Streamlit App
st.title("Image Encoder/Decoder")

# Options for Encode/Decode
option = st.selectbox("Choose an action", ["Encode", "Decode"])

if option == "Encode":
    st.header("Encode a Message into an Image")

    # Upload an image
    uploaded_image = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

    if uploaded_image is not None:
        # Display the image
        img = Image.open(uploaded_image)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Text input from user
        text = st.text_input("Enter the message to encode:")

        if st.button("Encode"):
            result = image_to_1d_array(uploaded_image)
            copyofresult = result.copy()
            copyofresult = map_text_to_result_array(text, prime_numbers, mapping, copyofresult)
            width, height = img.size
            encoded_image = array_to_image(copyofresult, width, height)

            # Display the encoded image
            st.image(encoded_image, caption="Encoded Image", use_column_width=True)

            # Provide download option
            buf = BytesIO()
            encoded_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            st.download_button(label="Download Encoded Image", data=byte_im, file_name="encoded_image.png", mime="image/png")

elif option == "Decode":
    st.header("Decode a Message from an Image")

    # Upload an encoded image
    uploaded_encoded_image = st.file_uploader("Upload an Encoded Image", type=["png", "jpg", "jpeg"])

    if uploaded_encoded_image is not None:
        # Display the image
        img = Image.open(uploaded_encoded_image)
        st.image(img, caption="Uploaded Encoded Image", use_column_width=True)

        if st.button("Decode"):
            result_array = image_to_1d_array(uploaded_encoded_image)
            decoded_message = encode(prime_numbers, rmapping, result_array)

            # Display the decoded message
            st.success(f"Decoded Message: {decoded_message}")
