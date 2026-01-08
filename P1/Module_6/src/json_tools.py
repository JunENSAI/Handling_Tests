from typing import Any

def flatten_json(y: dict[str, Any]) -> dict[str, Any]:
    out = {}

    def flatten(x: dict[str, Any], name: str = ''):
        if type(x) is dict:
            if "secret_key" in x:
                del x['secret_key']
                return flatten(x, name)
            
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out