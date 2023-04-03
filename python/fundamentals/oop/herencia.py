'''import cuentabancaria as  CuentaBancaria

class CuentaVitalicia(CuentaBancaria):
    def __init__(self, tasa_interés, cuenta_ira, balance=0):
        super().__init__(tasa_interés, balance)	
        self.cuenta_ira = cuenta_ira	
        super().deposito
'''

'''# importar la biblioteca

'''
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)