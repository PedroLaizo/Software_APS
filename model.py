class Pessoa:
    def __init__(self, nome, idade, matricula, tipo):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.tipo = tipo

class Materia:
    def __init__(self, nome, id_materia, pre_req, curso):
        self.nome = nome
        self.id_materia = id_materia
        self.pre_req = pre_req
        self.curso = curso

class Historico:
    def __init__(self, id_aluno, id_materia, curso_nome):
        self.id_aluno = id_aluno
        self.id_materia = id_materia
        self.curso_nome = curso_nome

class Cursos:
    def __init__(self, nome_curso, turno):
        self.nome_curso = nome_curso
        self.turno = turno

class Grade:
    def __init__(self, nome_materia, id_materia, matricula):
        self.nome_materia = nome_materia
        self.id_materia = id_materia
        self.matricula = matricula

# Se houver persistência, você pode adicionar uma classe para lidar com isso aqui
