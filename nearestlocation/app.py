
app = Flask(__name__)



####################### new ########################
@app.route('/<string:name>')
def Home(name):
  return render_template('myTemplate.html', name=name)

