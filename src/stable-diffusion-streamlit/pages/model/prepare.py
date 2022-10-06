from copy_pb import copy_weights
from download_onnx import download_save
from quantization import quant
import shutil

if __name__ == "__main__":
    shutil.rmtree("./onnx", ignore_errors=True)
    download_save()
    copy_weights()
    quant()
