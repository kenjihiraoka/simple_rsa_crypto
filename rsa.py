import random
import sys

class RsaCrypto():
    def __init__(self):
        self.n = None
        self.p = None
        self.q = None
        self.z = None
        self.d = None
        self.c = None
        self.char = None
        self.ascii_char = None
        self.mmc_z =[]
        self.mmc_e = []
        
    def get_p_q_value(self):
        factors = []
        while True:
            self.p = int(input('Entre com o valor de p: '))
            for i in range(1, self.p + 1):
                if self.p % i == 0:
                    factors.append(i)
                    if len(factors) > 2:
                        print('O valor de p não é primo.\nPor favor escolha outro valor.')
                        self.p = int(input('Entre com o valor de p: '))
            break
            
        factors = []
        while True:
            self.q = int(input('Entre com o valor de q: '))
            for i in range(1, self.q + 1):
                if self.q % i == 0:
                    factors.append(i)
                    if len(factors) > 2:
                        print('O valor de q não é primo.\nPor favor escolha outro valor.')
                        self.q = int(input('Entre com o valor de q: '))
            break

    def get_n_value(self):
        self.n = self.p * self.q
        print('Value of n: {}'.format(self.n))
    
    def get_z_value(self):
        self.z = (self.p - 1) * (self.q - 1)
        print('Value of z: {}'.format(self.z))
    
    def get_e_value(self):
        for e in range(1, self.n - 1):
            if (e % self.z) > 0:
                self.get_minimum_multiple(e)
                c_number = self.verify_cousin_number()
                if c_number == True:
                    self.e = e
                    print('Value of e: {}'.format(self.e))
                    break
    
    def verify_cousin_number(self):
        cont = 0
        for i in range(len(self.mmc_z)):
            for j in range(len(self.mmc_e)):
                if self.mmc_z[i] == self.mmc_e[j]:
                    cont += 1
        if cont >= 2:
            return False
        return True
    
    def get_minimum_multiple(self, e):
        self.mmc_z.append([i for i in range(1, self.z) if self.z % i == 0])
        self.mmc_e.append([i for i in range(1 , e) if e %i == 0])

    def get_character(self):
        self.char = input('Entre com o caractere que deseje encriptar: ')
        self.char_ascii = ord(self.char)
        print('Value of char: {}\nValue of char_ascii: {}'.format(self.char, self.char_ascii))
    
    def get_d_value(self):
        for n in range(2, 10000):
            d = (self.e * n) - 1
            if d % self.z == 1:
                self.d = d
                print('Value of d: {}'.format(self.d))
                break
                                            
    def encrypti(self):
        #c=m^e mod n
        self.c = pow(self.char_ascii, self.e) % self.n
        print('Value of c: {}'.format(self.c))
        
    def decrypt(self):
        #m=c^d mod n
        self.m = pow(self.c, self.d) % self.n
        print('Value of m: {}'.format(self.m))
        
        if (chr(self.m) == self.char):
            print('Your crypto is right!')
        else:
            print('You made a mistake!')

    def run(self):
        self.get_p_q_value()
        self.get_n_value()
        self.get_z_value()
        self.get_e_value()
        self.get_d_value()
        self.get_character()
        self.encrypti()
        self.decrypt()
  
    def run_test(self):
        self.p = 13
        self.q = 17
        self.char = 'a'
        self.char_ascii = 97
        print('Value of p: {}\nValue of q: {}\nValue of char: {}\nValue of char_ascii: {}'.format(
            self.p, self.q, self.char, self.char_ascii
        ))
        self.get_n_value()
        self.get_z_value()
        self.get_e_value()
        self.get_d_value()
        self.encrypti()
        self.decrypt()
            
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'test':
            print('============= TEST MODE =============')
            RsaCrypto().run_test()
    else:
        rsa = RsaCrypto()
        rsa.run()
    