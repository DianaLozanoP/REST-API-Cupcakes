"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

app.app_context().push()

connect_db(app)


@app.route('/')
def show_home_page():
    """Display home page to user, and display form"""
    form = AddCupcakeForm()
    return render_template('home_page.html', form=form)


@app.route('/api/cupcakes')
def show_all_cupcakes():
    """Show all the cupcakes data"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_data_cupcake(id):
    """Show data about an specific cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    json_cup = cupcake.serialize()
    return jsonify(cupcake=json_cup)


@app.route('/api/cupcakes', methods=["POST"])
def create_cupcake():
    """Post data about a new cupcake"""
    new_cupcake = Cupcake(flavor=request.json["flavor"], size=request.json[
                          "size"], rating=request.json["rating"], image=request.json["image"])
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcakes(id):
    """Update information about a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/todos/<int:id>', methods=["DELETE"])
def delete_cupcake(id):
    """Delete a cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Deleted")
