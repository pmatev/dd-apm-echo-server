#!/usr/bin/env python

from sanic import Sanic, response
import msgpack
import pprint

app = Sanic(name='dd-apm-echo-server')
pp = pprint.PrettyPrinter(indent=4)


@app.route("/v0.4/traces", methods=["POST"])
async def test(request):
    if request.content_type == 'application/msgpack':
        pp.pprint(msgpack.unpackb(request.body))
        return response.json({'msgpack': True})
    return response.json({})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv('PORT', 9001))