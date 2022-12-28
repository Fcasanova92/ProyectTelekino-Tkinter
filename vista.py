from tkinter import *

from tkinter import ttk

from controller import CONTROLLER


class INTERFAZ (CONTROLLER):

    def __init__(self):

        super().__init__()
        
        self.root = Tk()

        self.root.config(width=1093, height=659, bg = "DeepSkyBLue2")

        self.root.resizable(0,0)

        self.root.title("Telekino")

        self.icono_root = PhotoImage(file = R"C:\Users\User\Desktop\Python-Domo\TPS\TP4\Logonuevo150.png")

        self.root.iconphoto(True, self.icono_root)

        # Frame donde se ubicaran los widgets 

        self.frame = Frame( self.root)

        self.frame_principal()

        self.root.mainloop()


    def frame_principal (self):

            self.frame.config(width=1050, height= 640, bg = "SkyBlue2")

            self.frame.place(x = 20 , y = 20)

            self.icono = PhotoImage(file=R"C:\Users\User\Desktop\Python-Domo\TPS\TP4\telekino_imagen.png")

            self.imagen_telekino = Label(self.frame, image = self.icono, bg = "SkyBlue2")

            self.imagen_telekino.place(x = 90, y = 15)


            # Numeros sorteados

            self.num1 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num1.place(x = 20, y = 320)


            self.num2 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num2.place(x = 100, y = 320)


            self.num3 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num3.place(x = 180, y = 320)


            self.num4 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num4.place(x = 260, y = 320)


            self.num5 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num5.place(x = 340, y = 320)


            self.num6 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num6.place(x = 20, y = 400)


            self.num7 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num7.place(x = 100, y = 400)


            self.num8 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num8.place(x = 180, y = 400)


            self.num9 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num9.place(x = 260, y = 400)


            self.num10 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num10.place(x = 340, y = 400)


            self.num11 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num11.place(x = 20, y = 480)


            self.num12 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num12.place(x = 100, y = 480)

            self.num13 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num13.place(x = 180, y = 480)


            self.num14 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num14.place(x = 260, y = 480)


            self.num15 = Label(self.frame, width= 4 , height= 2, bg="Yellow", font=("Arial Black", 15), text = " ", relief = "sunken", borderwidth = 5)

            self.num15.place(x = 340, y = 480)


            # Botones de sorteo y carton

            self.Boton_carton = Button(self.frame, width=22, height=1, bg= "white", font= ("Arial", 10), text = "Comprar Cartón", command=self.view_carton )

            self.Boton_carton.place(x = 20, y = 580 )



            self.Boton_sorteo = Button(self.frame, width=22, height=1, bg= "white", font= ("Arial", 10), text = "Sortear", command = self.sorteo )

            self.Boton_sorteo.place(x = 222, y = 580 )


            # Carton


            self.carton_view = Label(self.frame, width = 50 , height = 4, bg = "SkyBlue2", font=("Arial Black", 11), text = " ", 

            highlightthickness = 4, highlightbackground = "White", highlightcolor = "White")

            self.carton_view.place(x = 480, y = 2)



            # Tabla de Ganadores

            columnas_tabla = ("#1", "#2", "#3")

            style_win_table = ttk.Style()

            style_win_table.theme_use("default")

            style_win_table.configure("Treeview.Heading", background = "red", foreground = "white", font = ("Arial Black", 10))

            self.win_table = ttk.Treeview(self.frame, height = 18,  columns = columnas_tabla, show="headings")

            self.win_table.heading("#1", text= " CATEGORÍA ")

            self.win_table.heading("#2", text= " N° DE GANADORES ")

            self.win_table.heading("#3", text= " PREMIO $ C/U ")

            self.win_table.column("#1", width = 120)

            self.win_table.column("#2", width = 200)

            self.win_table.column("#3", width = 200)

            self.win_table.place(x = 500, y = 230)


            # Fecha y Numero de sorteo


            self.fecha_sorteo = Label(self.frame, width = 10 , height = 2, bg = "yellow", font=("Arial Black", 10), text = " ", relief="ridge")

            self.fecha_sorteo.place(x = 500, y = 155)

            self.fecha_sorteo_title = Label(self.frame, width = 10 , height = 2, bg = "white", font=("Arial Black", 10), text = " FECHA ", relief="ridge")

            self.fecha_sorteo_title.place(x = 500, y = 125)


            self.numero_sorteo = Label(self.frame, width = 15 , height = 2, bg = "yellow", font=("Arial Black", 10), text = " ", relief="ridge")

            self.numero_sorteo.place(x = 650, y = 155)

            self.numero_sorteo_title = Label(self.frame, width = 15 , height = 2, bg = "white", font=("Arial Black", 10), text = "SORTEO N°", relief="ridge")

            self.numero_sorteo_title.place(x = 650, y = 125)


proyecto = INTERFAZ ()















