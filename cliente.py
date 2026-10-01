from xmlrpc.client import ServerProxy

servidor = ServerProxy("http://lacalhost:8005/")

resultado = servidor.calcular_pagamento(8, 25)

print("Valor do pagamento:", resultado)


terminal:

PS C:\Users\quelu\OneDrive\Desktop\aula de python-anhaguera> python prova1/cliente.py
Traceback (most recent call last):
  File "C:\Users\quelu\OneDrive\Desktop\aula de python-anhaguera\prova1\cliente.py", line 5, in <module>
    resultado = servidor.calcular_pagamento(8, 25)
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1096, in __call__
    return self.__send(self.__name, args)
           ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1435, in __request
    response = self.__transport.request(
        self.__host,
    ...<2 lines>...
        verbose=self.__verbose
        )
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1140, in request
    return self.single_request(host, handler, request_body, verbose)
           ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1152, in single_request
    http_conn = self.send_request(host, handler, request_body, verbose)
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1265, in send_request
    self.send_content(connection, request_body)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\xmlrpc\client.py", line 1295, in send_content
    connection.endheaders(request_body)
    ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\http\client.py", line 1333, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
    ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\http\client.py", line 1093, in _send_output
    self.send(msg)
    ~~~~~~~~~^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\http\client.py", line 1037, in send
    self.connect()
    ~~~~~~~~~~~~^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\http\client.py", line 1003, in connect
    self.sock = self._create_connection(
                ~~~~~~~~~~~~~~~~~~~~~~~^
        (self.host,self.port), self.timeout, self.source_address)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\socket.py", line 840, in create_connection
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
               ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\quelu\AppData\Local\Programs\Python\Python313\Lib\socket.py", line 977, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
               ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
socket.gaierror: [Errno 11001] getaddrinfo failed
PS C:\Users\quelu\OneDrive\Desktop\aula de python-anhaguera> 




