# and or not

gas = True
encendido = True
edad = 18

if gas and (encendido or edad > 17):
    print('puedes avanzar')
# operadores de corto circuito
if gas and encendido and edad > 17:
    print('puedes avanzar')
