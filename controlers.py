from app import app
from flask import render_template,request,redirect
from models import *
from forms import *
import requests


@app.route('/')
def home():
    ScroolData = Scrool.query.all()
    data = requests.get('https://www.cbar.az/currencies/13.07.2023.xml')
    print(data)
    return render_template('home.html',ScroolData = ScroolData,data = data) 



@app.route('/Campaigns')
def get_products():
    category = request.args.get('category', 'All campaigns')  
    
    if category == 'All campaigns':
        products = Campaniya.query.all() 
    else:
        products = Campaniya.query.filter_by(category=category).all()  

    return render_template('Campaigns.html', products=products,category = category)

@app.route("/Campaigns/<int:id>")
def get_product(id):
    
    product = Campaniya.query.filter_by(id = id).all()
    return render_template("CampaignsItem.html",product = product)
@app.route('/Quest',methods = ["GET","POST"])
def Quest():
    form = SorguForm()
    if request.method == "POST":
        my_data = request.form
        form = SorguForm(data = my_data)
        if form.validate_on_submit():
            phoneNumber = form.phone.data
            phonePrefix = form.prefix.data
            
            print(phonePrefix)
            fulNumber = f"{phonePrefix}{phoneNumber}"
            contactdata = Sorgu(Branch = form.Branch.data,
                                Service = form.Service.data,
                                Date = form.Date.data,
                                Time = form.Time.data,
                                Phone = fulNumber)
            contactdata.save()
            # return redirect('/')
           
    return render_template('quest.html',form = form)
