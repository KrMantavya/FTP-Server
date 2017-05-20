from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("mantavya", "123", "/home/mantavya294/projects/FTPServer/ftpserverDirectory", perm="elradfmw")
authorizer.add_anonymous("/home/mantavya294/ftpserver")
handler = FTPHandler
handler.authorizer = authorizer
connection = ("localhost", 8080)
ftpd = FTPServer(connection, handler)
ftpd.serve_forever()
