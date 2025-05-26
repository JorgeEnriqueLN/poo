from app import db


class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False) 
    provincia = db.Column(db.String(50), nullable=False)
    localidad = db.Column(db.String(50), nullable=False)
    direccion= db.Column(db.String(50),nullable=False)
    paquetes = db.relationship('Paquete', backref='sucursal', lazy=True, foreign_keys='Paquete.idsucursal')



class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.String(255), unique=True, nullable=False)
    peso = db.Column(db.Integer, nullable=False)
    nomdestinatario = db.Column(db.String(50), nullable=False)
    dirdestinatario = db.Column(db.String(50), nullable=False)
    entregado = db.Column(db.Boolean, default=False, nullable=False)    
    observaciones = db.Column(db.String(100), nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=False)
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=False)
   

class Repartidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20))
    nombre = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)


class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.String(20), nullable=False)
    fechahorasalida = db.Column(db.DateTime, nullable=True)
    fechahorallegada = db.Column(db.DateTime, nullable=True)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    
    sucursal = db.relationship('Sucursal', backref=db.backref('transportes', lazy=True))


# class Sucursal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     numero = db.Column(db.Integer)
#     provincia = db.Column(db.String(50))
#     localidad = db.Column(db.String(50))
#     direccion = db.Column(db.String(255))
# class Sucursal(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     numero = db.Column(db.Integer, nullable=False) 
#     provincia = db.Column(db.String(50), nullable=False)
#     localidad = db.Column(db.String(50), nullable=False)
#     direccion= db.Column(db.String(50),nullable=False)
#     paquetes = db.relationship('Paquete', backref='sucursal', lazy=True, foreign_keys='Paquete.idsucursal')

# class Paquete(db.Model):
#     __tablename__='paquete'
#     id= db.Column(db.Integer, primary_key= True)
#     numeroenvio= db.Column(db.String(255), unique=True, nullable=False)
#     peso= db.Column(db.Integer,nullable=False)
#     nomdestinatario= db.Column(db.String(50),nullable=False)
#     dirdestinatario= db.Column(db.String(50),nullable=False)
#     entregado= db.Column(db.String(10),nullable=False)
#     observaciones= db.Column(db.String(100),nullable=False)
#     idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
#     idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), nullable=False)
#     idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), nullable=False)
#     despachante_id = db.Column(db.Integer, db.ForeignKey('despachante.id'), nullable=False)


# class Despachante(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(50), nullable=False)
#     paquetes = db.relationship('Paquete', backref='despachante', lazy=True)

# class Repartidor(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     nombre = db.Column(db.String(50), nullable=False)
#     dni = db.Column(db.String(20), unique=True, nullable=False)
#     paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)
#     idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)


# class Transporte(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     numerotransporte = db.Column(db.String(20), nullable=False)
#     id_sucursal_origen = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
#     id_sucursal_destino = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)