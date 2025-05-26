from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models import Sucursal, Repartidor, Paquete, Transporte
from datetime import datetime
import random, string

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/acceso_despachante', methods=['GET', 'POST'])
def acceso_despachante():
    if request.method == 'POST':
        sucursal_id = request.form.get('sucursal_id')
        session['sucursal_id'] = sucursal_id
        sucursal = Sucursal.query.get(sucursal_id)
        if sucursal:
            session['sucursal'] = {'id': sucursal.id, 'numero': sucursal.numero, 'provincia': sucursal.provincia, 'localidad': sucursal.localidad}
        return redirect(url_for('opciones'))
    sucursales = Sucursal.query.all()
    return render_template('acceso_despachante.html', sucursales=sucursales)

@app.route('/registrar_paquete', methods=['GET', 'POST'])
def registrar_paquete():
    # Obtener la sucursal receptora seleccionada por el despachante
    sucursal_id = session.get('sucursal_id')
    sucursal = Sucursal.query.get(sucursal_id)
    
    if request.method == 'POST':
        peso = request.form.get('peso')
        nomdestinatario = request.form.get('nomdestinatario')
        dirdestinatario = request.form.get('dirdestinatario')
        
        # Generar automáticamente el número de envío
        numeroenvio = generar_numero_envio()
        
        # Crear un nuevo paquete y guardar en la base de datos
        paquete = Paquete(numeroenvio=numeroenvio, peso=peso, nomdestinatario=nomdestinatario,
                          dirdestinatario=dirdestinatario, entregado=False, idsucursal=sucursal_id)
        db.session.add(paquete)
        db.session.commit()
        
        flash('Registro de paquete exitoso. Número de envío: {}'.format(numeroenvio))
        return redirect(url_for('opciones'))
    
    return render_template('registrar_paquete.html', sucursal=sucursal)

def generar_numero_envio():
    # Generar un número de envío aleatorio (simulado)
    numero = random.randint(1, 9999)
    return f"{numero}"


@app.route('/salida_transporte', methods=['GET', 'POST'])
def salida_transporte():
    # Obtener la lista de sucursales y paquetes disponibles
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()

    if request.method == 'POST':
        sucursal_destino_id = request.form.get('sucursal_destino')
        paquetes_seleccionados = request.form.getlist('paquetes')

        if not sucursal_destino_id:
            flash('Seleccione una sucursal destino')
        else:
            # Generar un número de transporte único
            numero_transporte = generar_numero_transporte_unico()

            transporte = Transporte(numerotransporte=numero_transporte, idsucursal=sucursal_destino_id, fechahorasalida=datetime.now())
            db.session.add(transporte)

            for paquete_id in paquetes_seleccionados:
                paquete = Paquete.query.get(paquete_id)
                if paquete:
                    paquete.idtransporte = transporte.id

            try:
                db.session.commit()
                flash('Registro de transporte exitoso')
            except Exception as e:
                db.session.rollback()
                flash(f'Error al registrar el transporte: {e}')

            return redirect(url_for('opciones'))

    return render_template('salida_transporte.html', sucursales=sucursales, paquetes=paquetes)


def generar_numero_transporte_unico():
    return random.randint(200, 1000)
@app.route('/llegada_transporte/<int:idsucursal>', methods=['GET', 'POST'])
def llegada_transporte(idsucursal):
    print(f'ID de la Sucursal: {idsucursal}')  

    if request.method == 'POST':
        transporte_id = request.form.get('transporte_id')
        print(f'Transporte ID recibido: {transporte_id}')  
        if transporte_id:
            transporte = Transporte.query.filter_by(id=transporte_id, idsucursal=idsucursal).first()
            print(f'Transporte encontrado: {transporte}')  
            if transporte:
                transporte.fechahorallegada = datetime.now()
                try:
                    db.session.commit()
                    flash('Llegada registrada exitosamente', 'success')
                except Exception as e:
                    db.session.rollback()
                    flash(f'Error al registrar la llegada: {e}', 'danger')
            else:
                flash('Transporte no encontrado para la sucursal seleccionada', 'danger')
        else:
            flash('ID de transporte no proporcionado', 'danger')
        return redirect(url_for('llegada_transporte', idsucursal=idsucursal))

    transportes_pendientes = Transporte.query.filter_by(idsucursal=idsucursal, fechahorallegada=None).all()
    print(f'Transportes pendientes: {transportes_pendientes}') 
    print(f'ID de la Sucursal: {idsucursal}')# -
    return render_template('llegada_transporte.html', transportes=transportes_pendientes, idsucursal=idsucursal)


@app.route('/asignar_paquetes', methods=['GET', 'POST'])
def asignar_paquetes():
    # Obtener la sucursal del despachante (puedes pasarla como parámetro o recuperarla de la sesión)
    sucursal_id = obtener_sucursal_despachante()  # Esta función es un ejemplo, deberás implementarla

    # Obtener los repartidores y paquetes disponibles para la sucursal del despachante
    repartidores = Repartidor.query.filter_by(idsucursal=sucursal_id).all()
    paquetes_disponibles = Paquete.query.filter_by(idsucursal=sucursal_id, entregado=False, idrepartidor=None).all()

    if request.method == 'POST':
        # Obtener el repartidor seleccionado y los paquetes asignados
        idrepartidor = request.form['idrepartidor']
        paquetes_asignados = request.form.getlist('paquetes')

        # Asignar los paquetes al repartidor
        repartidor = Repartidor.query.get(idrepartidor)
        if repartidor:
            for paquete_id in paquetes_asignados:
                paquete = Paquete.query.get(paquete_id)
                if paquete:
                    paquete.repartidor = repartidor
            db.session.commit()
            flash('Paquetes asignados exitosamente.')
            return redirect(url_for('asignar_paquetes'))  # Redirecciona nuevamente a la página de asignación
        else:
            flash('Error: No se encontró el repartidor seleccionado.')
    return render_template('asignar_paquetes.html', repartidores=repartidores, paquetes=paquetes_disponibles)

def obtener_sucursal_despachante():
    return session.get('sucursal_id')


@app.route('/acceso_repartidor', methods=['GET', 'POST'])
def acceso_repartidor():
    if request.method == 'POST':
        numero_repartidor = request.form['numero_repartidor']
        dni = request.form['dni']
        repartidor = Repartidor.query.filter_by(numero=numero_repartidor, dni=dni).first()
        if repartidor:
            # Si el repartidor es válido, redirecciona a la vista de opciones de entrega
            return redirect(url_for('registrar_entrega', idrepartidor=repartidor.id))
        else:
            # Si los datos no corresponden a un repartidor registrado, muestra un mensaje de error
            error = 'Credenciales incorrectas'
            return render_template('acceso_repartidor.html', error=error)
    return render_template('acceso_repartidor.html')


@app.route('/registrar_entrega/<int:idrepartidor>', methods=['GET', 'POST'])
def registrar_entrega(idrepartidor):
    repartidor = Repartidor.query.get_or_404(idrepartidor)
    paquete = Paquete.query.filter_by(idrepartidor=idrepartidor, entregado=False).first()
    if request.method == 'POST':
        accion = request.form['accion']
        observaciones = request.form['observaciones']
        if paquete and accion == 'entregado':
            paquete.entregado = True
            paquete.observaciones = observaciones
            db.session.commit()
            mensaje = 'Paquete entregado con éxito.'
        elif paquete and accion == 'no_entregado':
            paquete.observaciones = observaciones
            db.session.commit()
            mensaje = 'Paquete marcado como no entregado.'
        else:
            mensaje = 'Error al procesar la acción.'
        return redirect(url_for('mensaje_entrega', idrepartidor=repartidor.id, mensaje=mensaje))
    return render_template('registrar_entrega.html', repartidor=repartidor, paquete=paquete)

@app.route('/mensaje_entrega/<int:idrepartidor>', methods=['GET'])
def mensaje_entrega(idrepartidor):
    repartidor = Repartidor.query.get_or_404(idrepartidor)
    mensaje = request.args.get('mensaje', 'No hay mensaje.')
    return render_template('mensaje_entrega.html', repartidor=repartidor, mensaje=mensaje)

@app.route('/opciones', methods=['GET', 'POST'])
def opciones():
    sucursal_id = session.get('sucursal_id')
    sucursal = session.get('sucursal')
    if request.method == 'POST':
        opcion = request.form.get('opcion')
        sucursal_id = session.get('sucursal_id')

        if not sucursal_id:
            flash('Error: No se ha seleccionado ninguna sucursal.')
            return redirect(url_for('acceso_despachante'))

        if opcion == 'registrar_paquete':
            return redirect(url_for('registrar_paquete', sucursal_id=sucursal_id))
        elif opcion == 'asignar_paquetes':
            return redirect(url_for('asignar_paquetes', sucursal_id=sucursal_id))
        elif opcion == 'llegada_transporte':
            return redirect(url_for('llegada_transporte', idsucursal=sucursal_id))
        elif opcion == 'salida_transporte':
            return redirect(url_for('salida_transporte', sucursal_id=sucursal_id))
        else:
            flash('Error: Opción no válida.')
            return redirect(url_for('opciones'))

    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    #return render_template('opciones.html', sucursales=sucursales)
    return render_template('opciones.html', sucursal_id=sucursal_id, sucursal=sucursal)
