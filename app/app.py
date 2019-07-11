##==============================================================#
## SECTION: Imports                                             #
##==============================================================#

from flask import Flask, request, render_template
from flask_restful import Resource, Api

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

app = Flask(__name__)
api = Api(app)

#: Movie info is stored here. Could implement disk storage if wanted.
MOVIES = {}

##==============================================================#
## SECTION: Class Definitions                                   #
##==============================================================#

class Movies(Resource):
    def _prep(self, user):
        global MOVIES
        MOVIES.setdefault(user, [])
        print(f"MOVIES = {MOVIES}")
        self.movies = MOVIES
    def get(self, user):
        self._prep(user)
        return self.movies[user]
    def post(self, user, movie):
        self._prep(user)
        if movie not in self.movies[user]:
            self.movies[user].append(movie)
        return self.get(user)
    def delete(self, user, movie):
        self._prep(user)
        if movie in self.movies[user]:
            self.movies[user].remove(movie)
        return self.movies[user]
api.add_resource(Movies, '/api/movies/<string:user>', '/api/movies/<string:user>/<string:movie>')

##==============================================================#
## SECTION: Function Definitions                                #
##==============================================================#

@app.route('/')
def index():
    return render_template('index.html.jinja2')

@app.route('/user')
def user(name=None):
    name = request.args.get('name', None)
    return render_template('user.html.jinja2', name=name)

##==============================================================#
## SECTION: Global Definitions                                  #
##==============================================================#

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)
