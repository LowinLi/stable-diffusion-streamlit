import streamlit as st
import os
import json

tab1, tab2 = st.tabs(["文字转图片"])

with tab1:
    list_uid = os.listdir("pages/model/result/text2image")
    list_uid = sorted(list_uid, reverse=True)

    for uid in list_uid:
        try:
            with open(
                os.path.join("pages/model/result/text2image", uid, "config.json"), "r"
            ) as f:
                config = json.load(f)

            with st.container():
                st.caption(uid)
                st.image(
                    f"pages/model/result/text2image/{uid}/image.png",
                    caption=str(config["text_prompt"]),
                )
                st.json(config, expanded=False)
            st.markdown("---")
        except:
            pass
