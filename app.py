

import streamlit as st
import os
import mimetypes
import shutil
import re



uploaded_file = st.file_uploader("Upload File")

if uploaded_file:
	st.markdown(f"streamlit file type: {uploaded_file.type}")

	mime_type, _ = mimetypes.guess_type(uploaded_file.name)

	st.markdown(f"mimetypes: {mime_type}")
