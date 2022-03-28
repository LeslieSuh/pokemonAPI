from flask import Flask, render_template, redirect
import helpers

# __name__ is EITHER the name of the file, minus the .py, or __main__ if it's the file currently being run

app = Flask(__name__)

# @ - a decorator (wraps a function with some extra functionality)
@app.route('/')
def home():
    return "The site is up and running!"

@app.route('/hello')
def say_hello():
    return render_template('hello.html', username='world')

@app.route('/hello/<name>')
def say_hello_to(name):
    return render_template('hello.html', username=name)

# @app.route('/pokemon')
# def pokemon_list():
#     return f"My pokemon: {helpers.get_random_pokemon_list()}"

@app.route('/pokemon')
def pokemon_list():
    return render_template('pokemon_list.html', pokemon_list=helpers.get_random_pokemon_list())

@app.route('/pokemon/<int:pokemon_id>')
def pokemon_info(pokemon_id):
    if pokemon_id not in helpers.FIRST_GEN_IDS:
        return redirect('/pokemon')
        pass
    pokemon = helpers.get_pokemon(pokemon_id)
    return render_template('pokemon_info.html', pokemon=pokemon)

app.run()