from tkinter import *
import tkinter as tk
from tkinter import ttk, Frame, Button, Label, Canvas, TOP, W, BOTH, RIGHT, Y, messagebox
import controle

class SistemaAcademico:
    def __init__(self, master):
        self.master = master
        self.login_frame = Frame(master)
        self.login_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_login()

        self.mycanvas = Canvas(master)
        self.mycanvas.pack(side=LEFT, fill=BOTH, expand=YES)

        self.second_frame = Frame(self.mycanvas)

        self.mycanvas.create_window((0, 0), window=self.second_frame, anchor='nw')

        self.frame_atual = None
        
    def criar_interface_login(self):
        self.fonte = ("Verdana", "8")
        
        self.lbMatricula = Label(self.login_frame, text="Matricula:", font=self.fonte, width=10)
        self.lbMatricula.pack(pady=10)

        self.txMatricula = Entry(self.login_frame, font=self.fonte)
        self.txMatricula.pack()

        self.lbSenha = Label(self.login_frame, text="Senha:", font=self.fonte, width=10)
        self.lbSenha.pack(pady=10)

        self.txSenha = Entry(self.login_frame, font=self.fonte, show="*")
        self.txSenha.pack()

        self.btLogin = Button(self.login_frame, text="Login", font=self.fonte, command=self.efetuar_login, width=10)
        self.btLogin.pack()

        self.btCadastro = Button(self.login_frame, text="Cadastro", font=self.fonte, command=self.abrir_janela_cadastro, width=10)
        self.btCadastro.pack()

    def abrir_janela_cadastro(self):
        janela_cadastro = Toplevel()
        FrameCadastro_user(janela_cadastro)

    def efetuar_login(self):
        matricula = self.txMatricula.get()
        senha = self.txSenha.get()

        try:
            login_strategy = controle.Pessoa()
            login_strategy.get(matricula, senha)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {e}")

class FrameCadastro:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_cadastro()

    def criar_interface_cadastro(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text="Nome", font=self.fonte, width=10)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.lbcadMatricula = Label(self.cadastro_frame, text="Matricula", font=self.fonte, width=10)
        self.lbcadMatricula.pack(pady=10)

        self.txcadMatricula = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadMatricula.pack()

        self.lbcadTipo = Label(self.cadastro_frame, text="Tipo(estudante ou ADM)", font=self.fonte, width=20)
        self.lbcadTipo.pack(pady=10)

        self.txcadTipo = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadTipo.pack()

        self.lbcadSenha = Label(self.cadastro_frame, text="Senha", font=self.fonte, width=10)
        self.lbcadSenha.pack(pady=10)

        self.txSenha = Entry(self.cadastro_frame, font=self.fonte, show="*")
        self.txSenha.pack()

        self.btCAD = Button(self.cadastro_frame, text="Cadastrar", font=self.fonte, width=50, command=self.cadastrar_usuario)
        self.btCAD.pack(pady=20)

    def cadastrar_usuario(self):
        nome = self.txcadNome.get()
        matricula = self.txcadMatricula.get()
        tipo = self.txcadTipo.get()
        senha = self.txSenha.get()

        modelo_inserir = (nome, matricula, tipo, senha)

        try:
            pessoa_strategy = controle.Pessoa()
            pessoa_strategy.inserir(modelo_inserir)
            self.master.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

class FrameCadastro_user:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_cadastro_user()

    def criar_interface_cadastro_user(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text="Nome", font=self.fonte, width=10)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.lbcadMatricula = Label(self.cadastro_frame, text="Matricula", font=self.fonte, width=10)
        self.lbcadMatricula.pack(pady=10)

        self.txcadMatricula = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadMatricula.pack()

        self.lbcadTipo = Label(self.cadastro_frame, text="Tipo: Estudante", font=self.fonte, width=20)
        self.lbcadTipo.pack(pady=10)
        
        self.lbcadSenha = Label(self.cadastro_frame, text="Senha", font=self.fonte, width=10)
        self.lbcadSenha.pack(pady=10)

        self.txSenha = Entry(self.cadastro_frame, font=self.fonte, show="*")
        self.txSenha.pack()

        self.btCAD = Button(self.cadastro_frame, text="Cadastrar", font=self.fonte, width=50, command=self.cadastrar_usuario_user)
        self.btCAD.pack(pady=20)        

    def cadastrar_usuario_user(self):
        nome = self.txcadNome.get()
        matricula = self.txcadMatricula.get()
        tipo = "estudante"
        senha = self.txSenha.get()

        modelo_inserir_user = (nome, matricula, tipo, senha)

        try:
            pessoa_strategy = controle.Pessoa()
            pessoa_strategy.inserir(modelo_inserir_user)
            self.master.destroy()
        except Exception as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {err}")

class FrameMenu: 
    def __init__(self, master):
        self.master = master

        self.menu_frame = Frame(master)
        self.menu_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_menu()

    def criar_interface_menu(self):
        self.fonte = ("Verdana", "8")

        self.btGrade = Button(self.menu_frame, text="Ver Materias", font=self.fonte, width=50)
        self.btGrade["command"] = self.abrir_janela_materias
        self.btGrade.pack(pady=20)

        self.btHistorico = Button(self.menu_frame, text="Inserir no Historico", font=self.fonte, width=50, command=self.abrir_janela_historico)
        self.btHistorico.pack(pady=20)

        self.btRemovemat = Button(self.menu_frame, text="Remover do Historico", font=self.fonte, width=50, command=self.abrir_janela_remover)
        self.btRemovemat.pack(pady=20)

        self.btMostrarH = Button(self.menu_frame, text="Mostrar Historico", font=self.fonte, width=50, command=self.abrir_janela_mostrarH)
        self.btMostrarH.pack(pady=20)

        self.btSolicitamat = Button(self.menu_frame, text="Pesquisar", font=self.fonte, width=50, command=self.abrir_janela_pesquisar_aluno)
        self.btSolicitamat.pack(pady=20)

        self.btSolicitamat = Button(self.menu_frame, text="Inserir na Grade", font=self.fonte, width=50, command=self.abrir_janela_solicitar_materias)
        self.btSolicitamat.pack(pady=20)

        self.btSolicitamat = Button(self.menu_frame, text="Ver Grade", font=self.fonte, width=50, command=self.abrir_janela_grade_horaria)
        self.btSolicitamat.pack(pady=20)

        self.btLogout = Button(self.menu_frame, text="Logout", font=self.fonte, width=50, command=self.logout)
        self.btLogout.pack(pady=20)
    
    #ver materias
    def abrir_janela_materias(self):
        janela_grade = Toplevel()
        FrameGrade(janela_grade)

    #inserir no historico
    def abrir_janela_historico(self):
        janela_historico = Toplevel()
        FrameHistorico(janela_historico)

    #remover Materias Historico
    def abrir_janela_remover(self):
        janela_remover = Toplevel()
        remover = FrameRemove(janela_remover)

    #mostrar historico
    def abrir_janela_mostrarH(self):
        janela_mostrarh = Toplevel()
        mostrarh = FrameMostrarH(janela_mostrarh)
        
    #Matricular na materia
    def abrir_janela_solicitar_materias(self):
        janela_solicitar_materia = Toplevel()
        solicitar_materia = FrameSolicitarMateria(janela_solicitar_materia)

    #Mostrar grade
    def abrir_janela_grade_horaria(self):
        janela_grade_horaria = Toplevel()
        grade_horaria = FrameMostrarGrade(janela_grade_horaria)


    def abrir_janela_pesquisar_aluno(self):
        janela_pesquisar_aluno = Toplevel()
        pesquisar = FramePesquisa_Aluno(janela_pesquisar_aluno)
    
    def logout(self):
        self.master.destroy()

class FrameMenuAdm:
    def __init__(self, master):
        self.master = master

        self.menu_frame = Frame(master)
        self.menu_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_menu_adm()

    def criar_interface_menu_adm(self):
        self.fonte = ("Verdana", "8")

        self.btGrade = Button(self.menu_frame, text="Cadastrar Usuarios", font=self.fonte, width=50)
        self.btGrade["command"] = self.abrir_janela_cadastro_adm
        self.btGrade.pack(pady=20)

        self.btRemovemat = Button(self.menu_frame, text="Inserir Curso", font=self.fonte, width=50, command=self.abrir_janela_inserir_curso)
        self.btRemovemat.pack(pady=20)

        self.btHistorico = Button(self.menu_frame, text="Remover Curso", font=self.fonte, width=50, command=self.abrir_janela_remover_curso)
        self.btHistorico.pack(pady=20)

        self.btRemovemat = Button(self.menu_frame, text="Inserir Materias", font=self.fonte, width=50, command=self.abrir_janela_inserir_materia)
        self.btRemovemat.pack(pady=20)

        self.btGrade = Button(self.menu_frame, text="Ver Materias", font=self.fonte, width=50)
        self.btGrade["command"] = self.abrir_janela_grade
        self.btGrade.pack(pady=20)

        self.btHistorico = Button(self.menu_frame, text="Remover Materias", font=self.fonte, width=50, command=self.abrir_janela_remover_materia)
        self.btHistorico.pack(pady=20)

        self.btMostrarH = Button(self.menu_frame, text="Remover usuarios", font=self.fonte, width=50, command=self.abrir_janela_remover_usuario)
        self.btMostrarH.pack(pady=20)

        self.btSolicitamat = Button(self.menu_frame, text="Pesquisar", font=self.fonte, width=50, command=self.abrir_janela_pesquisar)
        self.btSolicitamat.pack(pady=20)

        self.btLogout = Button(self.menu_frame, text="Logout", font=self.fonte, width=50, command=self.logout)
        self.btLogout.pack(pady=20)
    
    def abrir_janela_cadastro_adm(self):
        janela_cadastro_adm = Toplevel()
        FrameCadastro(janela_cadastro_adm)

    def abrir_janela_inserir_curso(self):
        janela_inserir_curso = Toplevel()
        inserir_cursos = FrameInserir_Curso(janela_inserir_curso)
    
    def abrir_janela_inserir_materia(self):
        janela_inserir_materia = Toplevel()
        inserir = FrameInserir(janela_inserir_materia)

    def abrir_janela_remover_curso(self):
        janela_remover_curso = Toplevel()
        remover_curso = FrameRemover_Curso(janela_remover_curso)
    
    def abrir_janela_grade(self):
        janela_grade = Toplevel()
        FrameGrade(janela_grade)

    def abrir_janela_remover_materia(self):
        janela_remover_materia = Toplevel()
        remover = FrameRemover_Materia(janela_remover_materia)


    def abrir_janela_remover_usuario(self):
        janela_remover_usuario = Toplevel()
        remover_usuario = FrameRemover_User(janela_remover_usuario)
    
    def abrir_janela_pesquisar(self):
        janela_pesquisar = Toplevel()
        pesquisar = FramePesquisa(janela_pesquisar)

    def logout(self):
        self.master.destroy()

class FrameGrade:
    def __init__(self, master):
        self.master = master
        self.grade_frame = Frame(master)
        self.grade_frame.pack(expand=YES, fill=BOTH)
        
        curso_strategy = controle.Cursos()
        cursos = curso_strategy.get()

        self.curso_selecionado = tk.StringVar()
        self.combobox = ttk.Combobox(self.grade_frame, textvariable=self.curso_selecionado, values=cursos)
        self.combobox.pack(pady=5)

        self.botao_mostrar_materias = tk.Button(self.grade_frame, text="Mostrar Matérias", command=self.populate_table)
        self.botao_mostrar_materias.pack(pady=10)
       
        self.active = "white"
        self.default_color = "white"
        
        self.save_button = Button(self.grade_frame, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def fetch_data_from_db(self):
        curso_escolhido = self.combobox.get()
        materia_strategy = controle.Materia()
        return materia_strategy.get(curso_escolhido)

    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.grade_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Id", "Nome_materia", "Pre"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=20, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))

    def save_changes(self):
        cursor = self.conn.cursor()
        try:
            for row_idx in range(34):
                id_materia = row_idx + 1
                for col_idx, col_name in enumerate(["Id", "Nome_materia", "Pre"]):
                    cell = self.frame.pack_slaves()[row_idx].pack_slaves()[col_idx]
                    materia_info = {
                        "Id": id_materia,
                        "Nome_materia": cell.cget("text"),
                        "Pre": cell.cget("text")
                    }
                    query = "INSERT INTO salvo_grade (Id, Nome_materia, Pre) VALUES (%s, %s, %s)"
                    values = (materia_info["Id"], materia_info["Nome_materia"], materia_info["Pre"])
                    cursor.execute(query, values)
                    self.conn.commit()
                    print(f"Insercao bem-sucedida para a materia ID {id_materia}")
        except Exception as e:
            print(f"Erro durante a insercao no banco: {e}")
        finally:
            cursor.close()
        self.master.destroy()
            
    def voltar_ao_menu(self):
        self.master.destroy()

    def click(self, event, label):
        if label["bg"] == self.active:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active)

class FrameHistorico:
    def __init__(self, master):
        self.master = master
        self.labels = []
        
        self.historico_frame = Frame(master)
        self.historico_frame.pack(expand=YES, fill=BOTH)

        curso_strategy = controle.Cursos()
        cursos = curso_strategy.get()

        self.curso_selecionado = tk.StringVar()
        self.combobox = ttk.Combobox(self.historico_frame, textvariable=self.curso_selecionado, values=cursos)
        self.combobox.pack(pady=10)
        self.obter_matricula_usuario()

        self.active = "green"
        self.default_color = "white"

    def criar_interface_grade(self):
        self.fonte = ("Verdana", "8")
        
        self.label_titulo = Label(self.historico_frame, text="Grade de Matérias", font=("Verdana", 8, "bold"))
        self.label_titulo.pack(pady=10)

        self.btVoltar = Button(self.historico_frame, text="Voltar ao menu", font=self.fonte, width=50, command=self.voltar_ao_menu)
        self.btVoltar.pack(side=BOTTOM)

        self.save_button = Button(self.historico_frame, text="Salvar", font=self.fonte, width=50, command=self.save_changes)
        self.save_button.pack(side=BOTTOM)  

        self.populate_table()
    
    def obter_matricula_usuario(self):
        self.fonte = ("Verdana", "8")
        
        matricula_label = Label(self.historico_frame, text="Digite sua matrícula:")
        matricula_label.pack()
        matricula_entry = Entry(self.historico_frame)
        matricula_entry.pack()
        matricula_entry.focus_set()

        def salvar_matricula():
            self.matricula_usuario = matricula_entry.get()
            matricula_entry.pack_forget()
            self.criar_interface_grade()

        matricula_entry.bind("<Return>", lambda event: salvar_matricula())
    
    def fetch_data_from_db(self):
        curso_escolhido = self.combobox.get()

        materia_strategy = controle.Materia()
        return materia_strategy.get(curso_escolhido)
    
    def populate_table(self):
        if not self.master.winfo_exists():
            return
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.historico_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Nome_materia"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=20, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))
                self.labels.append(label)
                print(f"Label adicionado: {label.cget('text')}")

    def save_changes(self):
        try:
            print("Labels:", self.labels)
            for label in self.labels:
                materia_nome = label.cget("text")
                if label["bg"] == self.active:
                    materia_strategy = controle.Materia()
                    materia_id = materia_strategy.fetch_materia_id(materia_nome)
                    materia_pre = materia_strategy.fetch_materia_pre(materia_nome)
                    materia_curso = materia_strategy.fetch_materia_curso(materia_nome)

                    if materia_id is not None and materia_pre is not None:
                        historico_strategy = controle.Historico()
                        historico_strategy.inserir(self.matricula_usuario, materia_id, materia_nome, materia_curso)
                        
                else:
                    print(f"Erro: Materia {materia_nome} não encontrada no banco")
            messagebox.showinfo("Sucesso", "Materias selecionadas foram salvas")
        except Exception as e:
            print(f"Erro durante a insercao no banco: {e}")
            messagebox.showerror("Erro", f"Erro ao inserir as materias no banco: {e}")
        finally:
            self.master.destroy()
        
        self.populate_table()
            
    def voltar_ao_menu(self):
        self.master.destroy()

    def click(self, event, label):
        print(f"Label clicado: {label.cget('text')}")
        if label["bg"] == self.active:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active)

class FrameRemove:
    def __init__(self, master):
        self.master = master
        self.labels = []
        self.matricula_usuario = None
        self.active_color = "red"
        self.default_color = "white"
        
        self.solicitar_materia_frame = Frame(master)
        self.solicitar_materia_frame.pack(expand=YES, fill=BOTH)

        self.obter_matricula_usuario()

    def obter_matricula_usuario(self):
        matricula_label = Label(self.solicitar_materia_frame, text="Digite sua matrícula:")
        matricula_label.pack()
        matricula_entry = Entry(self.solicitar_materia_frame)
        matricula_entry.pack()
        matricula_entry.focus_set()

        def salvar_matricula():
            self.matricula_usuario = matricula_entry.get()
            matricula_entry.pack_forget()
            self.fetch_data_from_db()

        matricula_entry.bind("<Return>", lambda event: salvar_matricula())

    def fetch_data_from_db(self):
        materia_strategy = controle.Materia()
        data = materia_strategy.fetch_data_from_db_remove(self.matricula_usuario)

        for row_data in data:
            id_materia = row_data["Id"]
            nome_materia = row_data["Nome_materia"]
            pre_requisito = row_data["Pre"]
            curso = row_data["Curso"]
            row_frame = Frame(self.solicitar_materia_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            label = Label(row_frame, text=nome_materia, width=20, height=1, borderwidth=0.5, relief="solid", padx=5, bg=self.default_color)
            label.pack(side=LEFT, expand=YES, fill=BOTH)
            label.bind("<Button-1>", lambda event, label=label, id_materia=id_materia, nome_materia=nome_materia, pre_requisito=pre_requisito: self.click(event, label, id_materia, nome_materia, pre_requisito))
            self.labels.append(label)

        self.solicitar_button = Button(self.solicitar_materia_frame, text="Remover", command=self.apagar_materias)
        self.solicitar_button.pack(side=TOP)

    def apagar_materias(self):
        mat_selected = []

        for idx, label in enumerate(self.labels):
            if label.cget("bg") == self.active_color:
                id_materia = idx + 1
                nome_materia = label.cget("text")
                materia_strategy = controle.Materia()
                pre_requisito = materia_strategy.fetch_materia_pre_id(id_materia)
                if not self.verificar_historico(id_materia):
                    mat_selected.append((self.matricula_usuario, str(id_materia), nome_materia, pre_requisito))
                else:
                    messagebox.showwarning("Aviso", f"A matéria {id_materia} já está no seu histórico!")

        if mat_selected:
            try:
                for mat in mat_selected:
                    historico_strategy = controle.Historico()
                    historico_strategy.remover(self.matricula_usuario, mat[2])
                #self.conn.commit()
                messagebox.showinfo("Sucesso", "Matérias removidas com sucesso!")
                #self.master.mudar_frame(FrameMenu)
            except Exception as err:
                print(f"Erro ao executar a consulta: {err}")
                messagebox.showerror("Erro", f"Erro ao apagar as matérias: {err}")
        else:
            messagebox.showwarning("Aviso", "Nenhuma matéria foi selecionada para solicitar.")

        self.voltar_ao_menu()

    def verificar_historico(self, id_materia):
        try:
            historico_strategy = controle.Historico()
            resultado = historico_strategy.pesquisar(id_materia, self.matricula_usuario)
            return resultado is not None
        except Exception as err:
            print(f"Erro ao verificar histórico: {err}")
            return False

    def click(self, event, label, id_materia, nome_materia, pre_requisito):
        print(f"Label clicado: {label.cget('text')}, ID: {id_materia}, Pre: {pre_requisito}")
        if label.cget("bg") == self.active_color:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active_color)

    def voltar_ao_menu(self):
        self.master.destroy()

class FrameMostrarH:
    def __init__(self, master):
        self.master = master
        self.matricula_usuario = None
        self.labels = []
        
        self.mostrarh_frame = Frame(master)
        self.mostrarh_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_grade()

        self.active = "white"
        self.default_color = "white"
        
        self.populate_table()

    def criar_interface_grade(self):
        self.fonte = ("Verdana", "8")
        self.lbcadMatricula = Label(self.mostrarh_frame, text="Matricula", font=self.fonte, width=20)
        self.lbcadMatricula.pack(pady=10)

        self.txcadMatricula = Entry(self.mostrarh_frame, font=self.fonte, width=50)
        self.txcadMatricula.pack()
        
        self.btBuscarHistorico = Button(self.mostrarh_frame, text="Buscar Histórico", font=self.fonte, width=50, command=self.buscar_historico)
        self.btBuscarHistorico.pack(side=TOP)

        self.btVoltar = Button(self.mostrarh_frame, text="Voltar ao menu", font=self.fonte, width=50, command=self.voltar_ao_menu)
        self.btVoltar.pack(side=BOTTOM)  

    def fetch_data_from_db(self):
        matricula = self.txcadMatricula.get()
        historico_strategy = controle.Historico()
        return historico_strategy.get(matricula)

    def buscar_historico(self):
        matricula = self.txcadMatricula.get()

        if matricula:
            self.populate_table()
        else:
            messagebox.showwarning("Aviso", "Por favor, insira sua matrícula para buscar o histórico.")

    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.mostrarh_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["materia_nome", "nome_cursos"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=50, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))
                self.labels.append(label)

    def voltar_ao_menu(self):
        self.master.destroy()

    def click(self, event, label):
        print(f"Label clicado: {label.cget('text')}")
        if label["bg"] == self.active:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active)

class FrameSolicitarMateria:
    def __init__(self, master):
        self.master = master
        self.labels = []
        self.matricula_usuario = None
        self.active_color = "yellow"
        self.default_color = "white"
        self.active = self.active_color
        
        self.solicitar_materia_frame = Frame(master)
        self.solicitar_materia_frame.pack(expand=YES, fill=BOTH)

        self.obter_matricula_usuario()
    
    def obter_matricula_usuario(self):
        matricula_label = Label(self.solicitar_materia_frame, text="Digite sua matrícula:")
        matricula_label.pack()
        matricula_entry = Entry(self.solicitar_materia_frame)
        matricula_entry.pack()
        matricula_entry.focus_set()

        def salvar_matricula():
            self.matricula_usuario = matricula_entry.get()
            matricula_entry.pack_forget() 
            self.populate_table() 

        matricula_entry.bind("<Return>", lambda event: salvar_matricula())
    
    def fetch_data_from_db(self):
        grade_strategy = controle.Grade()
        return grade_strategy.pesquisar(self.matricula_usuario)

    def populate_table(self):
        self.solicitar_button = Button(self.solicitar_materia_frame, text="Solicitar", command=self.save_changes)
        self.solicitar_button.pack(side=BOTTOM)

        if not self.master.winfo_exists():
            return
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.solicitar_materia_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Nome_materia"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=20, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))
                self.labels.append(label)
                print(f"Label adicionado: {label.cget('text')}")
        
    def save_changes(self):
        try:
            for label in self.labels:
                materia_nome = label.cget("text")
                
                if label["bg"] == self.active:
                    materia_strategy = controle.Materia()
                    materia_id = materia_strategy.fetch_materia_id(materia_nome)  
                    materia_pre = materia_strategy.fetch_materia_pre(materia_nome)
                    grade = materia_nome, materia_id, materia_pre, self.matricula_usuario
                    
                    if materia_id is not None and materia_pre is not None:
                        grade_strategy = controle.Grade()
                        grade_strategy.inserir(grade)
                else:
                    print(f"Erro: Materia {materia_nome} não encontrada no banco")
            messagebox.showinfo("Sucesso", "Materias selecionadas foram salvas")
        except Exception as e:
            print(f"Erro durante a insercao no banco: {e}")
            messagebox.showerror("Erro", f"Erro ao inserir as materias no banco: {e}")
        finally:
            self.master.destroy()
            
    def voltar_ao_menu(self):
        self.master.destroy()

    def click(self, event, label):
        print(f"Label clicado: {label.cget('text')}")
        if label["bg"] == self.active_color:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active_color)

class FrameMostrarGrade:
    def __init__(self, master):
        self.master = master
        self.matricula_usuario = None
        self.labels = []
        
        self.mostrarh_frame = Frame(master)
        self.mostrarh_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_grade()

        self.active = "white"
        self.default_color = "white"
        
        self.populate_table()

    def criar_interface_grade(self):
        self.fonte = ("Verdana", "8")
        self.lbcadMatricula = Label(self.mostrarh_frame, text="Matricula", font=self.fonte, width=20)
        self.lbcadMatricula.pack(pady=10)

        self.txcadMatricula = Entry(self.mostrarh_frame, font=self.fonte, width=50)
        self.txcadMatricula.pack()
        
        self.btBuscarHistorico = Button(self.mostrarh_frame, text="Mostrar Grade", font=self.fonte, width=50, command=self.mostrar_grade)
        self.btBuscarHistorico.pack(side=TOP)

        self.btVoltar = Button(self.mostrarh_frame, text="Voltar ao menu", font=self.fonte, width=50, command=self.voltar_ao_menu)
        self.btVoltar.pack(side=BOTTOM)

    def fetch_data_from_db(self):
        matricula = self.txcadMatricula.get()

        grade_strategy = controle.Grade()
        return grade_strategy.get(matricula)

    def mostrar_grade(self):
        matricula = self.txcadMatricula.get()

        if matricula:
            self.populate_table()
        else:
            messagebox.showwarning("Aviso", "Por favor, insira sua matrícula para buscar a grade.")

    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.mostrarh_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Nome_materia"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=50, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))
                self.labels.append(label)

    def voltar_ao_menu(self):
        self.master.destroy()

    def click(self, event, label):
        print(f"Label clicado: {label.cget('text')}")
        if label["bg"] == self.active:
            label.config(bg=self.default_color)
        else:
            label.config(bg=self.active)

class FramePesquisa_Aluno:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_pesquisa()
        self.save_button = Button(master, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def criar_interface_pesquisa(self):
        self.fonte = ("Verdana", "8")

        self.btUser = Button(self.cadastro_frame, text="Materias", font=self.fonte, width=20, command=self.abrir_janela_pesquisa_materias)
        self.btUser.pack(pady=20)

        self.btUser = Button(self.cadastro_frame, text="Cursos", font=self.fonte, width=20, command=self.abrir_janela_pesquisa_cursos)
        self.btUser.pack(pady=20)
    
    def abrir_janela_pesquisa_materias(self):
        janela_pesquisa_materias = Toplevel()
        pesquisa_materias = FramePesquisa_Materias(janela_pesquisa_materias)

    def abrir_janela_pesquisa_cursos(self):
        janela_pesquisa_cursos = Toplevel()
        pesquisa_materias = FramePesquisa_Cursos(janela_pesquisa_cursos)

    def voltar_ao_menu(self):
        self.master.destroy()

class FramePesquisa_User:
    def __init__(self, master):
        self.master = master
        self.pesquisa_user_frame = Frame(master)
        self.pesquisa_user_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_pesquisa_user()

        self.active = "white"
        self.default_color = "white"
        
        self.save_button = Button(master, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def criar_interface_pesquisa_user(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.pesquisa_user_frame, text="Nome do Usuario", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.pesquisa_user_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.btCAD = Button(self.pesquisa_user_frame, text="Pesquisar", font=self.fonte, width=50, command=self.populate_table)
        self.btCAD.pack(pady=20)

    def fetch_data_from_db(self):
        nome = self.txcadNome.get()

        pessoa_strategy = controle.Pessoa()

        return pessoa_strategy.pesquisa(nome)

    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.pesquisa_user_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Nome", "Matricula", "Tipo"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=20, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))

    def voltar_ao_menu(self):
        self.master.destroy()

class FramePesquisa_Materias:
    def __init__(self, master):
        self.master = master
        self.pesquisa_materias_frame = Frame(master)
        self.pesquisa_materias_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_pesquisa_materias()

        self.active = "white"
        self.default_color = "white"
        
        self.save_button = Button(master, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def criar_interface_pesquisa_materias(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.pesquisa_materias_frame, text="Nome da Materia", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.pesquisa_materias_frame, font=self.fonte, width=60)
        self.txcadNome.pack()

        self.btCAD = Button(self.pesquisa_materias_frame, text="Pesquisar", font=self.fonte, width=50, command=self.populate_table)
        self.btCAD.pack(pady=20)
    
    def fetch_data_from_db(self):
        nomemateria = self.txcadNome.get()
        materia_strategy = controle.Materia()
        return materia_strategy.pesquisar(nomemateria)
    
    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.pesquisa_materias_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Id", "Nome_materia", "Pre", "Curso"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=30, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))

    def voltar_ao_menu(self):
        self.master.destroy()

class FramePesquisa_Cursos:
    def __init__(self, master):
        self.master = master
        self.pesquisa_cursos_frame = Frame(master)
        self.pesquisa_cursos_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_pesquisa_cursos()

        self.active = "white"
        self.default_color = "white"
        
        self.save_button = Button(master, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def criar_interface_pesquisa_cursos(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.pesquisa_cursos_frame, text="Nome do Curso", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.pesquisa_cursos_frame, font=self.fonte, width=60)
        self.txcadNome.pack()

        self.btCAD = Button(self.pesquisa_cursos_frame, text="Pesquisar", font=self.fonte, width=50, command=self.populate_table)
        self.btCAD.pack(pady=20)
    
    def fetch_data_from_db(self):
        nomecurso = self.txcadNome.get()
        curso_strategy = controle.Cursos()
        return curso_strategy.pesquisar(nomecurso)

    def populate_table(self):
        data = self.fetch_data_from_db()
        for row_data in data:
            row_frame = Frame(self.pesquisa_cursos_frame)
            row_frame.pack(expand=YES, fill=BOTH)
            for col_name in ["Nome_curso", "Turno"]:
                label = Label(row_frame, text=row_data[col_name], bg=self.default_color, width=30, height=1, borderwidth=0.5, relief="solid", padx=5)
                label.pack(side=LEFT, expand=YES, fill=BOTH)
                label.bind("<Button-1>", lambda event, label=label: self.click(event, label))

    def voltar_ao_menu(self):
        self.master.destroy()

class FrameInserir_Curso:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_inserir_curso()

    def criar_interface_inserir_curso(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text="Nome da Curso", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.lbcadID = Label(self.cadastro_frame, text="Turno", font=self.fonte, width=10)
        self.lbcadID.pack(pady=10)

        self.txcadID = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadID.pack()

        self.btCAD = Button(self.cadastro_frame, text="Inserir", font=self.fonte, width=50, command=self.inserir_curso)
        self.btCAD.pack(pady=20)        

    def inserir_curso(self):
        nome = self.txcadNome.get()
        turno = self.txcadID.get()

        curso = (nome, turno)

        curso_strategy = controle.Cursos()
        curso_strategy.inserir(curso)
        self.master.destroy()

class FrameInserir:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_inserir_materia()

    def criar_interface_inserir_materia(self):

        curso_strategy = controle.Cursos()
        cursos = curso_strategy.get()

        self.curso_selecionado = tk.StringVar()

        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text=" Nome da Materia", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.combobox = ttk.Combobox(self.cadastro_frame, textvariable=self.curso_selecionado, values=cursos)
        self.combobox.pack(pady=10)

        self.lbcadID = Label(self.cadastro_frame, text="ID da materia", font=self.fonte, width=10)
        self.lbcadID.pack(pady=10)

        self.txcadID = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadID.pack()

        self.lbcadTipo = Label(self.cadastro_frame, text="Pre-requisitos", font=self.fonte, width=20)
        self.lbcadTipo.pack(pady=10)

        self.txcadTipo = Entry(self.cadastro_frame, width=50, font=self.fonte)
        self.txcadTipo.pack()
        
        self.btCAD = Button(self.cadastro_frame, text="Inserir", font=self.fonte, width=50, command=self.inserir_materia)
        self.btCAD.pack(pady=20)        

    def inserir_materia(self):
        nome = self.txcadNome.get()
        id = self.txcadID.get()
        tipo = self.txcadTipo.get()
        curso = self.combobox.get()

        materia = (nome, id, tipo, curso)

        materia_strategy = controle.Materia()
        materia_strategy.inserir(materia)
        self.master.destroy()

class FrameRemover_Materia:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_remover_materia()

    def criar_interface_remover_materia(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text=" Nome da Materia", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=10)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.btCAD = Button(self.cadastro_frame, text="Remover", font=self.fonte, width=50, command=self.remover_materia)
        self.btCAD.pack(pady=20)        

    def remover_materia(self):
        nome = self.txcadNome.get()
        materia_strategy = controle.Materia()
        materia_strategy.remover(nome)
        
        self.master.destroy()

class FrameRemover_Curso:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_remover_curso()

    def criar_interface_remover_curso(self):
        self.fonte = ("Verdana", "8")
        self.lbcadNome = Label(self.cadastro_frame, text="Nome da Curso", font=self.fonte, width=20)
        self.lbcadNome.pack(pady=20)

        self.txcadNome = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadNome.pack()

        self.btCAD = Button(self.cadastro_frame, text="Remover", font=self.fonte, width=50, command=self.remover_curso)
        self.btCAD.pack(pady=20)        

    def remover_curso(self):
        nome = self.txcadNome.get()

        curso_strategy = controle.Cursos()
        curso_strategy.remover(nome)
        
        self.master.destroy()

class FrameRemover_User:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_remover_user()

    def criar_interface_remover_user(self):
        self.fonte = ("Verdana", "8")
        self.lbcadMatricula = Label(self.cadastro_frame, text="Matricula", font=self.fonte, width=20)
        self.lbcadMatricula.pack(pady=10)

        self.txcadMatricula = Entry(self.cadastro_frame, font=self.fonte, width=50)
        self.txcadMatricula.pack()

        self.btCAD = Button(self.cadastro_frame, text="Remover", font=self.fonte, width=50, command=self.remover_user)
        self.btCAD.pack(pady=20)        

    def remover(self):
        matricula = self.txcadMatricula.get()

        pessoa_strategy = controle.Pessoa()
        pessoa_strategy.remover(matricula)

        self.master.destroy()

class FramePesquisa:
    def __init__(self, master):
        self.master = master
        self.cadastro_frame = Frame(master)
        self.cadastro_frame.pack(expand=YES, fill=BOTH)
        self.criar_interface_pesquisa()
        self.save_button = Button(master, text="Voltar ao menu", command=self.voltar_ao_menu)
        self.save_button.pack(side=BOTTOM)

    def criar_interface_pesquisa(self):
        self.fonte = ("Verdana", "8")

        self.btUser = Button(self.cadastro_frame, text="Usuario", font=self.fonte, width=20, command=self.abrir_janela_pesquisa_user)
        self.btUser.pack(pady=20)

        self.btUser = Button(self.cadastro_frame, text="Materias", font=self.fonte, width=20, command=self.abrir_janela_pesquisa_materias)
        self.btUser.pack(pady=20)

        self.btUser = Button(self.cadastro_frame, text="Cursos", font=self.fonte, width=20, command=self.abrir_janela_pesquisa_cursos)
        self.btUser.pack(pady=20)

    def abrir_janela_pesquisa_materias(self):
        janela_pesquisa_materias = Toplevel()
        pesquisa_materias = FramePesquisa_Materias(janela_pesquisa_materias)

    def abrir_janela_pesquisa_cursos(self):
        janela_pesquisa_cursos = Toplevel()
        pesquisa_materias = FramePesquisa_Cursos(janela_pesquisa_cursos)

    def abrir_janela_pesquisa_user(self):
        janela_pesquisa_user = Toplevel()
        pesquisa_user = FramePesquisa_User(janela_pesquisa_user)        

    def voltar_ao_menu(self):
        self.master.destroy()

