# Questão 6
class Palindromo:
    def __init__(self):
        self.deque = []

    def __str__(self):
        return f"{self.deque}"
    
    def add(self, e):
        e = e.lower()
        for l in e:
            self.deque.append(l)
    
    def remove_first(self):
        r = self.deque.pop(0)
        return r

    def remove_last(self):
        r = self.deque.pop()
        return r

if __name__ == '__main__':
    p = Palindromo()
    p.add("abelha") #False

    while len(p.deque) > 1:
        if p.remove_first() == p.remove_last():
            continue
        else:
            break

    if len(p.deque) == 1: 
        print(True)
    else: 
        print(False)