from sqlalchemy.engine import url
from application import app, db
from application.models import Beds, Plants
from application.forms import AddBeds, AddPlants
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/mygarden')

def view_garden():
    beds = Beds.query.all()
    plants = Plants.query.all()
    return render_template('viewmygarden.html', beds=beds, plants=plants)


@app.route('/addbeds', methods = ['GET','POST'])

def add_beds():
    form = AddBeds()
    if request.method =='POST':
        name = form.bed_name.data
        length = form.bed_length.data
        width = form.bed_width.data
        aspect = form.bed_aspect.data
        if form.validate_on_submit:
            newbed = Beds(name=name, length=length, width=width, aspect=aspect)
            db.session.add(newbed)
            db.session.commit()
        return redirect(url_for('view_garden'))
    return render_template("addbed.html", form=form)

@app.route('/addplants', methods = ['GET','POST'])

def add_plants():
    form = AddPlants()
    beds = Beds.query.all()
    for bed in beds:
        form.plant_bed.choices.append(
            (bed.id, f"{bed.name}")
        )
    if request.method =='POST':
        name = form.plant_name.data
        plantbed = form.plant_bed.data
        if form.validate_on_submit:
            newplant = Plants(name=name, plantbed=plantbed, bed_id=bed.id)
            db.session.add(newplant)
            db.session.commit()
        return redirect(url_for('view_garden'))
    return render_template("addplant.html", form=form, beds=beds) 

@app.route('/deletebed/<int:id>')

def deletebed(id):
    bed = Beds.query.get(id)
    db.session.delete(bed)
    db.session.commit()
    return redirect(url_for('view_garden'))

@app.route('/deleteplant/<int:id>')

def deleteplant(id):
    plant = Plants.query.get(id)
    db.session.delete(plant)
    db.session.commit()
    return redirect(url_for('view_garden'))
       
