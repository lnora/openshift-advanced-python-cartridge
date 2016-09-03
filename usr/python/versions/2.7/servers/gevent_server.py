import os
from gevent import socket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

import app


#sock_path = "{0}run/appserver.sock".format(os.environ["OPENSHIFT_ADVANCED_PYTHON_DIR"])
#sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
#sock.bind(sock_path)
#sock.listen(256)

#WSGIServer(sock, app.application, handler_class=WebSocketHandler).serve_forever()

WSGIServer((os.environ.get("OPENSHIFT_ADVANCED_PYTHON_IP", "127.0.0.1"), 15001), app.application, handler_class=WebSocketHandler).serve_forever()
