
app = Flask(__name__)



####################### new ########################
@app.route('/')
def index(name):
  return render_template('myTemplate.html', name=name)

