import streamlit as st
import numpy as np
import time
import threading
from datetime import datetime
import json
import os
from diffusers.training_utils import set_seed

from pages.model.inference import result_dir, quant_pipe
from pages.model.thread import PipelineThread

st.set_page_config(
    page_title="文字转图片",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={},
)


st.title("扩散模型文字生成图片")
with st.form(key="my_form"):
    ce, c1, ce, c2, c3 = st.columns([0.07, 1, 0.07, 5, 0.07])
    with c1:
        st.subheader("参数配置", anchor=None)
        num_inference_steps = st.slider(
            "生成轮数(num_inference_steps)",
            min_value=5,
            max_value=100,
            value=50,
            step=1,
            label_visibility="visible",
            help="约大生成图片质量越高，但是速度越慢 \n The number of denoising steps. More denoising steps usually lead to a higher quality image at the expense of slower inference.",
        )
        guidance_scale = st.slider(
            "指导参数(guidance_scale)",
            min_value=0.0,
            max_value=30.0,
            value=7.0,
            step=0.1,
            help="值越大，约接近输入文字 \n Defined in https://arxiv.org/abs/2207.12598 \n Guidance scale is enabled by setting `guidance_scale > 1`. Higher guidance scale encourages to generate images that are closely linked to the text `prompt`, usually at the expense of lower image quality.",
            label_visibility="visible",
        )
        height = st.slider(
            "高度像素(height)",
            min_value=64,
            max_value=1024,
            value=512,
            step=8,
            label_visibility="visible",
        )
        width = st.slider(
            "宽度像素(width)",
            min_value=64,
            max_value=1024,
            value=512,
            step=8,
            label_visibility="visible",
        )
        eta = st.slider(
            "eta (η)",
            min_value=0.0,
            max_value=5.0,
            value=0.0,
            step=0.1,
            help="Corresponds to parameter eta (η) in the DDIM paper: https://arxiv.org/abs/2010.02502",
            label_visibility="visible",
        )
        seed = st.slider(
            "种子(seed)",
            min_value=0,
            max_value=1024,
            value=10,
            step=1,
            label_visibility="visible",
            help="配置不同种子可以生成不同的图片",
        )

    with c2:
        text_prompt = st.text_area(
            "输入提示文字",
            value="",
            help="The prompt or prompts to guide the image generation",
            disabled=False,
            label_visibility="visible",
        )
        negative_prompt = st.text_area(
            "输入不要生成的文字描述，不填为不使用",
            value="",
            help="The prompt or prompts not to guide the image generation. Ignored when not using guidance (i.e., ignored if `guidance_scale` is less than `1`).",
            disabled=False,
            label_visibility="visible",
        )
        negative_prompt = None
        submit_button = st.form_submit_button("开始生成", help=None, args=None, kwargs=None)
        my_bar = st.progress(0)
        if not submit_button:
            st.stop()
        set_seed(seed)
        uid = datetime.now().strftime("%Y%m%d_%H:%M:%S")
        args = (
            text_prompt,
            height,
            width,
            num_inference_steps,
            guidance_scale,
            negative_prompt,
            eta
        )
        t = PipelineThread(func=quant_pipe, args=args)
        t.start()
        while True:
            time.sleep(1)
            if isinstance(t.func.scheduler.counter, int):
                counter = t.func.scheduler.counter
            else:
                counter = 0
            progress = min(
                t.func.scheduler.counter / (num_inference_steps + 1),
                1.0,
            )
            my_bar.progress(progress)
            if progress >= 1:
                break
        t.join()

        image_filename = os.path.join(result_dir, "text2image", uid, "image.png")
        json_filename = os.path.join(result_dir, "text2image", uid, "config.json")
        os.makedirs(os.path.join(result_dir, "text2image", uid), exist_ok=True)
        t.get_result().images[0].save(image_filename)
        with open(json_filename, "w") as f:
            config = {
                "text_prompt": text_prompt,
                "height": height,
                "width": width,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "eta": eta,
                "seed": seed,
            }
            json.dump(config, f, indent=4, ensure_ascii=False)
        st.balloons()
        st.image(
            image_filename, channels="RGB", output_format="auto", caption=text_prompt
        )
        with open(json_filename, "r") as f:
            st.json(json.load(f), expanded=True)
