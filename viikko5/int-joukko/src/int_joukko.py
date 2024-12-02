class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _create_list(self, size):
        return [0] * size
    
    def __init__(self, size=5, growth=5):
        self.growth = growth
        self.list = self._create_list(size)
        self.total_count = 0

    def includes(self, n):
        for i in range(0, self.total_count):
            if n == self.list[i]:
                return True
        return False

    def add(self, n):
        if self.includes(n):
            return False
        
        self.list[self.total_count] = n
        self.total_count = self.total_count + 1

        if self.total_count % len(self.list) == 0:
            new_list = self._create_list(self.total_count + self.growth)
            self.copy_list(self.list, new_list)
            self.list = new_list

        return True

    def delete(self, n):
        index_to_delete = -1
    
        for i in range(self.total_count):
            if self.list[i] == n:
                index_to_delete = i
                break

        if index_to_delete == -1:
            return False

        for j in range(index_to_delete, self.total_count - 1):
            self.list[j] = self.list[j + 1]

        self.total_count -= 1
        return True

    def copy_list(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def length(self):
        return self.total_count

    def to_int_list(self):
        new_list = self._create_list(self.total_count)

        for i in range(0, len(new_list)):
            new_list[i] = self.list[i]

        return new_list

    @staticmethod
    def combination(a, b):
        x = IntJoukko() 
        for number in a.to_int_list() + b.to_int_list():
            x.add(number)
        return x

    @staticmethod
    def intersection(a, b):
        y = IntJoukko()
        a_set = set(a.to_int_list())
        b_taulu = b.to_int_list()

        for element in b_taulu:
            if element in a_set:
                y.add(element)

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_list = a.to_int_list()
        b_list = b.to_int_list()

        for i in range(0, len(a_list)):
            z.add(a_list[i])

        for i in range(0, len(b_list)):
            z.delete(b_list[i])

        return z

    def __str__(self):
        if self.total_count == 0:
            return "{}"
        elif self.total_count == 1:
            return "{" + str(self.list[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.total_count - 1):
                tuotos = tuotos + str(self.list[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.list[self.total_count - 1])
            tuotos = tuotos + "}"
            return tuotos
