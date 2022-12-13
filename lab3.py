import struct


class Register:
    def __init__(self):
        self.initial = self.float_to_bin(0)
        self.R1 = self.initial
        self.R2 = self.initial
        self.R3 = self.initial
        self.R4 = self.initial
        self.R5 = self.initial
        self.R6 = self.initial
        self.R7 = self.initial
        self.R8 = self.initial

        self.x = 0
        self.y = 0

        self._R1 = 0
        self._R2 = 0
        self._R3 = 0
        self._R4 = 0

        self.PC = 0  # лічильник команд
        self.TC = 0  # лічильник тактів
        self.PS = 0  # регістер стану
        self.IR = ""

    def print_nums(self):
        print("s hhhhhhhhhh n mmmmmmmm: number in IEEE 754 format")
        _min_mod = self.float_to_bin(0.5 * 2**(-9))
        print(f"{_min_mod} minimum for absolutely large large non-zero representation")
        _min = self.float_to_bin(-(1-2**(-8))*2**10)
        print(f"{_min} minimum negative representation")
        _max = self.float_to_bin((1 - 2 ** (-8)) * 2 ** 10)
        print(f"{_max} maximum negative representation")
        print()

    def print_registers(self):
        print("IR:", self.IR)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("R3:", self.R3)
        print("R4:", self.R4)
        print("R5:", self.R5)
        print("R6:", self.R6)
        print("R7:", self.R7)
        print("R8:", self.R8)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()

    #  перевод в нужный формат
    def float_to_bin(self, num):
        num = float(num)
        bits, = struct.unpack('!I', struct.pack('!f', num))
        n = "{:032b}".format(bits)
        n1 = n[0]
        n2 = n[1:9]
        n2 = n2.zfill(10)
        n3 = n[9:17]
        n = n1 + " " + n2 + " " + "1" + " " + n3
        return n

    def mov(self, num):
        self.PC += 1
        self.TC = 1
        n = self.float_to_bin(num)
        self.print_registers()
        self.TC += 1
        if n[0] == "1":
            self.PS = 1
        if n[0] == "0":
            self.PS = 0
        self._R4 = self._R3
        self._R3 = self._R2
        self._R2 = self._R1
        self._R1 = float(num)
        self.R8 = self.R7
        self.R7 = self.R6
        self.R6 = self.R5
        self.R5 = self.R4
        self.R4 = self.R3
        self.R3 = self.R2
        self.R2 = self.R1
        self.R1 = n
        self.print_registers()

    def copy(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        self.R2 = self.R1
        self._R2 = self._R1
        self.TC += 1
        self.print_registers()

    def mult(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        self._R1 = self._R1 * self._R2
        #  print(f"{self._R1} * {self._R2} = ")
        self.R1 = self.float_to_bin(self._R1)
        #  print(f"{self._R1}")
        self.R2 = self.R3
        self.R3 = self.R4
        self.R4 = self.R5
        self.R5 = self.R6
        self.R6 = self.R7
        self.R7 = self.R8
        self.R8 = self.initial
        self._R2 = self._R3
        self._R3 = self._R4
        self._R4 = 0
        self.TC += 1
        self.print_registers()

    def add(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        #  print(f"{self._R1} + {self._R2} =")
        self._R1 = self._R1 + self._R2
        #  print(f"{self._R1}")
        self.R1 = self.float_to_bin(self._R1)
        self.R2 = self.R3
        self.R3 = self.R4
        self.R4 = self.R5
        self.R5 = self.R6
        self.R6 = self.R7
        self.R7 = self.R8
        self.R8 = self.initial
        self._R2 = self._R3
        self._R3 = self._R4
        self._R4 = 0
        self.TC += 1
        self.print_registers()

    def reverse(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        tmp = self.R1
        self.R1 = self.R2
        self.R2 = tmp
        tmp1 = self._R1
        self._R1 = self._R2
        self._R2 = tmp1
        self.TC += 1
        self.print_registers()

    def sub(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        #  print(f"{self._R1} - {self._R2} =")
        self._R1 = self._R1 - self._R2
        #  print(f"{self._R1}")
        self.R1 = self.float_to_bin(self._R1)
        self.R2 = self.R3
        self.R3 = self.R4
        self.R4 = self.R5
        self.R5 = self.R6
        self.R6 = self.R7
        self.R7 = self.R8
        self.R8 = self.initial
        self._R2 = self._R3
        self._R3 = self._R4
        self._R4 = 0
        self.TC += 1
        self.print_registers()

    def div(self):
        self.PC += 1
        self.TC = 1
        self.print_registers()
        #  print(f"{self._R1} / {self._R2} =")
        self._R1 = self._R1 / self._R2
        #  print(f"{self._R1}")
        self.R1 = self.float_to_bin(self._R1)
        self.R2 = self.R3
        self.R3 = self.R4
        self.R4 = self.R5
        self.R5 = self.R6
        self.R6 = self.R7
        self.R7 = self.R8
        self.R8 = self.initial
        self._R2 = self._R3
        self._R3 = self._R4
        self._R4 = 0
        self.TC += 1
        self.print_registers()


def main():
    print()
    print("List of the commands: ")
    _list = list()
    f = open(r'C:\Users\User\aos\commands.txt')
    for line in f:
        _list.append(line)
    i = 0
    while i < len(_list):
        print(_list[i], end='')
        i += 1
    print("\n")
    _list = [line.rstrip() for line in _list]
    s = ','.join(_list)
    d = list(item.split(' ') for item in s.split(','))

    r = Register()
    r.x = input("Enter x: ")
    r.y = input("Enter y: ")
    print()
    r.print_nums()
    print()
    i = 0
    while i < len(d):
        for d[i] in d:
            if d[i][0] == "mov":
                if d[i][1] == "x":
                    d[i][1] = r.x
                if d[i][1] == "y":
                    d[i][1] = r.y
                r.IR = d[i][0] + ", " + d[i][1]
                r.mov(d[i][1])
            if d[i][0] == "copy":
                r.IR = d[i][0]
                r.copy()
            if d[i][0] == "mult":
                r.IR = d[i][0]
                r.mult()
            if d[i][0] == "add":
                r.IR = d[i][0]
                r.add()
            if d[i][0] == "reverse":
                r.IR = d[i][0]
                r.reverse()
            if d[i][0] == "sub":
                r.IR = d[i][0]
                r.sub()
            if d[i][0] == "div":
                r.IR = d[i][0]
                r.div()
            i += 1


main()
