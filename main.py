from model import *
from visao import *
from controle import *

if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    root.title("Sistema Acadêmico")

    frame_main = SistemaAcademico(root)

    root.mainloop()