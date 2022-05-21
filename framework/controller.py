import json
from templator import render
from urls import url_map


def control_func(method, path, body=None):
    if method == 'GET':
        output = render(url_map(path))
    elif method == 'POST':
        try:
            proper_body = json.loads(body)
        except TypeError:
            proper_body = body
        output = render(url_map(path), object_list=proper_body)

    return [output.encode('UTF-8')]


if __name__ == '__main__':
    # Пример использования
    output_test = control_func('POST', '/', ['name', 1233])
    print(output_test)
