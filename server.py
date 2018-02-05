import mimetypes
from flask import *
from calendar import month_name, month_abbr

exec(open('profile.py').read())
exec(open('linkedin.py').read())
exec(open('transaction.py').read())

app = Flask(__name__, template_folder='./')

with open('template.html', 'r') as template_file:
	template_html = template_file.read()

@app.route("/")
@app.route("/<path:path>")
def serve(path = "index.html"):
	if ".html" in path:
		mod_html = render_template(path, 
		forename=forename, lastname=lastname, name=forename+" "+lastname, birthDay=birthDay, 
		married=married, age=age, sex=sex, housePrice=housePrice, houseLow=houseLow, 
		houseHigh=houseHigh, religion="Buddhism", summary=summary, connectNum=connectNum, 
		employed=employed, salaryTotal=salaryTotal, jobInfo=jobInfo, month_name=month_name,
		ratio=ratio, credit=credit, debit=debit)
		return render_template('template.html', content=Markup(mod_html))
	try:
		file = open(path, 'r')
		return Response(file.read(), mimetype=mimetypes.guess_type(path, False)[0])
	except:
		with open(path, 'rb') as file:
			return Response(file.read(), mimetype=mimetypes.guess_type(path, False)[0])