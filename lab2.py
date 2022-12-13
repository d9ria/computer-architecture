class Register:
    def __init__(self):
        self.A = "0000 0000 0000"
        self.R1 = "0000 0000 0000"
        self.R2 = "0000 0000 0000"
        self.PC = 0
        self.TC = 0
        self.PS = 0
        self.IR = ""

    def to_binary(self, var):
        n = ""
        var2 = abs(int(var))
        while var2 > 0:
            y = str(var2 % 2)
            n = y + n
            var2 = int(var2 / 2)
        if len(n) < 12:
            n = n.zfill(12)  # 12 битов
        if int(var) > 0:
            self.PS = 0
        if int(var) < 0:
            self.PS = 1
            n = list(n)
            n[0] = "1"
            n = ''.join(n)
        n = ' '.join([n[i:i + 4] for i in range(0, len(n), 4)])
        return n

    def load(self, var):
        self.TC += 1
        n = self.to_binary(var)
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()
        self.A = n
        self.TC += 1
        self.PC += 1
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()

    def shift(self, steps):
        self.TC += 1
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()
        steps = int(steps)
        #  двоичное число в список
        a = list(self.A)

        #  алгоритм сдвига
        if steps < 0:
            steps = abs(steps)
            for i in range(steps):
                a.append(a.pop(0))
        else:
            for i in range(steps):
                a.insert(0, a.pop())

        #  список в двоичное число
        n = ''.join(a)
        n = ''.join(n.split())
        if n[0] == "1":
            self.PS = 1
        else:
            self.PS = 0
        self.A = ' '.join([n[i:i + 4] for i in range(0, len(n), 4)])
        self.PC += 1
        self.TC += 1
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()

    def save(self, register):
        self.TC += 1
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()
        if register == "R1":
            self.R1 = self.A
        else:
            self.R2 = self.A
        self.PC += 1
        self.TC += 1
        print("IR:", self.IR)
        print("A:", self.A)
        print("R1:", self.R1)
        print("R2:", self.R2)
        print("PS:", self.PS)
        print("PC:", self.PC)
        print("TC:", self.TC)
        print()


def main():
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
    i = 0
    while i < len(d):
        for d[i] in d:
            if d[i][0] == "load":
                r.IR = d[i][0] + ", " + r.to_binary(d[i][1])
                r.load(d[i][1])
            if d[i][0] == "shift":
                r.IR = d[i][0] + ", " + d[i][1]
                r.shift(d[i][1])
            if d[i][0] == "save":
                r.IR = d[i][0] + ", " + d[i][1]
                r.save(d[i][1])
            i += 1


main()