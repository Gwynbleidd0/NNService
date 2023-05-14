import json
import pathlib

from datacontracts.NNKernelConfiguration import NNKernelConfiguration


class ConfigProvider:
    def __init__(self, config_path: pathlib.Path = None) -> None:
        if config_path is None:
            with open("kernel_config.json") as f:
                config = json.load(f)
        else:
            with open(config_path) as f:
                config = json.load(f)
        if config.get("temp_folder") is not None:
            self.temp_folder = config.get("temp_folder")
        else:
            raise Exception("Not found some configuration fields: temp_folder")
        self.NNKernels = []
        if config.get("NNKernels") is not None:
            for i in config.get("NNKernels"):
                try:
                    new_kernel = NNKernelConfiguration(title=i["title"], type=i["type"], ip=i["ip"], port=i["port"])
                    self.NNKernels.append(new_kernel)
                except:
                    pass
                    # Добавить логирование ошибки
