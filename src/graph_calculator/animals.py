from abc import ABCMeta
from .graph import Node
from typing import Self

import pandas as pd
import yaml


class AnimalsCSV(Node):
    _name = "AnimalsCSV"
    _calculated = True

    def __init__(self, raw_data: pd.DataFrame):
        self._value = raw_data

    def dependencies(self) -> tuple[ABCMeta]:
        return tuple()

    def calculate(self, *args):
        pass

    @staticmethod
    def from_file(file_name: str) -> Self:
        print("Loading animals csv")
        return AnimalsCSV(pd.read_csv(file_name))


class CoolnessConfig(Node):
    _name = "CoolnessConfig"
    _calculated = True

    def __init__(self, coolness_dict: dict[str, int]):
        self._value = coolness_dict

    def dependencies(self) -> tuple[ABCMeta]:
        return tuple()

    def calculate(self, *args):
        pass

    @staticmethod
    def from_file(file_name: str) -> Self:
        print("Loading coolness yaml")
        with open(file_name, "r") as f:
            my_dict = yaml.safe_load(f)
        return CoolnessConfig(my_dict)


class CatsColumn(Node):
    _name = "CatsColumn"

    def dependencies(self) -> tuple[ABCMeta]:
        return (AnimalsCSV,)

    def calculate(self, *args):
        print(f"Calculating {self.name}")
        (df,) = args
        self._value = df["cats"]
        self._calculated = True


class DogsColumn(Node):
    _name = "DogsColumn"

    def dependencies(self) -> tuple[ABCMeta]:
        return (AnimalsCSV,)

    def calculate(self, *args):
        print(f"Calculating {self.name}")
        (df,) = args
        self._value = df["dogs"]
        self._calculated = True


class MamalsColumn(Node):
    _name = "MamalsColumn"

    def dependencies(self) -> tuple[ABCMeta]:
        return CatsColumn, DogsColumn

    def calculate(self, *args):
        print(f"Calculating {self.name}")
        cats, dogs = args
        self._value = cats + dogs
        self._calculated = True


class CoolnessColumn(Node):
    _name = "CoolnessColumn"

    def dependencies(self) -> tuple[ABCMeta]:
        return AnimalsCSV, CoolnessConfig

    def calculate(self, *args):
        print(f"Calculating {self.name}")
        animals, conf = args
        self._value = (
            animals["cats"] * conf["cats"]
            + animals["dogs"] * conf["dogs"]
            + animals["iguanas"] * conf["iguanas"]
        )
        self._calculated = True
