import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO

# Your mappings
mapping = {
    ' ': 0, 'a': 1, 'b': 7, 'c': 13, 'd': 19, 'e': 25, 'f': 31, 'g': 37, 'h': 43,
    'i': 49, 'j': 55, 'k': 61, 'l': 67, 'm': 73, 'n': 79, 'o': 85, 'p': 91, 'q': 97,
    'r': 103, 's': 109, 't': 115, 'u': 121, 'v': 127, 'w': 133, 'x': 139, 'y': 145, 'z': 151,
    '!': 3, '.': 9, ',': 12, '?': 18, '-': 21, '_': 24, '@': 27, '#': 30, 
    '$': 33, '%': 36, '^': 39, '&': 42, '*': 45, '(': 48, ')': 51, 
    'A': 2, 'B': 8, 'C': 14, 'D': 20, 'E': 26, 'F': 32, 'G': 38, 
    'H': 44, 'I': 50, 'J': 56, 'K': 62, 'L': 68, 'M': 74, 'N': 80, 
    'O': 86, 'P': 92, 'Q': 98, 'R': 104, 'S': 110, 'T': 116, 'U': 122, 
    'V': 128, 'W': 134, 'X': 140, 'Y': 146, 'Z': 152,
    '0':5,'1':10,'2':15,'3':30,'4':35,'5':40,'6':60,'7':65,'8':70,'9':75
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
    img = Image.open(image)  # Keep the image in its original mode
    img_array = np.array(img)
    return img_array.flatten()

# Convert 1D array back to image
def array_to_image(img_1d_array, width, height):
    img_2d_array = img_1d_array.reshape((height, width, -1))  # Reshape considering the number of channels
    return Image.fromarray(img_2d_array.astype(np.uint8))

# Map text to result array
def map_text_to_result_array(text, prime_set, mapping, result):
    l=len(text)
    for i, char in enumerate(text):
        prime_index = prime_set[i]
        result[prime_index] = mapping.get(char, 0)
    result[10]=l
    return result


def encode(prime_numbers, rmapping, result):
    decoded_message = ''
    i = 0
    l=result[10]
    while i < l:
        prime_index = prime_numbers[i]
        value = result[prime_index]
        if value in rmapping:
            decoded_message += rmapping[value]
        i += 1
    
    return decoded_message
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
