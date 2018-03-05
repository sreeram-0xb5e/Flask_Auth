from gevent.wsgi import WSGIServer
from yourapplication import app

http_server = WSGIServer(('', 9000), app)
http_server.serve_forever()
