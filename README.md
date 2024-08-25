<h1 align="center" id="title">ImageEncoderDecode</h1>

<p id="description">This Streamlit application allows you to encode and decode messages within images. The encoded images can be used to discreetly convey information and the messages can be retrieved later using this app.</p>

<h2>Features:</h2>

### Encode a Message:

Upload an image input a message and the app will encode the message within the image. The encoding process modifies specific areas of the image to store the message.

### Decode a Message:

Upload an image with an encoded message and the app will extract and display the hidden message. The decoding process identifies the message by examining the modified areas of the image.<h2>Flow Diagram</h2>

<img src="https://i.postimg.cc/htgd1HgT/Screenshot-2024-08-25-200517.png" alt="Streamlit App Screenshot">

<h2>How It Works:</h2>

  

### Encoding Process:

  
  
1-Upload an image.  
2-Enter the message you want to encode.  
3-The app embeds the message into the image by modifying certain pixels. The encoded image is displayed and available for download.

### Decoding Process:

1-Upload an image containing an encoded message.  
2-The app analyzes the image to retrieve the hidden message.  
3-The decoded message is displayed on the screen.

<h2>Project Screenshots:</h2>

<img src="https://i.postimg.cc/HxYkRgj1/Screenshot-2024-08-25-204246.png" alt="project-screenshot" width="500" height="400/">

<img src="https://i.postimg.cc/631J5J6Z/Screenshot-2024-08-25-204836.png" alt="project-screenshot" width="500" height="400/">

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone the repository:</p>

```
git clone https://github.com/FurkanKhann/repository.git cd repository
```

<p>2. Install the required packages:</p>

```
pip install -r Requirements.txt
```

<p>3. Run the Streamlit app:</p>

```
streamlit run main.py
```

<h2>💖Like my work?</h2>

<p>contact:khanfurkan575@gmail.com<br>LinkedIn:https://www.linkedin.com/in/furkankhan16/</p>
