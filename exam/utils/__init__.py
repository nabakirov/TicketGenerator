from flask import make_response, jsonify


def HTTP_OK(data=None, status=200, message='OK', **kwargs):
    if not isinstance(data, dict) or not isinstance(data, list):
        data = dict(
            status=status,
            message=message
        )
    data.update(kwargs)
    if 'message' not in data:
        data['message'] = message
    if 'status' not in data:
        data['status'] = status
    return jsonify(data), status


def HTTP_ERR(data=None, status=500, message='INTERNAL SERVER ERROR', **kwargs):
    if not isinstance(data, dict) or not isinstance(data, list):
        data = dict(
            status=status,
            error=message
        )
    data.update(kwargs)
    if 'error' not in data:
        data['error'] = message
    if 'status' not in data:
        data['status'] = status

    r = make_response(jsonify(data))
    r.headers['Access-Control-Allow-Origin'] = '*'
    return r, status


def getargs(request, *keys, default_val=None):
    json = request.get_json(force=True, silent=True)
    out = []
    for key in keys:
        out.append(request.args.get(key) or request.form.get(key) or(
            json.get(key, default_val) if isinstance(json, dict) else default_val)
        )
    return tuple(out)


