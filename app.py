import numpy as np
import os
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.transform import resize
import streamlit as st
import pickle
from PIL import Image
st.title('Image Classifier Using Machine Learning')
st.text('Upload the Image')
model=pickle.load(open('img_model.p','rb'))
uploaded_file= st.file_uploader("Choose an image...", type="jpeg")
if uploaded_file is not None:
    img= Image.open(uploaded_file)
    st.image(img,caption='Uploaded Image')
if st.button('Predict'):
    CATEGORIES= ['pretty sunflower','rugby ball leather','ice cream cone']
    st.write('Result')
    flat_data=[]
    img=np.array(img)
    img_resized=resize(img,(150,150,3))
    flat_data.append(img_resized.flatten())
    flat_data=np.array(flat_data)
    plt.imshow(img_resized)
    y_out=model.predict(flat_data)
    y_out=CATEGORIES[y_out[0]]
    st.title(f'PREDICTED OUTPUT :{y_out}')
    q=model.predict_proba(flat_data)
    for index,item in enumerate(CATEGORIES):
        st.write(f'{item}:{q[0][index]*100}')
    
