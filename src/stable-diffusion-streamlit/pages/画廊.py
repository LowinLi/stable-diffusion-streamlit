import streamlit as st
import os
import json

# tab1 = st.tabs(["文字转图片"])

# with tab1:
result_dir = "pages/model/result/text2image"
os.makedirs(result_dir, exist_ok=True)
list_uid = os.listdir(result_dir)
list_uid = sorted(list_uid, reverse=True)

for uid in list_uid:
    try:
        with open(os.path.join(result_dir, uid, "config.json"), "r") as f:
            config = json.load(f)

        with st.container():
            st.caption(uid)
            st.image(
                os.path.join(result_dir, uid, "image.png"),
                caption=str(config["text_prompt"]),
            )
            st.json(config, expanded=False)
        st.markdown("---")
    except:
        pass
