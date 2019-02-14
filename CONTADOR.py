class Contador():
    def __init__(self):
        self.inicio= 00
    
    def incrementar(self):
        self.inicio+=1
        
    def decrementar(self):
        self.inicio -=1        


cont1 = Contador()
print("CONTADOR:", cont1.inicio)
cont1.incrementar()
print("CONTADOR:", cont1.inicio)
cont1.incrementar()
print("CONTADOR:", cont1.inicio)
cont1.incrementar()
print("CONTADOR:", cont1.inicio)
cont1.decrementar()
print("CONTADOR:", cont1.inicio)
cont1.incrementar()
print("CONTADOR:", cont1.inicio)
cont1.decrementar()
print("CONTADOR:", cont1.inicio)
