import pickle
import json
from abc import ABC, abstractmethod


class SerializationInterface(ABC):

    @abstractmethod
    def serialize(self, file):
        raise NotImplementedError


class SerializeToJson(SerializationInterface):

    def serialize(self, file):
        with open('json.json', 'w', encoding='utf-8') as fh:
            json.dump(file, fh)


class SerializeToBin(SerializationInterface):

    def serialize(self, file):
        with open('bin.bin', 'wb') as fh:
            pickle.dump(file, fh)


json_test = SerializeToJson()
bin_test = SerializeToBin()

json_data = {'data': 'json_test'}
bin_data = {'data': 'bin_test'}

json_test.serialize(json_data)
bin_test.serialize(bin_data)

with open('bin.bin', 'rb') as f:
    print(f'{pickle.load(f)}')
with open('json.json', 'r') as f:
    print(f'{json.load(f)}')

