from modetp4l import SORTEO, BOLILLERO, CARTON

from tkinter import messagebox as MessageBox

from tkinter import *

from datetime import date


class CONTROLLER(SORTEO):

   def view_carton (self):

      self.carton = CARTON().get_carton_sorteo()

      self.text = (""" EL CARTÓN ES 
            
      {0} - {1} - {2} - {3} - {4} - {5} - {6} - {7} - {8} - {9} - {10} - {11} - {12} - {13} - {14} """ )

    
      self.carton_text = self.text.format(self.carton[0], self.carton[1], self.carton[2], self.carton[3], 
        
                        self.carton[4], self.carton[5], self.carton[6], self.carton[7], self.carton[8], self.carton[9], self.carton[10], self.carton[11], self.carton[12], self.carton[13], self.carton[14])

      self.carton_view.configure(text = self.carton_text)


   def sorteo (self):

      try:

         self.view_bolillas()

         self.aciertos = self.result_sorteo()

         self.date_sorteo = date.today()

         self.n_sorteo = self.num_sorteo()

         self.fecha_sorteo.configure(text = self.date_sorteo)

         self.numero_sorteo.configure(text = (f"{self.n_sorteo} "))


         if self.aciertos == 15 :

            MessageBox.showerror("FELICIDADES", 
      " ¡¡¡¡ TUVISTE 15 ACIERTOS, HAZ GANADO EL POZO ACUMULADO DEL TELEKINO !!!!!!!")

            self.win_table.insert("",END, values = ("15", " 1", self.pozo_sort()))

            self.seteo_sorteo()


         else:

            MessageBox.showerror("A NO DECAER", 
                  f"¡¡¡¡ TUVISTE {self.aciertos} ACIERTOS, EL POZO QUEDA VACANTEEE !!!!!!!")


            self.win_table.insert("",END, values = ("15", " VACANTE ", self.pozo_sort()))

            self.seteo_sorteo()

      except:

         self.seteo_sorteo()

         MessageBox.showerror("ALERTA", 
    " ¡¡¡¡ PRIMERO COMPRA UN CARTON !!!!!!!")



   def view_bolillas(self):

         self.lista_bolillas = BOLILLERO().get_bolillas_sorteo()

         self.lista_bolillas_str = []

         for i in self.lista_bolillas:

            self.lista_bolillas_str.append(str(i))
      
         self.num1.configure(text = (self.lista_bolillas_str[0]))
         self.num2.configure(text = (self.lista_bolillas_str[1]))
         self.num3.configure(text = (self.lista_bolillas_str[2]))
         self.num4.configure(text = (self.lista_bolillas_str[3]))
         self.num5.configure(text = (self.lista_bolillas_str[4]))
         self.num6.configure(text = (self.lista_bolillas_str[5]))
         self.num7.configure(text = (self.lista_bolillas_str[6]))
         self.num8.configure(text = (self.lista_bolillas_str[7]))
         self.num9.configure(text = (self.lista_bolillas_str[8]))
         self.num10.configure(text = (self.lista_bolillas_str[9]))
         self.num11.configure(text = (self.lista_bolillas_str[10]))
         self.num12.configure(text = (self.lista_bolillas_str[11]))
         self.num13.configure(text = (self.lista_bolillas_str[12]))
         self.num14.configure(text = (self.lista_bolillas_str[13]))
         self.num15.configure(text = (self.lista_bolillas_str[14]))


   
   def seteo_sorteo (self):

         self.num1.configure(text = " " )
         self.num2.configure(text = " " )
         self.num3.configure(text = " " )
         self.num4.configure(text = " " )
         self.num5.configure(text = " " )
         self.num6.configure(text = " " )
         self.num7.configure(text = " " )
         self.num8.configure(text = " " )
         self.num9.configure(text = " " )
         self.num10.configure(text = " " )
         self.num11.configure(text = " " )
         self.num12.configure(text = " " )
         self.num13.configure(text = " " )
         self.num14.configure(text = " " )
         self.num15.configure(text = " " )

         self.carton_view.configure(text = " " )

         self.numero_sorteo.configure(text = " ")

         self.fecha_sorteo.configure(text = " ")








   
 

      

  

      
    


            







        


    

     

      

        












