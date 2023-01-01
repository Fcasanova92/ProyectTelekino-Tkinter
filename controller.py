from modetp4l import  SORTEO, BOLILLERO, CARTON

from vista import INTERFAZ

from tkinter import messagebox as MessageBox

from tkinter import *

from datetime import date



class CONTROLLER:

   def __init__(self):

      self.root = Tk()

      self.sort = SORTEO()

      self.vista = INTERFAZ(self.root, self)

      self.root.mainloop()
      



   def view_carton (self):

      self.get_carton = CARTON().get_carton_sorteo()

      self.vista.Boton_sorteo.configure(state = "normal")

      self.text = (""" EL CARTÓN ES 
            
      {0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14} """ )

    
      self.carton_text = self.text.format(self.get_carton[0], self.get_carton[1], self.get_carton[2], self.get_carton[3], 
        
                        self.get_carton[4], self.get_carton[5], self.get_carton[6], self.get_carton[7], self.get_carton[8], self.get_carton[9], self.get_carton[10], self.get_carton[11], 
                        
                        self.get_carton[12], self.get_carton[13], self.get_carton[14])
                        

      self.vista.carton_view.configure(text = self.carton_text)



   
   def view_bolillas(self):

      self.get_bolillero = BOLILLERO().get_bolillas_sorteo()

      self.lista_num_bolillas = []

      for i in self.get_bolillero:

         self.lista_num_bolillas.append(str(i))
      
      self.vista.num1.configure(text = (self.lista_num_bolillas[0]))
      self.vista.num2.configure(text = (self.lista_num_bolillas[1]))
      self.vista.num3.configure(text = (self.lista_num_bolillas[2]))
      self.vista.num4.configure(text = (self.lista_num_bolillas[3]))
      self.vista.num5.configure(text = (self.lista_num_bolillas[4]))
      self.vista.num6.configure(text = (self.lista_num_bolillas[5]))
      self.vista.num7.configure(text = (self.lista_num_bolillas[6]))
      self.vista.num8.configure(text = (self.lista_num_bolillas[7]))
      self.vista.num9.configure(text = (self.lista_num_bolillas[8]))
      self.vista.num10.configure(text = (self.lista_num_bolillas[9]))
      self.vista.num11.configure(text = (self.lista_num_bolillas[10]))
      self.vista.num12.configure(text = (self.lista_num_bolillas[11]))
      self.vista.num13.configure(text = (self.lista_num_bolillas[12]))
      self.vista.num14.configure(text = (self.lista_num_bolillas[13]))
      self.vista.num15.configure(text = (self.lista_num_bolillas[14]))


   
   def seteo_sorteo (self):

      self.vista.num1.configure(text = " " )
      self.vista.num2.configure(text = " " )
      self.vista.num3.configure(text = " " )
      self.vista.num4.configure(text = " " )
      self.vista.num5.configure(text = " " )
      self.vista.num6.configure(text = " " )
      self.vista.num7.configure(text = " " )
      self.vista.num8.configure(text = " " )
      self.vista.num9.configure(text = " " )
      self.vista.num10.configure(text = " " )
      self.vista.num11.configure(text = " " )
      self.vista.num12.configure(text = " " )
      self.vista.num13.configure(text = " " )
      self.vista.num14.configure(text = " " )
      self.vista.num15.configure(text = " " )

      self.vista.carton_view.configure(text = " " )

      self.vista.numero_sorteo.configure(text = " ")

      self.vista.fecha_sorteo.configure(text = " ")



   def aciertos(self):

      self.n_aciertos = 0
      
      for i in range(len(self.get_carton)):

         if self.get_bolillero.count(self.get_carton[i]) == 1:

            self.n_aciertos += 1


      if self.n_aciertos == 15 :

         MessageBox.showerror("FELICIDADES", 
            " ¡¡¡¡ TUVISTE 15 ACIERTOS, HAZ GANADO EL POZO ACUMULADO DEL TELEKINO !!!!!!!")

         self.vista.win_table.insert("",END, values = ("15", " 1", self.sort.pozo_sort()))

         self.seteo_sorteo()


      else:

         MessageBox.showerror("A NO DECAER", 
                        f"¡¡¡¡ TUVISTE {self.n_aciertos} ACIERTOS, EL POZO QUEDA VACANTEEE !!!!!!!")


         self.vista.win_table.insert("",END, values = ("15", " VACANTE ", self.sort.pozo_sort()))

         self.seteo_sorteo()




   def result_sorteo (self):

      self.view_bolillas()

      self.vista.Boton_sorteo.configure(state = "disabled")

      self.date_sorteo = date.today()

      self.n_sorteo = self.sort.n_sorteo()

      self.vista.fecha_sorteo.configure(text = self.date_sorteo)

      self.vista.numero_sorteo.configure(text = (f"{self.n_sorteo} "))

      self.result_sorteo =  self.aciertos()

      

      












