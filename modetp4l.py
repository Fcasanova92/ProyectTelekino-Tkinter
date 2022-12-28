import random

class LIST_NUMBER:

    def __init__(self):

        self.numbers = []

        self.numbers_verify = []

        self.number_order = []

        self.count = 0


    def num_sort(self):

        while self.count < 15:

            self.num=random.randint(1,25)

            self.numbers.append(self.num)

            if self.numbers.count(self.num) == 1:

                self.count += 1

                self.numbers_verify.append(self.num)

                self.numbers_order = sorted(self.numbers_verify)

        return self.numbers_order



class CARTON(LIST_NUMBER):

    def __init__(self):

        super().__init__()

        self.carton = self.num_sort()


    def get_carton_sorteo (self):

        return self.carton




class BOLILLERO(LIST_NUMBER):

    def __init__(self):

        super().__init__()

        self.bolillas = self.num_sort()


    def get_bolillas_sorteo (self):

        return self.bolillas



class SORTEO (BOLILLERO,CARTON):

    def __init__(self):

        self.pozo = 115368971

        self.num_list_sorteo = []


    def num_sorteo(self):

        num=1

        self.num_list_sorteo.append(num)

        return sum(self.num_list_sorteo)


    def pozo_sort (self):

      if self.n_sorteo == 1:

         return self.pozo

      else:

         return self.pozo + self.pozo*0.1698*self.n_sorteo

    
    def result_sorteo(self):

        self.aciertos = 0

        for i in range(len(self.carton)):

            if self.lista_bolillas.count(self.carton[i]) == 1:

               self.aciertos += 1

        return self.aciertos






