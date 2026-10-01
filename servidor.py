from xmlrpc.server import SimpleXMLRPCServer

def calcular_pagamento(horas, valor_por_hora):
    return horas * valor_por_hora

servidor = SimpleXMLRPCServer(("localhost", 8005))

servidor.register_function(
    calcular_pagamento,
    "calcular_pagamento"
)

print("servidor RPC aguardando solicitações...")

servidor.serve_forever()


terminal:
PS C:\Users\quelu\OneDrive\Desktop\aula de python-anhaguera> python prova1/servidor.py
servidor RPC aguardando solicitações...
