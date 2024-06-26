from pydantic import BaseModel
from typing import Optional, List, Union
from polyfactory.factories.pydantic_factory import ModelFactory


class ExampleModel(BaseModel):
    values: Union[List[str], None]


class ExampleModelFactory(ModelFactory):
    __model__ = ExampleModel


if __name__ == "__main__":
    print(list(ExampleModelFactory.coverage()))
