import streamlit as st
import pytesseract
from PIL import Image
import openai

openai.api_key = "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"

# Set page title
st.set_page_config(page_title='OCR App')

# Set up sidebar
st.title('OCR App')


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Add file uploader
uploaded_file = st.file_uploader('Upload an image', type=['png', 'jpg', 'jpeg'])

# Add OCR button
if st.button('Perform OCR'):

  # Check if file has been uploaded
  if uploaded_file is not None:
    with st.spinner("Extracting OCR..."):
    # Load image
      image = Image.open(uploaded_file)
      st.image(image)
      # Perform OCR using PyTesseract
      text = pytesseract.image_to_string(image)

      st.subheader("OCR Text")
      # Display OCR results
      with st.expander("See OCR Results"):
        st.write(text)

      #define the prompt
      ocr_text = text

      prompt= f"""Extract entities and their values from the provided text as a key-value pair, and separate them by a new line.
Text:{ocr_text} 
Entities:"""

      #Get The Response
      response= openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    entities = response['choices'][0]['text']
    

    st.subheader("Entities")
    with st.expander("See Extracted Entities"):
      st.code(entities)


  else:
    st.warning('Please upload an image first.')
