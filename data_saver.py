import json

from pathlib import Path
from abc import ABC, abstractmethod


class DataSaver(ABC):
    def __init__(
        self,
        filename: str,
        folder_name: str,
    ) -> None:
        self.filename = filename
        self.folder_name = folder_name

    @property
    def folder_name(self) -> str:
        """Getter for folder_name"""
        return self._folder_name

    @folder_name.setter
    def folder_name(self, vl: str) -> None:
        """Establish the desired folder structure, currently done local but ideally eventually done in a cloud storage
        somewhere.

        Parameters
        ----------
        vl : Folder structure that you will set up.
        """
        try:
            Path(f'{vl}').mkdir(parents=True, exist_ok=True)
        except Exception as e:
            raise e

        self._folder_name = vl

    @abstractmethod
    def save_data(self, to_save: str) -> None:
        """Save the serialised object to the desired location, currently local only.

        Parameters
        ----------
        to_save : data structure to be saved
        """
        pass


class JSONSaver(DataSaver):
    def save_data(self, to_save: str) -> None:
        with open(f'{self.folder_name}/{self.filename}.json', 'w', encoding='utf-8') as f:
            json.dump(to_save, f, ensure_ascii=False, indent=4)
