import threading
import copy
from diffusers import StableDiffusionOnnxPipeline, StableDiffusionPipeline


class PipelineThread(threading.Thread):
    def __init__(self, func, args=()):
        super(PipelineThread, self).__init__()
        self.func = StableDiffusionOnnxPipeline(
            func.vae_decoder,
            func.text_encoder,
            func.tokenizer,
            func.unet,
            copy.deepcopy(func.scheduler),
            func.safety_checker,
            func.feature_extractor,
        )
        self.args = args

    def run(self):
        self.result = self.func(*self.args)

    def get_result(self):
        try:
            return self.result
        except Exception:
            return None
