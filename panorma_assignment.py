import streamlit as st
st.title('My panorma project')

import cv2
import os
from PIL import Image

uploaded_file1 = st.file_uploader("",key="image1", type=["png", "jpg", "jpeg"], label_visibility="hidden")

# Check if an image file is uploaded
if uploaded_file1 is not None:
    file_details = {"File Name":uploaded_file1.name, "Size":uploaded_file1.size}
    st.write(file_details)
    with open(os.path.join("content",uploaded_file1.name),"wb") as f:
        f.write(uploaded_file1.getbuffer())


uploaded_file2 = st.file_uploader("",key="image2" ,type=["png", "jpg", "jpeg"], label_visibility="hidden")

# Check if an image file is uploaded
if uploaded_file2 is not None:
    file_details = {"File Name":uploaded_file2.name, "Size":uploaded_file2.size}
    st.write(file_details)
    with open(os.path.join("content",uploaded_file2.name),"wb") as f:
        f.write(uploaded_file2.getbuffer())
    imgs=[]
    image_paths = [os.path.join("content",uploaded_file1.name),os.path.join("content",uploaded_file2.name)]
    for i in range(len(image_paths)):
        imgs.append(cv2.imread(image_paths[i]))
        imgs[i]=cv2.resize(imgs[i],(0,0),fx=0.4,fy=0.4)

    # showing the original pictures
    st.image(os.path.join("content",uploaded_file1.name))
    st.image(os.path.join("content",uploaded_file2.name))


    stitchy=cv2.Stitcher.create()
    (dummy,output)=stitchy.stitch(imgs)

    if dummy != cv2.STITCHER_OK:
        st.write("stitching ain't successful")
    else:
        st.write('Your Panorama is ready!!!')

# final output
    cv2.imwrite("content/output.jpeg",output)
    st.image(os.path.join("content","output.jpeg"))




