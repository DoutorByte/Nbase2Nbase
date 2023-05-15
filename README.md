# Nbase2Nbase
Funções mátemáticas para conveter números de qualquer base para outra.


# converter o número DECIMAL "123456789" para HEXADECIMAL
resultado = int2base(123456789, 16)
print(resultado)  # saída: "75BCD15"

# converter o número HEXA "75BCD15" para decimal (REQUER AS FUNÇÕES int2base E base2int)
resultado = base2int("75BCD15", 16)
print(resultado)  # saída: 123456789


# converter o número HEXA "75BCD15" para BINÁRIO
resultado = base2base("75BCD15", 16, 2) 
print(resultado) # saída: "111010110111100110100010101"
