import abc
import torch
import shutil

from batteryml.data.databundle import DataBundle


class BaseModel(abc.ABC):

    def __init__(self, workspace: str = None):
        self.workspace = workspace

    @abc.abstractmethod
    def fit(self, dataset: DataBundle, timestamp: str = None):
        

    @abc.abstractmethod
    def predict(self, dataset: DataBundle, data_type: str='test') -> torch.Tensor:


    @abc.abstractmethod
    def dump_checkpoint(self, path: str):

    @abc.abstractmethod
    def load_checkpoint(self, path: str):

    def to(self, device: str):
        return self

    def link_latest_checkpoint(self, filename: str):
        to_dump = self.workspace / 'latest.ckpt'
        shutil.copyfile(filename, to_dump)
