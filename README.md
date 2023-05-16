# Nbase2Nbase
Funções mátemáticas para conveter números de qualquer base para outra.
<br>
<br>
Converter o número DECIMAL "123456789" para HEXADECIMAL<br>
resultado = int2base(123456789, 16)<br>
print(resultado)  # saída: "75BCD15"<br>
<br>
Converter o número HEXA "75BCD15" para decimal<br>
resultado = base2int("75BCD15", 16)<br>
print(resultado)  # saída: 123456789<br>

Converter o número HEXA "75BCD15" para BINÁRIO  (REQUER AS FUNÇÕES int2base E base2int)<br>
resultado = base2base("75BCD15", 16, 2) <br>
print(resultado) # saída: "111010110111100110100010101"<br>
