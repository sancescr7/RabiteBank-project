from app import app
from flask import  render_template , request
from models import * 
from forms import *

@app.route('/')
def home():
    return render_template ('index.html')

@app.route('/xeberler')
def xeberler():
    catecory = request.args.get('catecory', 'Butun elanlar ')  
    
    if catecory == 'Butun elanlar ':
        xeberler = Xeberler.query.all() 
    else:
        xeberler = Xeberler.query.filter_by(catecory=catecory).all()  

    return render_template('xeberler.html', xeberler=xeberler,catecory = catecory)


# @app.route('/emanetler')
# def emanetler():
#     emanetler = Emanetler.query.all()
#     return render_template ('emanetler.html',emanetler=emanetler)

@app.route('/emanetler',methods = ["GET","POST"])
def emanetler():
    emanetler = Emanetler.query.all()
    form = EmanetlerSorguForm()
    if request.method == "POST":
        my_data = request.form
        form = EmanetlerSorguForm(data = my_data)
        if form.validate_on_submit():
            phoneNumber = form.phone.data
            phonePrefix = form.prefix.data
            
            fulNumber = f"{phonePrefix}{phoneNumber}"
            emanetlerdata = EmanetlerSorgu(Radio = form.Radio.data,
                                Name = form.Name.data,
                                Sorname = form.Sorname.data,
                                Phone = fulNumber)
            emanetlerdata.save()
            # return redirect('/')
           
    return render_template('emanetler.html',form = form, emanetler=emanetler)


@app.route('/detal/<int:id>')
def detal(id):
    detal = Xeberler.query.filter_by(id=id).all()
    return render_template ('detalxeber.html',detal=detal)