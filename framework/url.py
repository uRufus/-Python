from dataclasses import dataclass
from framework.view import View

@dataclass
class Url:
    path: str
    view: View
    name: str

