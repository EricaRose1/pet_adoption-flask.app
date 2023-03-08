from flask import Flask, request, render_template, redirect, session, flash, url_for, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "explorekey82"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

######################################################

@app.route('/')
def pets_list():
    pets = Pet.query.all()
    return render_template('/pets/homepage.html', pets=pets )

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    ''' add a pet form '''
    form = AddPetForm()

    if form.validate_on_submit():
        data = {k: v for k,v in form.data.items() if k != 'csrf_token'}
        new_pet = Pet(**data)
        db.session.add(new_pet)
        db.session.commit()
        flash(f'{{new_pet.name}} added!')
        return redirect(url_for('list_pets'))
    else:
        return render_template("/pets/add_pet_form.html", form=form)

@app.route("/<int:pet_id>", methods=['GET', 'POST'])
def edit_pet(pet_id):
    '''Edit pet.'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data

        db.session.commit()
        flash(f'{pet.name} updated!')
        return redirect('/')
    else:
        return render_template("edit_form.html", form=form, pet=pet)

@app.route("/api/pets/<int:pet_id>", methods=['GET'])
def api_get_pet(pet_id):
    """Return basic info about pet in JSON."""

    pet = Pet.query.get_or_404(pet_id)
    info = {"name": pet.name, "age": pet.age}

    return jsonify(info)











