from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


user = 'hppwioko'
password = 'Nyz365r8LNuKkR62MXMMGSJSag76phjo'
host = 'tuffi.db.elephantsql.com'
database = 'hppwioko'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "uma chave secreta bem secreta"


db = SQLAlchemy(app)


class Segunda(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_segunda():
        return Segunda.query.order_by(Segunda.idtarefa.asc()).all()

    @staticmethod
    def read_single_segunda(idtarefa_registro):
        return Segunda.query.get(idtarefa_registro)
    
    
    def save_segunda(self): 
        db.session.add(self) 
        db.session.commit()

    def update_segunda(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_segunda()

    def delete_segunda(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/segunda")
def read_all_segunda():
    
    registros = Segunda.read_all_segunda()
    return render_template("segunda.html", registros=registros)


@app.route("/create", methods=('GET', 'POST'))
def create_tarefa():
    novo_idtarefa = None

    if request.method == 'POST':
        form = request.form
        if form['dia'] == 'seg':
            registro = Segunda(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_segunda()
        elif form['dia'] == 'ter':
            registro = Terca(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_terca()
        elif form['dia'] == 'qua':
            registro = Quarta(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_quarta() 
        elif form['dia'] == 'qui':
            registro = Quinta(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_quinta() 
        elif form['dia'] == 'sex':
            registro = Sexta(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_sexta() 
        elif form['dia'] == 'sab':
            registro = Sabado(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_sabado() 
        elif form['dia'] == 'dom':
            registro = Domingo(form['tarefa'], form['dtagendamento'], form['observacao']) 
            registro.save_domingo()     

        novo_idtarefa = registro.idtarefa

    return render_template("create.html", novo_idtarefa=novo_idtarefa)


@app.route('/update_segunda/<idtarefa_registro>', methods=('GET', 'POST'))
def update_segunda(idtarefa_registro):
    sucesso = False

    registro = Segunda.read_single_segunda(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_segunda(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_segunda.html', registro=registro, sucesso=sucesso)


@app.route('/delete_segunda/<idtarefa_registro>')
def delete_segunda(idtarefa_registro):
    registro = Segunda.read_single_segunda(idtarefa_registro) 
    return render_template("delete_segunda.html", registro=registro)

@app.route('/delete_segunda/<idtarefa_registro>/confirmed')
def delete_segunda_confirmed(idtarefa_registro):
    sucesso = False 

    registro = Segunda.read_single_segunda(idtarefa_registro)

    if registro:
        registro.delete_segunda()
        sucesso = True

    return render_template("delete_segunda.html", registro=registro, sucesso=sucesso)

class Terca(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_terca():
        return Terca.query.order_by(Terca.idtarefa.asc()).all()

    @staticmethod
    def read_single_terca(idtarefa_registro):
        return Terca.query.get(idtarefa_registro)
    
    
    def save_terca(self): 
        db.session.add(self) 
        db.session.commit()

    def update_terca(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_terca()

    def delete_terca(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/terca")
def read_all_terca():
    
    registros = Terca.read_all_terca()
    return render_template("terca.html", registros=registros)


@app.route('/update_terca/<idtarefa_registro>', methods=('GET', 'POST'))
def update_terca(idtarefa_registro):
    sucesso = False

    registro = Terca.read_single_terca(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_terca(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_terca.html', registro=registro, sucesso=sucesso)


@app.route('/delete_terca/<idtarefa_registro>')
def delete_terca(idtarefa_registro):
    registro = Terca.read_single_terca(idtarefa_registro) 
    return render_template("delete_terca.html", registro=registro)

@app.route('/delete_terca/<idtarefa_registro>/confirmed')
def delete_confirmed_terca(idtarefa_registro):
    sucesso = False 

    registro = Terca.read_single_terca(idtarefa_registro)

    if registro:
        registro.delete_terca()
        sucesso = True

    return render_template("delete_terca.html", registro=registro, sucesso=sucesso)

class Quarta(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_quarta():
        return Quarta.query.order_by(Quarta.idtarefa.asc()).all()

    @staticmethod
    def read_single_quarta(idtarefa_registro):
        return Quarta.query.get(idtarefa_registro)
    
    
    def save_quarta(self): 
        db.session.add(self) 
        db.session.commit()

    def update_quarta(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento= nova_dtagendamento
        self.observacao = nova_observacao

        self.save_quarta()

    def delete_quarta(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/quarta")
def read_all_quarta():
    
    registros = Quarta.read_all_quarta()
    return render_template("quarta.html", registros=registros)



@app.route('/update_quarta/<idtarefa_registro>', methods=('GET', 'POST'))
def update_quarta(idtarefa_registro):
    sucesso = False

    registro = Quarta.read_single_quarta(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_quarta(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_quarta.html', registro=registro, sucesso=sucesso)


@app.route('/delete_quarta/<idtarefa_registro>')
def delete_quarta(idtarefa_registro):
    registro = Quarta.read_single_quarta(idtarefa_registro) 
    return render_template("delete_quarta.html", registro=registro)

@app.route('/delete_quarta/<idtarefa_registro>/confirmed')
def delete_confirmed_quarta(idtarefa_registro):
    sucesso = False 

    registro = Quarta.read_single_quarta(idtarefa_registro)

    if registro:
        registro.delete_quarta()
        sucesso = True

    return render_template("delete_quarta.html", registro=registro, sucesso=sucesso)


class Quinta(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_quinta():
        return Quinta.query.order_by(Quinta.idtarefa.asc()).all()

    @staticmethod
    def read_single_quinta(idtarefa_registro):
        return Quinta.query.get(idtarefa_registro)
    
    
    def save_quinta(self): 
        db.session.add(self) 
        db.session.commit()

    def update_quinta(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_quinta()

    def delete_quinta(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/quinta")
def read_all_quinta():
    
    registros = Quinta.read_all_quinta()
    return render_template("quinta.html", registros=registros)


@app.route('/update_quinta/<idtarefa_registro>', methods=('GET', 'POST'))
def update_quinta(idtarefa_registro):
    sucesso = False

    registro = Quinta.read_single_quinta(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_quinta(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_quinta.html', registro=registro, sucesso=sucesso)


@app.route('/delete_quinta/<idtarefa_registro>')
def delete_quinta(idtarefa_registro):
    registro = Quinta.read_single_quinta(idtarefa_registro) 
    return render_template("delete_quinta.html", registro=registro)

@app.route('/delete_quinta/<idtarefa_registro>/confirmed')
def delete_confirmed_quinta(idtarefa_registro):
    sucesso = False 

    registro = Quinta.read_single_quinta(idtarefa_registro)

    if registro:
        registro.delete_quinta()
        sucesso = True

    return render_template("delete_quinta.html", registro=registro, sucesso=sucesso)


class Sexta(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_sexta():
        return Sexta.query.order_by(Sexta.idtarefa.asc()).all()

    @staticmethod
    def read_single_sexta(idtarefa_registro):
        return Sexta.query.get(idtarefa_registro)
    
    
    def save_sexta(self): 
        db.session.add(self) 
        db.session.commit()

    def update_sexta(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_sexta()

    def delete_sexta(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/sexta")
def read_all_sexta():
    
    registros = Sexta.read_all_sexta()
    return render_template("sexta.html", registros=registros)



@app.route('/update_sexta/<idtarefa_registro>', methods=('GET', 'POST'))
def update_sexta(idtarefa_registro):
    sucesso = False

    registro = Sexta.read_single_sexta(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_sexta(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_sexta.html', registro=registro, sucesso=sucesso)


@app.route('/delete_sexta/<idtarefa_registro>')
def delete_sexta(idtarefa_registro):
    registro = Sexta.read_single_sexta(idtarefa_registro) 
    return render_template("delete_sexta.html", registro=registro)

@app.route('/delete_sexta/<idtarefa_registro>/confirmed')
def delete_confirmed_sexta(idtarefa_registro):
    sucesso = False 

    registro = Sexta.read_single_sexta(idtarefa_registro)

    if registro:
        registro.delete_sexta()
        sucesso = True

    return render_template("delete_sexta.html", registro=registro, sucesso=sucesso)


class Sabado(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_sabado():
        return Sabado.query.order_by(Sabado.idtarefa.asc()).all()

    @staticmethod
    def read_single_sabado(idtarefa_registro):
        return Sabado.query.get(idtarefa_registro)
    
    
    def save_sabado(self): 
        db.session.add(self) 
        db.session.commit()

    def update_sabado(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_sabado()

    def delete_sabado(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/sabado")
def read_all_sabado():
    
    registros = Sabado.read_all_sabado()
    return render_template("sabado.html", registros=registros)




@app.route('/update_sabado/<idtarefa_registro>', methods=('GET', 'POST'))
def update_sabado(idtarefa_registro):
    sucesso = False

    registro = Sabado.read_single_sabado(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_sabado(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_sabado.html', registro=registro, sucesso=sucesso)


@app.route('/delete_sabado/<idtarefa_registro>')
def delete_sabado(idtarefa_registro):
    registro = Sabado.read_single_sabado(idtarefa_registro) 
    return render_template("delete_sabado.html", registro=registro)

@app.route('/delete_sabado/<idtarefa_registro>/confirmed')
def delete_confirmed_sabado(idtarefa_registro):
    sucesso = False 

    registro = Sabado.read_single_sabado(idtarefa_registro)

    if registro:
        registro.delete_sabado()
        sucesso = True

    return render_template("delete_sabado.html", registro=registro, sucesso=sucesso)

class Domingo(db.Model):
    idtarefa = db.Column(db.Integer, primary_key=True)
    tarefa = db.Column(db.String(200), nullable=False)
    dtagendamento = db.Column(db.Date, nullable=True)
    observacao = db.Column(db.String(200), nullable=True)

    def __init__(self, tarefa, dtagendamento, observacao):
        self.tarefa = tarefa
        self.dtagendamento = dtagendamento
        self.observacao = observacao
    
    @staticmethod
    def read_all_domingo():
        return Domingo.query.order_by(Domingo.idtarefa.asc()).all()

    @staticmethod
    def read_single_domingo(idtarefa_registro):
        return Domingo.query.get(idtarefa_registro)
    
    
    def save_domingo(self): 
        db.session.add(self) 
        db.session.commit()

    def update_domingo(self, nova_tarefa, nova_dtagendamento, nova_observacao):
        self.tarefa = nova_tarefa
        self.dtagendamento = nova_dtagendamento
        self.observacao = nova_observacao

        self.save_domingo()

    def delete_domingo(self):
        db.session.delete(self)
        db.session.commit()


@app.route("/domingo")
def read_all_domingo():
    
    registros = Domingo.read_all_domingo()
    return render_template("domingo.html", registros=registros)



@app.route('/update_domingo/<idtarefa_registro>', methods=('GET', 'POST'))
def update_domingo(idtarefa_registro):
    sucesso = False

    registro = Domingo.read_single_domingo(idtarefa_registro)

    if request.method == 'POST':
        form = request.form 
        
        
        registro.update_domingo(form['tarefa'], form['dtagendamento'], form['observacao']) 
        

        sucesso = True
    
    return render_template('update_domingo.html', registro=registro, sucesso=sucesso)


@app.route('/delete_domingo/<idtarefa_registro>')
def delete_domingo(idtarefa_registro):
    registro = Domingo.read_single_domingo(idtarefa_registro) 
    return render_template("delete_domingo.html", registro=registro)

@app.route('/delete_domingo/<idtarefa_registro>/confirmed')
def delete_confirmed_domingo(idtarefa_registro):
    sucesso = False 

    registro = Domingo.read_single_domingo(idtarefa_registro)

    if registro:
        registro.delete_domingo()
        sucesso = True

    return render_template("delete_domingo.html", registro=registro, sucesso=sucesso)

class Anotacoes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    anotacao = db.Column(db.String(255), nullable=False)


    def __init__(self, anotacao):
        self.anotacao = anotacao

    @staticmethod
    def read_all_anotacao():
        return Anotacoes.query.order_by(Anotacoes.id.asc()).all()

    @staticmethod
    def read_single_anotacao(idtarefa_registro):
        return Anotacoes.query.get(idtarefa_registro)
    
    
    def save_anotacao(self): 
        db.session.add(self) 
        db.session.commit()


    def delete_anotacao(self):
        db.session.delete(self)
        db.session.commit()

@app.route("/anotacoes")
def read_all_anotacoes():
    
    registros = Anotacoes.read_all_anotacao()
    return render_template("anotacoes.html", registros=registros)

@app.route('/delete_anotacoes/<id_registro>')
def delete_anotacao(id_registro):
    sucesso = False 

    registro = Anotacoes.read_single_anotacao(id_registro)

    if registro:
        registro.delete_anotacao()
        sucesso = True
    return render_template("delete_anotacoes.html", registro=registro)

@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == "POST":
        form = request.form
        registro = Anotacoes(form['anotacao']) 
        registro.save_anotacao()

    return render_template("index.html")

if (__name__ == "__main__"):
    app.run(debug=True)