class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p = programmer("Payal", 10000000, 411014)
print(p.name, p.salary, p.pin, p.company)
s = programmer("Prajwal", 1200000, 411027)
print(s.name, s.salary, s.pin, s.company)