from flask import make_response, jsonify


def HTTP_OK(data=None, status=200, message='OK', **kwargs):
    resp = dict()
    if data:
        resp['data'] = data
    resp['message'] = message
    resp['status'] = status
    resp.update(kwargs)
    return jsonify(resp), status


def HTTP_ERR(data=None, status=500, message='INTERNAL SERVER ERROR', **kwargs):
    if not isinstance(data, dict):
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


def getargs(request, *keys, default_val=None):
    json = request.get_json(force=True, silent=True)
    out = []
    for key in keys:
        out.append(request.args.get(key) or request.form.get(key) or(
            json.get(key, default_val) if isinstance(json, dict) else default_val)
        )
    return tuple(out)


