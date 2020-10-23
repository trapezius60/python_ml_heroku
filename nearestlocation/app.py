
app = Flask(__name__)



####################### new ########################
@app.route('/')
def index():
  return render_template('myTemplate.html')

