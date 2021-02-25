from PyJS.modules import fs
import json as json_origin
import forbiddenfruit as ff

__all__ = (
    "JSON"
)

class JSON:
    def parse(stream:fs.createReadStream) -> dict:
        with open(stream.path, "r") as f:
            return json_origin.load(f)

    def stringify(_json:dict) -> str:
        return str(_json)