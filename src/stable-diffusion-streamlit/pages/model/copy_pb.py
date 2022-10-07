import os
import shutil


def copy_weights():
    for (root, _, file_list) in os.walk(
        os.path.join(
            os.environ["HOME"],
            ".cache/huggingface/diffusers/models--CompVis--stable-diffusion-v1-4",
        )
    ):
        if "weights.pb" in file_list:
            shutil.copyfile(os.path.join(root, "weights.pb"), "./onnx/unet/weights.pb")


if __name__ == "__main__":
    copy_weights()
