from flask import Flask,render_template,request,redirect,session
from DBConnection import Db
import datetime
app = Flask(__name__)
app.secret_key="123"
path=r"C:\Users\user\PycharmProjects\All For Canine\static\img\\"

@app.route('/')
def hello_world():
    return  render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/product')
def product():
    return render_template("product.html")

@app.route('/admin_home')
def admin_home():
    return render_template("admin/index.html")

@app.route('/singleblog')
def singleblog():
    return render_template("single-blog.html")



@app.route('/user_home')
def user_home():
    return render_template("user/index.html")
@app.route('/login',methods=['get','post'])
def login():
    if request.method=="POST":
        username=request.form['textfield']
        password=request.form['textfield2']
        db=Db()
        res=db.selectOne("select * from login WHERE username='"+str(username)+"' and password='"+str(password)+"' ")
        if res is not None:
            if res['usertype']=='admin':
                return redirect('/admin_home')
            session['lid']=res['loginid']
            if res['usertype']=='shop':
                return redirect('/shop_home')
            if res['usertype']=='user':
                session['lid']=res['loginid']
                return redirect('/user_home')
            else:
                return '<script>alert("invalid");window.location="/"</script>'
        else:
            return "invalid username"
    else:
        return render_template("admin/login.html")

@app.route('/logout')
def logout():
    return redirect('/')

@app.route('/viewandverifyshop')
def viewandverifyshop():
    db=Db()
    a=db.select("select * from shop,login where login.loginid=shop.shop_id and usertype='pending'")
    return render_template("admin/view & verify shop.html",data=a)
@app.route('/approvedshop/<g>')
def approvedshop(g):
    db=Db()
    db.update("update login set usertype='shop' where loginid='"+g+"'")
    return '<script>alert("approved");window.location="/viewandverifyshop"</script>'

@app.route('/rejectshop/<g>')
def rejectshop(g):
    db=Db()
    db.update("update login set usertype='rejected' where loginid='"+g+"'")
    return '<script>alert("rejected");window.location="/viewandverifyshop"</script>'
@app.route('/viewshop')
def viewshop():
    db=Db()
    a=db.select("select * from shop,login where login.loginid=shop.shop_id and (usertype='shop' or usertype='blocked')")
    return render_template("admin/view shop.html",data=a)
@app.route('/rating/<i>')
def rating(i):
    db=Db()
    aa=db.select("select *from rating,shop,user where user.user_id=rating.User_id and rating.Shop_id=shop.shop_id and shop.Shop_id='"+i+"'")
    ar_rt = []

    for im in range(0, len(aa)):
        val = str(aa[im]['Rating'])
        ar_rt.append(val)
    fs = "/static/star/full.jpg"
    hs = "/static/star/half.jpg"
    es = "/static/star/empty.jpg"
    arr = []

    for rt in ar_rt:
        print(rt)
        a = float(rt)

        if a >= 0.0 and a < 0.4:
            print("eeeee")
            ar = [es, es, es, es, es]
            arr.append(ar)

        elif a >= 0.4 and a < 0.8:
            print("heeee")
            ar = [hs, es, es, es, es]
            arr.append(ar)

        elif a >= 0.8 and a < 1.4:
            print("feeee")
            ar = [fs, es, es, es, es]
            arr.append(ar)

        elif a >= 1.4 and a < 1.8:
            print("fheee")
            ar = [fs, hs, es, es, es]
            arr.append(ar)

        elif a >= 1.8 and a < 2.4:
            print("ffeee")
            ar = [fs, fs, es, es, es]
            arr.append(ar)

        elif a >= 2.4 and a < 2.8:
            print("ffhee")
            ar = [fs, fs, hs, es, es]
            arr.append(ar)

        elif a >= 2.8 and a < 3.4:
            print("fffee")
            ar = [fs, fs, fs, es, es]
            arr.append(ar)

        elif a >= 3.4 and a < 3.8:
            print("fffhe")
            ar = [fs, fs, fs, hs, es]
            arr.append(ar)

        elif a >= 3.8 and a < 4.4:
            print("ffffe")
            ar = [fs, fs, fs, fs, es]
            arr.append(ar)

        elif a >= 4.4 and a < 4.8:
            print("ffffh")
            ar = [fs, fs, fs, fs, hs]
            arr.append(ar)

        elif a >= 4.8 and a <= 5.0:
            print("fffff")
            ar = [fs, fs, fs, fs, fs]
            arr.append(ar)
        print(arr)
    return render_template("admin/rating.html",resu=aa, r1=arr, ln=len(arr))

@app.route('/blockshop/<g>')
def blockshop(g):
    db=Db()
    db.update("update login set usertype='blocked' where loginid='"+g+"'")
    return '<script>alert("blocked");window.location="/viewshop"</script>'
@app.route('/unblockshop/<g>')
def unblockshop(g):
    db=Db()
    db.update("update login set usertype='shop' where loginid='"+g+"'")
    return '<script>alert("unblocked");window.location="/viewshop"</script>'
@app.route('/viewregistereduser')
def viewregistereduser():
    db=Db()
    a=db.select("select * from user,login where user.user_id=login.loginid")
    return render_template("admin/view registered user.html",data=a)
@app.route('/viewcomplaintandsendreply')
def viewcomplaintandsendreply():
    db=Db()
    a=db.select("select * from complaint,user where complaint.userid=user.User_id ")
    return render_template("admin/view complaint send reply.html",data=a)
@app.route('/changepassword',methods=['get','post'])
def changepassword():
    if request.method == "POST":
        currentpassword=request.form['textfield']
        newpassword=request.form['textfield2']
        confirmpassword=request.form['textfield3']
        db=Db()
        a=db.selectOne("select * from login WHERE password='"+currentpassword+"' and usertype='admin'")
        if a is not None:
            if newpassword==confirmpassword:
                db.update("update login set password='"+newpassword+" ' where usertype='admin' ")
                return '<script>alert("password changed");window.location="/admin_home"</script>'
            else:
                return'<script>alert("newpassword and confirmpassword are not equal");window.location="/"</script>'
        else:
            return'<script>alert("Incorrect password");window.location="/"</script>'
    return render_template("admin/change password.html")
@app.route('/breedadd',methods=['get','post'])
def breedadd():
    if request.method == "POST":
        Name=request.form['textfield2']
        Photo=request.files['fileField']
        Price=request.form['textfield']
        To=request.form['textfield3']
        date = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(r"C:\Users\user\PycharmProjects\All For Canine\static\img\\"+date+'.jpg')
        p = "/static/img/" + date + '.jpg'
        db = Db()
        db.insert( "insert into breed VALUES ('','" + Name + "','"+str(p)+"','" + Price + "','"+To+"')")
        return '<script>alert("Added successfully");window.location="/viewbreed"</script>'

    return render_template("admin/breed add.html")
@app.route('/viewbreed')
def viewbreed():
    db=Db()
    a=db.select("select * from breed")
    return render_template("admin/view breed.html",data=a)

@app.route('/deletebreed/<i>')
def deletebreed(i):
    db=Db()
    db.delete("delete from breed where Breed_id='"+i+"'")
    return '<script>alert("Deleted successfully");window.location="/viewbreed"</script>'

@app.route('/addfood/<bid>',methods=['get','post'])
def addfood(bid):
    if request.method=="POST":
        Name=request.form['textfield']
        Photo=request.files['fileField']
        Details=request.form['textfield2']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'

        db=Db()
        re = db.selectOne("select * from food WHERE food_name='"+Name+"' and Breed_id='"+str(bid)+"'")

        if re is None:
            db=Db()
            db.insert("insert into food(Food_id,Breed_id,Food_name,Food_photo,Food_details) values('','"+bid+"','"+Name+"','"+p+"','"+Details+"')")
            return '<script>alert("Added successfully");window.location="/viewbreed"</script>'
        else:
            return '<script>alert("ALREADY EXIST");window.location="/viewbreed"</script>'

    return render_template("admin/add food.html")
@app.route('/viewfood/<vf>')
def viewfood(vf):
    db=Db()
    a=db.select("select * from food,breed where food.Breed_id=breed.Breed_id and breed.Breed_id='"+vf+"'")
    return render_template("admin/view food.html",data=a)
@app.route('/deletefood/<df>')
def deletefood(df):
    db = Db()
    db.delete("delete from food where Breed_id='" + df + "'")
    return '<script>alert("Deleted successfully");window.location="/viewbreed"</script>'
@app.route('/viewdiseases/<vd>')
def viewdiseases(vd):
    db=Db()
    a=db.select("select * from diseases,breed where diseases.Breed_id=breed.Breed_id and breed.Breed_id='"+vd+"'")
    return render_template("admin/view diseases.html",data=a)
@app.route('/deletedisease/<dd>')
def deletedesease(dd):
    db = Db()
    db.delete("delete from diseases where Breed_id='" + dd + "'")
    return '<script>alert("Deleted successfully");window.location="/viewbreed"</script>'


@app.route('/adddiseases/<dd>',methods=['get','post'])
def adddiseases(dd):
    if request.method == "POST":
        Name=request.form['textfield']
        Photo=request.files['fileField']
        d=datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(path+d+'.jpg')
        p="/static/img/"+d+'.jpg'
        Symptoms=request.form['textfield2']
        Solutions=request.form['textfield3']
        db=Db()
        db.insert("insert into diseases VALUES ('','"+dd+"','"+Name+"','"+Symptoms+"','"+Solutions+"','"+p+"')")
        return '<script>alert("Added successfully");window.location="/viewbreed"</script>'
    else:
        return render_template("admin/add diseases.html")
@app.route('/sendreply/<d>',methods=['get','post'])
def sendreply(d):
    if request.method=="POST":
        reply=request.form['textarea']
        db=Db()
        db.update("update complaint set Reply='"+reply+"' ,Reply_date=curdate() where Complaint_id='"+d+"' ")
        return '<script>alert("sended");window.location="/viewcomplaintandsendreply"</script>'

    return render_template("admin/send reply.html")

# =========================================================================================================================================================================

# @app.route('/shopregistration')
# def shopregistration():
#     return render_template("admin/admin home.html")
@app.route('/shopadd',methods=['get','post'])
def shopadd():
    if request.method == "POST":
        shopname=request.form['textfield']
        email=request.form['textfield2']
        phonenumber=request.form['textfield3']
        Photo=request.files['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        lattitude = request.form['textfield5']
        longitude = request.form['textfield6']
        password = request.form['textfield7']
        db = Db()
        a=db.insert("insert into login values('','"+email+"','"+password+"','pending')")
        db.insert( "insert into shop VALUES ('"+str(a)+"','" + shopname + "','"+email+"','" + phonenumber + "','"+lattitude+"','"+longitude+"','"+p+"')")
        return '<script>alert("Added successfully");window.location="/"</script>'

    return render_template("shop/shop registration.html")

@app.route('/shop_home')
def shop_home():
    return render_template("shop/shop home.html")

@app.route('/view_profile')
def view_profile():
    db=Db()
    res=db.selectOne("select * from shop where shop_id='"+str(session['lid'])+"'")
    return render_template("shop/view profile.html", data=res)

@app.route('/viewprofileandupdate/<up>',methods=['get','post'])
def viewprofileandupdate(up):
    if request.method=="POST":
        shopname=request.form['textfield']
        email= request.form['textfield2']
        phonenumber= request.form['textfield3']
        photo = request.files['fileField']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'

        lattitude= request.form['textfield5']
        longitude= request.form['textfield6']
        db=Db()
        db.update("UPDATE shop set shop_name='"+shopname+"',shop_email='"+email+"',shop_phonenumber='"+phonenumber+"',shop_lattitude='"+lattitude+"',shop_longitude='"+longitude+"',shop_photo='"+p+"' where shop_id='"+up+"'")
        return '<script>alert("UPDATED");window.location="/view_profile"</script>'
    db=Db()
    res=db.selectOne("select * from shop where shop_id='"+up+"'")
    return render_template("shop/update_profile.html", data=res)

@app.route('/viewbreedd')
def viewbreedd():
    db=Db()
    res=db.select("select * from breed")
    return render_template("shop/view breed.html",data=res)


@app.route('/deletebreedd/<f>')
def deletebreedd(f):
    db=Db()
    db.delete("DELETE from breed where Breed_id='"+f+"'")
    return '<script>alert("DELETED");window.location="/viewbreedd"</script>'


@app.route('/viewfoodd')
def viewfoodd():
    db = Db()
    a = db.select("select * from food,breed WHERE food.Breed_id=breed.Breed_id")
    return render_template("shop/view food.html",data=a)

@app.route('/addaccessories',methods=['get','post'])
def addaccessories():
    if request.method=="POST":
        Name=request.form['textfield']
        Photo=request.files['fileField']
        Price=request.form['textfield2']
        Qty=request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db = Db()
        db.insert( "insert into accessories(A_id,Name,Photo,Price,Qty,SHOP_ID) values('','" + Name + "','" + p + "','" + Price + "','"+Qty+"','"+str(session['lid'])+"')")
        return '<script>alert("Added successfully");window.location="/viewaccessories"</script>'
    return render_template("shop/add accessories.html")

@app.route('/editaccessories/<ea>',methods=['get','post'])
def editaccessories(ea):
    if request.method=="POST":
        Name=request.form['textfield']
        Photo= request.files['fileField']
        Price = request.form['textfield2']
        Qty= request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        Photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db=Db()
        db.update("update accessories set Name='"+Name+"',Photo='"+p+"',Price='"+Price+"',Qty='"+Qty+"' where A_id='"+ea+"' ")
        return '<script>alert("UPDATED");window.location="/viewaccessories"</script>'
    db=Db()
    res = db.selectOne("select * from accessories where A_id='" + ea + "'")
    return render_template("shop/edit accessories.html",data=res)

@app.route('/viewaccessories')
def viewaccessories():
    db=Db()
    a=db.select("select * from accessories where SHOP_ID='"+str(session['lid'])+"'")
    return render_template("shop/view accessories.html",data=a)

@app.route('/deleteaccessories/<da>')
def deleteaccessories(da):
    db=Db()
    db.delete("DELETE from accessories WHERE A_id='"+da+"' ")
    return '<script>alert("DELETED");window.location="/viewaccessories"</script>'

@app.route('/addpets',methods=['get','post'])
def addpets():
    if request.method=="POST":
        choosebreed=request.form['textfield']
        photo=request.files['fileField']
        price=request.form['textfield2']
        details=request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db = Db()
        db.insert("insert into pets(Breed_id,P_photo,Price,Details,User_id,User_type) values('" + choosebreed + "','" + p + "','" + price + "','" + details + "','"+str(session['lid'])+"','shop')")
        return '<script>alert("Added successfully");window.location="/viewpets"</script>'
    db=Db()
    a=db.select("select * from breed")
    return render_template("shop/add pets.html",data=a)

@app.route('/editpets/<up>',methods=['get','post'])
def editpets(up):
    if request.method=="POST":
        choosebreed=request.form['textfield']
        photo=request.files['fileField']
        price=request.form['textfield2']
        details=request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db = Db()
        db.update("update pets set Breed_id='"+choosebreed+"',P_photo='"+p+"',Price='"+price+"',Details='"+details+"' where P_id='"+up+"'")
        return '<script>alert("UPDATED");window.location="/viewpets"</script>'
    db=Db()
    res=db.selectOne("select * from pets,breed WHERE pets.Breed_id=breed.Breed_id and P_id='"+up+"'")
    a = db.select("select * from breed")
    return render_template("shop/edit pets.html",data=res,data2=a)

@app.route('/viewpets')
def viewpets():
    db=Db()
    a=db.select("select * from pets,breed WHERE pets.Breed_id=breed.Breed_id  ")
    # user.user_id='"+str(session['lid'])+"'
    return render_template("shop/view pets.html",data=a)

@app.route('/deletepets/<dp>')
def deletepets(dp):
    db = Db()
    db.delete("delete from pets where P_id='" + dp + "'")
    return '<script>alert("Deleted successfully");window.location="/viewpets"</script>'

@app.route('/viewdisease')
def viewdisease():
    db = Db()
    a = db.select("select * from diseases,breed WHERE diseases.Breed_id=breed.Breed_id")
    return render_template("shop/view disease.html",data=a)

@app.route('/viewtodaypurchasehistory')
def viewtodaypurchasehistory():
    db = Db()
    a = db.select("select * from shop,ordered_accessories,user,accessories_booking,accessories where accessories_booking.Shop_id=shop.shop_id and accessories_booking.User_id=user.User_id  and accessories_booking.AB_id=ordered_accessories.OAB_id and ordered_accessories.AC_id=accessories.A_id  ")
    print(a)
    return render_template("shop/view today purchase history.html",data=a)

@app.route('/viewitems/<d>')
def viewitems(d):
    db = Db()
    a = db.select("select * from accessories WHERE A_id='"+d+"'")
    return render_template("shop/view items.html",data=a)

@app.route('/shopchangepasswordd',methods=['get','post'])
def shopchangepassword():
    if request.method=="POST":
        currentpassword=request.form['textfield']
        newpassword = request.form['textfield2']
        confirmpassword= request.form['textfield3']
        db=Db()
        a=db.selectOne("select * from login WHERE password='"+currentpassword+"' and loginid='"+str(session['lid'])+"'")
        if a is not None:
            if newpassword==confirmpassword:
                db.update("update login set password='"+newpassword+"' where loginid='"+str(session['lid'])+"'")
                return '<script>alert("PASSWORD CHANGED");window.location="/shop_home"</script>'
            else:

                return '<script>alert("NEW PASSWORD AND CONFIRM PASSWORD ARE NOT EQUAL");window.location="/shopchangepasswordd"</script>'
        else:
            return '<script>alert("INCORRECT PASSWORD");window.location="/shopchangepasswordd"</script>'
    else:
        return render_template('shop/change password.html')
@app.route('/viewpurchasehistory')
def viewpurchasehistory():
    db = Db()
    a = db.select("select * from shop,ordered_accessories,user,accessories_booking,accessories where accessories_booking.Shop_id=shop.shop_id and accessories_booking.User_id=user.User_id  and accessories_booking.AB_id=ordered_accessories.OAB_id and ordered_accessories.AC_id=accessories.A_id  ")
    print(a)
    return render_template("shop/view purchase history.html",data=a)
#====================================================================================================================================================================

# @app.route('/userregistration')
# def userregistration():
#     return render_template("admin/admin home.html")
@app.route('/useradd',methods=['get','post'])
def useradd():
    if request.method == "POST":
        username=request.form['textfield']
        email=request.form['textfield12']
        housename=request.form['textfield13']
        place= request.form['textfield4']
        post= request.form['textfield5']
        pin = request.form['textfield6']
        lattitude = request.form['textfield2']
        longitude = request.form['textfield3']
        phonenumber= request.form['textfield9']
        password = request.form['textfield10']
        db = Db()
        a=db.insert("insert into login values('','"+email+"','"+password+"','user')")
        db.insert( "insert into user VALUES ('"+str(a)+"','" + username + "','"+email+"','" + housename + "','"+place+"','"+post+"','"+pin+"','"+lattitude+"','"+longitude+"','"+phonenumber+"')")
        return '<script>alert("Register successfully");window.location="/"</script>'
    else:

        return render_template("user/user registration.html")


@app.route('/viewprofile')
def viewprofile():
    db=Db()
    res=db.selectOne("select * from user where user_id='"+str(session['lid'])+"'")
    return render_template("user/viewprofile .html",data=res)


@app.route('/update_profile/<uid>',methods=['get','post'])
def viewprofileandupdatee(uid):
    if request.method == "POST":
        username=request.form['textfield']
        email=request.form['textfield12']
        housename=request.form['textfield13']
        place= request.form['textfield4']
        post= request.form['textfield5']
        pin = request.form['textfield6']
        lattitude = request.form['textfield2']
        longitude = request.form['textfield3']
        phonenumber= request.form['textfield9']
        db = Db()
        db.update("update user set user_name='"+username+"',user_email='"+email+"',user_housename='"+housename+"',user_place='"+place+"',user_post='"+post+"',user_pin='"+pin+"',user_latitude='"+lattitude+"',user_longitude='"+longitude+"',user_phonenumber='"+phonenumber+"'where user_id='"+uid+"'")
        return '<script>alert("update successfully");window.location="/user_home"</script>'

    else:
        db=Db()
        res=db.selectOne("select *  from user where user_id='"+uid+"'")

        return render_template("user/update profile .html",data=res)


@app.route('/addpetss',methods=['get','post'])
def addpetss():
    if request.method == "POST":
        choosebreed = request.form['textfield']
        photo = request.files['fileField']
        price = request.form['textfield2']
        details = request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db = Db()
        db.insert("insert into pets(Breed_id,P_photo,Price,Details,User_id,User_type) values('" + choosebreed + "','" + p + "','" + price + "','" + details + "','" + str(
                session['lid']) + "','user')")
        return '<script>alert("Added successfully");window.location="/viewpetss"</script>'
    db = Db()
    a = db.select("select * from breed")

    return render_template('user/Add pets.html',data=a)
@app.route('/viewpetss')
def viewpetss():
    db=Db()
    a=db.select("select * from pets,breed WHERE pets.Breed_id=breed.Breed_id and pets.User_id='"+str(session['lid'])+"' ")
    # user.user_id='"+str(session['lid'])+"'
    return render_template("user/view pets.html",data=a)
@app.route('/pet_del/<d>')
def pet_del(d):
    db=Db()
    db.delete("delete from pets where P_id='"+d+"'")
    return '<script>alert("deleted successfully");window.location="/viewpetss"</script>'
@app.route('/uppetss/<up>',methods=['get','post'])
def uppetss(up):
    if request.method == "POST":
        choosebreed = request.form['textfield']
        photo = request.files['fileField']
        price = request.form['textfield2']
        details = request.form['textfield3']
        d = datetime.datetime.now().strftime("%y%m%d-%H%M%S")
        photo.save(path + d + '.jpg')
        p = "/static/img/" + d + '.jpg'
        db = Db()
        db.update("update pets set Breed_id='"+choosebreed+"',P_photo='"+str(p)+"',Price='"+price+"',Details='"+details+"'  where P_id='"+up+"'")
        return '<script>alert("updated successfully");window.location="/viewpetss"</script>'
    else:
        db=Db()
        res=db.selectOne("select * from pets where P_id='"+up+"'")
        r=db.select("select * from breed")
        return render_template('user/Edit pet.html',data=res,data2=r)
# @app.route('/add_to_cart')
# def addtocart():
#     return render_template("user/add to cart.html")


@app.route('/book/<gg>/<j>',methods=['get','post'])
def book(gg,j):
    if request.method == "POST":
        qty = request.form['textfield']
        if int(qty)<=int(j):
            db = Db()
            db.insert("insert into add_to_cart VALUES ('','" + str(session['lid']) + "','" + gg + "','" + qty + "')")
            return '<script>alert("booked successfully");window.location="/view_acessoriess/'+str( session['shopid'])+'"</script>'
        else:
            return '<script>alert("Invalid qty");window.location="/view_acessoriess/'+str( session['shopid'])+'"</script>'

    return render_template("user/book.html")

@app.route('/pet_book/<pb>',methods=['get','post'])
def pet_book(pb):

        db = Db()
        db.insert("insert into pets_booking VALUES ('','" + str(session['lid']) + "','" + pb + "',curdate(),'pending')")
        return '<script>alert("booked successfully");window.location="/view_others_pet_book"</script>'


@app.route('/removefromcart/<r>')
def removefromcart(r):
    db=Db()
    db.delete("delete from add_to_cart where C_id='" + r + "'")
    return '<script>alert("removed");window.location="/view_cart"</script>'

@app.route('/pay',methods=['get','post'])
def pay():
    return render_template("user/pay.html")
@app.route('/Payment_option_acessories',methods=['get','post'])
def Paymentoptionacessories():
    return render_template("user/Payment option acessories.html")
@app.route('/user_registration')
def userregistration():
    return render_template("user/user registration.html")

@app.route('/view_acessoriess/<i>',methods=['get','post'])
def viewaccessoriess(i):
    session['shopid']=i
    if request.method == 'POST':
        s=request.form['textfield']
        db = Db()
        res = db.select("select * from accessories where Name like '%"+s+"%' and SHOP_ID='"+str(i)+"'")
        return render_template("user/view accessories.html", data=res)
    db=Db()
    res=db.select("select * from accessories where SHOP_ID='"+str(i)+"' ")
    return render_template("user/view accessories.html",data=res)

@app.route('/add_to_cart/<add>/<j>',methods=['get','post'])
def add_to_cart(add,j):
    if request.method=="POST":
        qty=request.form['textfield']
        if int(qty) <= int(j):
            db=Db()
            db.insert("insert into add_to_cart VALUES ('','"+str(session['lid'])+"','"+add+"','"+qty+"')")
            return '<script>alert("addes successfully");window.location="/view_acessoriess/'+str( session['shopid'])+'"</script>'
        else:
            return '<script>alert("Invalid qty");window.location="/view_acessoriess/'+str( session['shopid'])+'"</script>'

    return render_template("user/Quantity.html",)
@app.route('/viewbooking')
def viewbooking():
    db = Db()
    res = db.select("select * from accessories_booking,shop,user where accessories_booking.shop_id=shop.shop_id and accessories_booking.User_id=user.User_id and accessories_booking.User_id='"+str(session['lid'])+"'")
    return render_template("user/view booking.html", data=res)
@app.route('/view_breeddd')
def viewbreeddd():
    db=Db()
    a=db.select("select * from breed")
    return render_template("user/View breed.html",data=a)
@app.route('/view_cart')
def viewcart():
    db = Db()
    a = db.select("select * from add_to_cart,accessories,accessories_booking,user,shop WHERE add_to_cart.A_id=accessories.A_id and user.user_id=add_to_cart.User_id and accessories_booking.shop_id=shop.shop_id and add_to_cart.User_id='"+str(session['lid'])+"'  ")
    return render_template("user/view cart.html",data=a)

@app.route('/book_now')
def booknow():
    db = Db()
    a = db.select("select * from add_to_cart,accessories where add_to_cart.A_id=accessories.A_id and add_to_cart.User_id='"+str(session['lid'])+"'")
    for i in a:
        q=db.selectOne("select * from accessories_booking where User_id='"+str(session['lid'])+"' and Shop_id='"+str(i['SHOP_ID'])+"'  ")
        if q is None:
            q2=db.insert("insert into accessories_booking(User_id,Shop_id,Date,Payment_status) values('"+str(session['lid'])+"','"+str(i['SHOP_ID'])+"',curdate(),'pending')")
            db.insert("insert into ordered_accessories(OAB_id,AC_id,Qty) values('"+str(q2)+"','"+str(i['A_id'])+"','"+str(i['Qty'])+"')")
            db.delete("delete from add_to_cart where C_id='"+str(i['C_id'])+"'")
        else:
            db.insert("insert into ordered_accessories(OAB_id,AC_id,Qty) values('" + str(q['AB_id']) + "','" + str(i['A_id']) + "','" + str(i['Qty']) + "')")
            db.delete("delete from add_to_cart where C_id='" + str(i['C_id']) + "'")
    return '<script>alert("Booked successfully");window.location="/Payment_option_acessories"</script>'

@app.route('/view_diseasse/<vd>')
def viewdiseasse(vd):
    db=Db()
    a=db.select("select * from diseases,breed where diseases.Breed_id=breed.Breed_id")
    return render_template("user/view disease.html",data=a)
@app.route('/view_food/<vf>')
def viewfooddd(vf):
    db=Db()
    a=db.select("select * from food,breed where food.Breed_id=breed.Breed_id")
    return render_template("user/view food.html",data=a)
@app.route('/view_items/<vi>')
def viewitemss(vi):
    db=Db()
    a=db.select("select * from accessories where A_id='"+vi+"'")
    return render_template("user/view items.html",data=a)

@app.route('/view_others_pet_book')
def viewotherspetbook():
    db = Db()
    a = db.select("select * from breed,pets,user WHERE pets.User_id=user.user_id and pets.Breed_id=breed.Breed_id")
    return render_template("user/view other's pet book.html",data=a)

@app.route('/view_pending_books_and_approval')
def viewpendingbooksandapproval():
    db=Db()
    a=db.select("select * from pets_booking,user,pets,breed where pets_booking.PB_user_id=user.user_id and pets_booking.PB_pet_id=pets.P_id and breed.Breed_id=pets.Breed_id and pets_booking.PB_status='pending'")
    return render_template("user/View pending books and approval.html",data=a)
@app.route('/petbookingstatus/<a>')
def petbookingstatus(a):
    db=Db()
    db.update("update pets_booking set PB_status='approved' where PB_id='"+a+"' ")
    return '<script>alert("Approved");window.location="/view_pending_books_and_approval"</script>'
@app.route('/rejectpet/<aa>')
def rejectpet(aa):
    db=Db()
    db.update("update pets_booking set PB_status='reject' where PB_id='"+aa+"' ")
    return '<script>alert("Rejected");window.location="/view_pending_books_and_approval"</script>'





@app.route('/view_pets_booking_history')
def viewpetbookinghistory():
    db = Db()
    a = db.select("select * from pets_booking,user,pets,breed where pets_booking.PB_user_id=user.user_id and pets_booking.PB_pet_id=pets.P_id and breed.Breed_id=pets.Breed_id")
    return render_template("user/View pets booking history.html",data=a)
@app.route('/view_pet_booking status')
def viewpetbookingstatus():
    db=Db()
    a= db.select(" select * from pets_booking,user,pets,breed where pets_booking.PB_user_id=user.user_id AND pets_booking.PB_pet_id=pets.P_id and pets.Breed_id=breed.Breed_id")
    return render_template("user/View  pets booking status.html",data=a)

@app.route('/view_shop')
def viewshopp():
    db=Db()
    res=db.select("select  * from shop")
    return render_template("user/view shop.html",data=res)

@app.route('/view_shop_pet/<r>')
def viewshoppets(r):
    db = Db()
    a = db.select("select * from pets,breed,shop where pets.Breed_id=breed.Breed_id and pets.User_id=shop.shop_id and pets.User_id='"+r+"'  ")
    return render_template("user/view shop pets.html",data=a)





if __name__ == '__main__':
    app.run()




