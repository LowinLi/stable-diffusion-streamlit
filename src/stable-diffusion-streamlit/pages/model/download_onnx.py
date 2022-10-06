import os
from diffusers import StableDiffusionOnnxPipeline


def download_save():
    token = os.environ.get("HUGGINGFACE_TOKEN")

    pipe = StableDiffusionOnnxPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        revision="onnx",
        provider="CPUExecutionProvider",
        use_auth_token=token,
    )
    for tmp_dir in ["safety_checker", "text_encoder", "unet", "vae_decoder"]:
        os.makedirs(os.path.join("./onnx", tmp_dir), exist_ok=True)
        with open(os.path.join("./onnx", tmp_dir, "model.onnx"), "wb") as f:
            f.write(b"")
    pipe.save_pretrained("./onnx")


if __name__ == "__main__":
    download_save()
