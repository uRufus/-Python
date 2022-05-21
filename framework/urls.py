# Base path to stored templates
import json

TEMPLATE_PATH = 'templates/'

# In path you assign URL to template
paths = {
    '/': 'index.html',
    '/about': 'about.html',
}


def url_map(path):
    if path in paths:
        return f'{TEMPLATE_PATH}{paths[path]}'
    return f'{TEMPLATE_PATH}{paths["/"]}'
