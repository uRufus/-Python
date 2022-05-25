# Base path to stored templates
import json
from dataclasses import dataclass
from framework.view import View

TEMPLATE_PATH = 'framework/templates/'

# In path you assign URL to template
paths = {
    '/': 'index.html',
    '/about': 'about.html',
}

def url_map(path):
    if path in paths:
        return f'{TEMPLATE_PATH}{paths[path]}'
    return f'{TEMPLATE_PATH}{paths["/"]}'

@dataclass
class Url:
    path: str
    view: View
