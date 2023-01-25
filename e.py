class MyClass :
    @staticmethod
    def main( args) :
        print("jaja")
        a = ["eq 1", "eq 2", "eq 3", "eq 4", "eq 5", "eq 6", "eq 7", "eq 8"]
        print("las fechas de partidos son : " + str((len(a) - 1)))
        if (len(a) % 2 == 0) :
            i = 0
            while (i < len(a) - 1) :
                print("=========== fecha " + str((i + 1)) + "==============")
                if (i == 0) :
                    MyClass.mostrarFecha(a)
                else :
                    aux = MyClass.ordenarFecha(a)
                    MyClass.mostrarFecha(aux)
                    a = aux
                i += 1
    @staticmethod
    def  ordenarFecha( a) :
        aux = [None] * (len(a))
        aux[0] = a[0]
        aux[1] = a[len(a) - 1]
        i = 2
        while (i < len(a)) :
            aux[i] = a[i - 1]
            i += 1
        return aux
    @staticmethod
    def mostrarFecha( a) :
        numero = int(len(a) / 2)
        con = 0
        i = 0
        while (i < len(a)) :
            if (con != numero) :
                print(a[i] + " vs " + a[(len(a) - con) - 1])
                con += 1
            i += 1
    

if __name__=="__main__":
    MyClass.main([])