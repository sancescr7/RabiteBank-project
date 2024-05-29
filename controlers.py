from app import app
from flask import render_template,request,redirect
from models import *
from forms import *
from flask_login import login_user,login_required,logout_user
import requests
import xml.etree.ElementTree as ET



@app.route('/')
def home():
    ScroolData = Scrool.query.all()
    url = "https://www.cbar.az/currencies/13.07.2023.xml"
    response = requests.get(url)
    currencies = []

    if response.status_code == 200:
        # try:
            root = ET.fromstring(response.content)
            for valtype in root.findall('.//ValType'):
                valtype_name = valtype.attrib.get('Type', 'Unknown Type')
                for valute in valtype.findall('Valute'):
                    name = valute.find('Name').text
                    value = valute.find('Value').text
                    # bank_selling = valute.find('BankSelling').text if valute.find('BankSelling') is not None else "N/A"
                    currencies.append({
                        'type': valtype_name,
                        'name': name,
                        'value': value,
                        'bank_selling':  round(float(value) * 1.003,4),
                        'satıs': round(float(value) * 1.04,4)
                    })
    #     except ET.ParseError as e:
    #         print("Ошибка парсинга XML:", e)
    # else:
    #     print(f"Ошибка: {response.status_code}")
    #     print("Ответ сервера:", response.text)
    currencies
    x = slice(4,9)
    # print(currencies[x])

    return render_template('home.html',ScroolData = ScroolData,currencies = currencies[x] ) 
  



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

@app.route('/login')
def login():
    user = User.query.get(1)
    login_user(user)
    return 'logedd !'

@app.route('/logout')
@login_required
def logo():

    logout_user()
    return 'user loggout !'

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