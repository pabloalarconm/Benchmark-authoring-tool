# from typing import List, Optional, Union
from pydantic import BaseModel

class benchmarkInput(BaseModel):
    web_benchmark: str
    creator: str

    class Config:
        json_schema_extra = {
            "example":{
                "web_benchmark": "https://oeg-upm.github.io/fair_ontologies/doc/benchmark/ALL/ALL.ttl",
                "creator": "https://orcid.org/0000-0003-0454-7145"
            }
    }
