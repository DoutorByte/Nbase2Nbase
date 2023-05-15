def int2base(n, b):
    if n < b:
        return chr(n + 48) if n < 10 else chr(n + 55)
    return int2base(n // b, b) + int2base(n % b, b)

def base2int(n, b):
    f = lambda c: 0 if not c else b*f(c[1:]) + c[0]
    chars = [ord(c) - 48 if ord(c) < 65 else ord(c) - 55 for c in reversed(n.upper())]
    return f(chars)


def base2base(n, b1, b2):
    return int2base(base2int(n, b1), b2)
  
# converter o número DECIMAL "123456789" para HEXADECIMAL
resultado = int2base(123456789, 16)
print(resultado)  # saída: "75BCD15"

# converter o número HEXA "75BCD15" para decimal (REQUER AS FUNÇÕES int2base E base2int)
resultado = base2int("75BCD15", 16)
print(resultado)  # saída: 123456789


# converter o número HEXA "75BCD15" para BINÁRIO
resultado = base2base("75BCD15", 16, 2) 
print(resultado) # saída: "111010110111100110100010101"
