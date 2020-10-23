
app = Flask(__name__)



####################### new ########################
@app.route('/<string:name>')
def index(name):
  return render_template('myTemplate.html', name=name)

