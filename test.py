import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="file upload", page_icon="🦈", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title('File Upload System by Haibo')

uploaded_file = st.file_uploader(" Please choose a excel file")

if uploaded_file is not None:
    # # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    try:
        dataframe = pd.read_excel(uploaded_file)
        st.write(dataframe)

        if st.button('确认'):
            my_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1)
            
            dataframe.to_excel("test.xlsx", index=False)
            st.write('上传成功')
        else:
            st.write('等待上传')
    except:
        st.write("只接受EXCEL 文件")



