import mysql.connector
from tkinter import *
import tkinter as tk
from tkinter import ttk, Frame, Button, Label, Canvas, TOP, W, BOTH, RIGHT, Y, messagebox
import visao
import controle
from abc import ABC, abstractmethod

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P4sswd!",
    database="Software_APS",
    charset="utf8"
)

class DAO(ABC):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    @abstractmethod
    def inserir(self, modelo, curso, grade):
        pass

    @abstractmethod
    def pesquisar(self, nome, materia, matricula):
        pass

    @abstractmethod
    def remover(self, nome, matricula):
        pass

    @abstractmethod
    def get(self, values):
        pass
  
class Pessoa(DAO):
    def __init__(self, conn):
        super().__init__(conn)

    def get(self, values):
        matricula, senha = values
        try:
            self.cursor.execute("SELECT * FROM PESSOA WHERE Matricula = %s AND Senha = %s", (matricula, senha))
            usuario = self.cursor.fetchone()

            if usuario:
                tipo_usuario = usuario[2]
                return tipo_usuario
            else:
                messagebox.showerror("Erro de Login", "Credenciais inválidas. Tente novamente.")
                return None
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao conectar ao banco de dados: {err}")
            return None
        
    def inserir(self, modelo_inserir):
        nome, matricula, tipo, senha = modelo_inserir

        try:
            query = "INSERT INTO PESSOA (Nome, Matricula, Tipo, Senha) VALUES (%s, %s, %s, %s)"
            values = (nome, matricula, tipo, senha)
            self.cursor.execute(query, values)
            self.conn.commit()
            messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro ao Cadastrar Usuário", f"Erro ao cadastrar usuário: {err}")

    def pesquisar(self, nome):
        self.cursor.execute("SELECT Nome, Matricula, Tipo FROM PESSOA WHERE Nome REGEXP %s", (nome,))
        columns = [desc[0] for desc in self.cursor.description]
        data = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
        return data

    def remover(self, matricula):
        try:
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")
            self.cursor.execute("DELETE FROM PESSOA WHERE Matricula = %s", (matricula,))
            self.conn.commit()
            messagebox.showinfo("Remoção", "Usuário removido com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro ao Remover Usuário", f"Erro ao remover usuário: {err}")
        finally:
            self.cursor.close()

class Materia(DAO):
    def __init__(self, conn):
        super().__init__(conn)

    def inserir(self, materia):
        nome, id, tipo, curso = materia
        try:
            cursor = conn.cursor()
            query = "INSERT INTO MATERIAS (Nome_materia, ID, Pre, Curso) VALUES (%s, %s, %s, %s)"
            values = (nome, id, tipo, curso)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            messagebox.showinfo("Cadastro", "Materia cadastrada com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar materia: {err}")            

    def remover(self, nome):
        try:
            self.cursor = conn.cursor()
            self.cursor.execute("SET FOREIGN_KEY_CHECKS=0")    
            self.cursor.execute("DELETE FROM MATERIAS WHERE Nome_materia = %s", (nome,))
            conn.commit()
            self.cursor.close()
            messagebox.showinfo("Remoção", "Materia removida com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao remover materia: {err}")
            
    def get(self, curso_escolhido):
        self.cursor = conn.cursor(dictionary=True)
        self.cursor.execute("SELECT Nome_materia, Id, Pre, Curso FROM MATERIAS WHERE Curso = %s", (curso_escolhido, ))
        resultados = self.cursor.fetchall()

        data = [
        {"Nome_materia": resultado["Nome_materia"], "Id": resultado["Id"], "Pre": resultado["Pre"]}
        for resultado in resultados
        ] 
        self.cursor.close()
        
        return data

    def fetch_materia_pre(self, materia_nome):
        self.cursor = conn.cursor(dictionary=True)
     
        self.cursor.execute("SELECT Pre FROM MATERIAS WHERE Nome_materia = %s", (materia_nome,))
        materia_pre = self.cursor.fetchone()
        self.cursor.close()
        
        return materia_pre if materia_pre else None

    def fetch_materia_id(self, materia_nome):
        self.cursor = conn.cursor(dictionary=True)

        self.cursor.execute("SELECT Id FROM MATERIAS WHERE Nome_materia = %s", (materia_nome,))
        materia_id = self.cursor.fetchone()
        self.cursor.close()
        
        return materia_id

    def fetch_materia_curso(self, materia_nome):
        self.cursor = conn.cursor(dictionary=True)

        self.cursor.execute("SELECT Curso FROM MATERIAS WHERE Nome_materia = %s", (materia_nome,))
        materia_curso = self.cursor.fetchone()
        self.cursor.close()
        
        return materia_curso if materia_curso else None

    def fetch_data_from_db_remove(self, matricula):     
        self.cursor = conn.cursor(dictionary=True)
        query = ("SELECT Id, Nome_materia, Pre, Curso FROM MATERIAS "
              "WHERE Id IN (SELECT materia_id FROM HISTORICO WHERE matricula_usuario = %s)")
        self.cursor.execute(query, (matricula,))
        data = self.cursor.fetchall()
     
        self.cursor.close()
        
        return data

    def fetch_materia_pre_id(self, id_materia):
        self.cursor = conn.cursor(dictionary=True)
     
        self.cursor.execute("SELECT Pre FROM MATERIAS WHERE Id = %s", (id_materia,))
        materia_pre = self.cursor.fetchone()
        self.cursor.close()
        
        return materia_pre[0] if materia_pre else None

    def pesquisar(self, nomemateria):
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT Nome_materia, Id, Pre, Curso FROM MATERIAS WHERE Nome_materia REGEXP (%s)",(nomemateria, ))
        data = cursor.fetchall()
        cursor.close()
        return data

class Historico(DAO):
    def __init__(self, conn):
        super().__init__(conn)

    def inserir(self, values):
        matricula_usuario, materia_id, materia_nome, materia_curso = values
        self.cursor = conn.cursor(dictionary=True)

        query = "INSERT INTO HISTORICO(matricula_usuario, materia_id, materia_nome, nome_cursos) VALUES (%s, %s, %s, %s)"
        values = (matricula_usuario, materia_id, materia_nome, materia_curso)
        self.cursor.execute(query, values)
        print(f"Insercao bem-sucedida para a matéria: {materia_nome}")
        conn.commit()
        if conn is None:
                print(f"Erro: Nao ha conexao")
                messagebox.showerror("Erro", "Não há conexão o banco!")
                return
        self.cursor.close()

    def pesquisar(self, values):
        id_materia, matricula_usuario = values
        self.cursor = conn.cursor()
        self.cursor.execute("SELECT materia_id FROM HISTORICO WHERE matricula_usuario = %s AND materia_id = %s",
                           (matricula_usuario, id_materia))
        resultado = self.cursor.fetchone()
        self.cursor.close()
        
        return resultado

    def remover(self, values):
        matricula, mat = values

        self.cursor = conn.cursor(dictionary=True)
        query_delete = "DELETE FROM HISTORICO WHERE (matricula_usuario = %s) AND (materia_nome = %s)"
        self.cursor.execute(query_delete, (matricula, mat)) 
        conn.commit()
        self.cursor.close()
        
    def get(self, matricula):
        self.cursor = conn.cursor(dictionary=True)
        self.cursor.execute("SELECT * FROM HISTORICO WHERE matricula_usuario = %s", (matricula, ))
        data = self.cursor.fetchall()
        self.cursor.close()
        return data
    
class Cursos(DAO):
    def __init__(self, conn):
        super().__init__(conn)

    def pesquisar(self, nomecurso):
        self.cursor = conn.cursor(dictionary=True)
        self.cursor.execute("SELECT Nome_curso, Turno FROM CURSOS WHERE Nome_curso REGEXP (%s)",(nomecurso, ))
        data = self.cursor.fetchall()
        self.cursor.close()
        return data

    #obter_cursos 
    def get(self):
        self.cursor = conn.cursor()
        query = "SELECT Nome_curso FROM CURSOS"
        self.cursor.execute(query)
        resultados = self.cursor.fetchall()

        nomes_cursos = [resultado[0] for resultado in resultados]
        return nomes_cursos

    #inserir_cursos
    def inserir(self, curso):
        nome, turno = curso
        try:
            self.cursor = conn.cursor()
            query = "INSERT INTO CURSOS (Nome_curso, Turno) VALUES (%s, %s)"
            values = (nome, turno)
            self.cursor.execute(query, values)
            conn.commit()
            self.cursor.close()
            messagebox.showinfo("Cadastro", "Curso cadastrado com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar curso: {err}")            

    def remover(self, nome):
        try:
            cursor = conn.cursor()
            cursor.execute("SET FOREIGN_KEY_CHECKS=0")    
            cursor.execute("DELETE FROM CURSOS WHERE Nome_curso = %s", (nome,))
            conn.commit()
            cursor.close()
            messagebox.showinfo("Remoção", "Curso removido com sucesso!")
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao remover materia: {err}")            
     
class Grade(DAO):
    def __init__(self, conn):
        super().__init__(conn)

    def inserir(self, grade):
        materia_nome, materia_id, materia_pre, matricula_usuario = grade
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO nova_grade VALUES (%s, %s, %s, %s)"
                values = (materia_nome, materia_id, materia_pre, matricula_usuario)
                cursor.execute(query, values)
                print(f"Inserção bem-sucedida para a matéria: {materia_nome}")
                conn.commit()
        except mysql.connector.Error as err:
            print(f"Erro MySQL durante a inserção: {err}")
            print(f"Código de erro MySQL: {err.errno}")
            print(f"Mensagem do erro MySQL: {err.msg}")
            messagebox.showerror("Erro", f"Erro ao inserir as matérias no banco: {err}")        

    def get(self, matricula):
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM nova_grade WHERE matricula_usuario = %s", (matricula, ))
        data = cursor.fetchall()
        cursor.close()
        return data                    

    def pesquisar(self, matricula_usuario):
        self.cursor = conn.cursor(dictionary=True)
        self.cursor.execute("SELECT Id, Nome_materia, Pre, Curso FROM MATERIAS "
             "WHERE (Id NOT IN (SELECT materia_id FROM HISTORICO WHERE matricula_usuario = %s)) AND (Curso = 'Ciencia da Computacao')", (matricula_usuario, ))
        data = self.cursor.fetchall()
        self.cursor.close()
        
        return data 

    def remover(self):
        pass
