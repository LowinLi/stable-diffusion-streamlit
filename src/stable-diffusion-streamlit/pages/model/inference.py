from diffusers import StableDiffusionOnnxPipeline, StableDiffusionPipeline
import os
import json

root = os.getcwd()

if root[-3:] == "src":
    model_dir = os.path.join(root, "pages/model/onnx")
    result_dir = os.path.join(root, "pages/model/result")
else:
    model_dir = os.path.join(root, "onnx")
    result_dir = os.path.join(root, "result")

global quant_pipe

quant_pipe = StableDiffusionOnnxPipeline.from_pretrained(
    model_dir, provider="CPUExecutionProvider", local_files_only=True
)
# quant_pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", local_files_only=True)


def inference(uid, **args):
    image = quant_pipe(**args)["sample"][0]
    target = os.path.join(result_dir, uid)
    os.makedirs(target, exist_ok=True)
    image.save(os.path.join(target, "image.png"))
    with open(os.path.join(target, "config.json"), "w") as f:
        json.dump(args, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    inference(
        uid="test",
        prompt="Michael Jordan kill the game in the final 7 by a crossover shot",
        num_inference_steps=4,
    )
