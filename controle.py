import persist
import visao
from tkinter import *
from tkinter import ttk, Frame, Button, Label, Canvas, TOP, W, BOTH, RIGHT, Y, messagebox
from abc import ABC, abstractmethod


#ControllerStrategy
class Strategy(ABC):

        @abstractmethod
        def inserir(self):
                pass        

        @abstractmethod
        def remover(self):
                pass

        @abstractmethod
        def pesquisar(self):
                pass

        @abstractmethod
        def get(self):
                pass   

class Controller():
        def __init__(self, strategy: Strategy, matricula):
            
                self.matricula = matricula
                self._strategy = strategy
        
        def strategy(self, strategy: Strategy):
                self._strategy = strategy

        def inserir(self): #informacoes = a o que forr inserido 
                self._strategy.inserir()

        def get(self):
                self._strategy.get()
        
        def remover(self): #= a tudo que pode ser removido 
                self._strategy.remover()

        def pesquisa(self):
                self._strategy.pesquisa()
                

class Pessoa(Strategy):
        def __init__(self):
                pass

        def get(self, matricula, senha):
                values = (matricula, senha)

                pessoa_dao = persist.Pessoa(persist.conn)
                tipo_usuario = pessoa_dao.get(values)

                if tipo_usuario == 'admin':
                        janela_menu_adm = Toplevel()
                        visao.FrameMenuAdm(janela_menu_adm)

                if tipo_usuario == 'estudante':
                        janela_menu = Toplevel()
                        visao.FrameMenu(janela_menu)

        def remover(self, matricula):
                pessoa_dao = persist.Pessoa(persist.conn)
                pessoa_dao.remover(matricula)

        def inserir(self, modelo):
                pessoa_dao = persist.Pessoa(persist.conn)
                pessoa_dao.inserir(modelo)
        
        def pesquisar(self, nome):
                pessoa_dao = persist.Pessoa(persist.conn)
                data = pessoa_dao.pesquisar(nome)
                return data
       
class Historico(Strategy):

        def __init__(self):
                pass

        def inserir(self, matricula_usuario, materia_id, materia_nome, materia_curso):
                historico_dao = persist.Historico(persist.conn)
                values = (matricula_usuario, materia_id, materia_nome, materia_curso)
                historico_dao.inserir(values)
                
        def remover(self, matricula, mat):
                values = (matricula, mat)
                historico_dao = persist.Historico(persist.conn)
                historico_dao.remover(values)

        def pesquisar(self, id_materia, matricula_usuario):
                values = (id_materia, matricula_usuario)
                historico_dao = persist.Historico(persist.conn)
                return historico_dao.pesquisar(values)
        
        def get(self, matricula):
                historico_dao = persist.Historico(persist.conn)
                data = historico_dao.get(matricula)
                return data
       
class Cursos(Strategy):

        def __init__(self):
                pass

        def inserir(self, curso):
                curso_dao = persist.Cursos(persist.conn)
                curso_dao.inserir(curso)

        def get(self):
                curso_dao = persist.Cursos(persist.conn)
                nomes_cursos = curso_dao.get()
                return nomes_cursos

        def remover(self, nome):
                curso_dao = persist.Cursos(persist.conn)
                curso_dao.remover(nome)
        
        def pesquisar(self, nomecurso):
                curso_dao = persist.Cursos(persist.conn)
                data = curso_dao.pesquisar(nomecurso)
                return data

class Grade(Strategy):

        def __init__(self):
                pass
        
        def inserir(self, grade):
                grade_dao = persist.Grade(persist.conn)
                grade_dao.inserir(grade)

        def get(self, matricula):
                grade_dao = persist.Grade(persist.conn)
                data = grade_dao.get(matricula)
                return data

        def pesquisar(self, matricula_usuario):
                grade_dao = persist.Grade(persist.conn)
                data = grade_dao.pesquisar(matricula_usuario)
                return data
        
        def remover(self):
                pass
        
class Materia(Strategy): 

        def __init__(self):
                pass       

        def get(self, curso_escolhido):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.get(curso_escolhido)
                return data

        def inserir(self, materia):
                materia_dao = persist.Materia(persist.conn)
                materia_dao.inserir(materia)

        def remover(self, nome):
                materia_dao = persist.Materia(persist.conn)
                materia_dao.remover(nome)

        def pesquisar(self, nomemateria):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.pesquisar(nomemateria)
                return data
        
        #dentro do get
        def fetch_data_from_db_remove(self, matricula):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.fetch_data_from_db_remove(matricula)
                return data

        def fetch_materia_pre(self, materia_nome):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.fetch_materia_pre(materia_nome)
                return data['Pre']

        def fetch_materia_curso(self, materia_nome):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.fetch_materia_curso(materia_nome)
                return data['Curso']
       
        def fetch_materia_id(self, materia_nome):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.fetch_materia_id(materia_nome)
                return data['Id']

        def fetch_materia_pre_id(self, id_materia):
                materia_dao = persist.Materia(persist.conn)
                data = materia_dao.fetch_materia_pre_id(id_materia)
                return data