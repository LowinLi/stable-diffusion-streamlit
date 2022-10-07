import os
from onnxruntime.quantization import quantize_dynamic, QuantType


def quant():
    for root, dirs, filenames in os.walk("./onnx"):
        if "model.onnx" in filenames:
            if "weights.pb" in filenames:
                external_data = True
            else:
                external_data = False
            quantize_dynamic(
                model_input=os.path.join(root, "model.onnx"),
                model_output=os.path.join(root, "model.onnx"),  # 量化后直接覆盖原onnx文件
                per_channel=True,
                reduce_range=True,
                weight_type=QuantType.QUInt8,
                optimize_model=True,
                use_external_data_format=external_data,
            )
            print("Quantized model saved at: ", os.path.join(root, "model.onnx"))
            if "weights.pb" in filenames:
                os.remove(os.path.join(root, "weights.pb"))
                print("Removed weights.pb")

if __name__ == "__main__":
    quant()
