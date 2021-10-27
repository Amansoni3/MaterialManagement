from django.shortcuts import render
from . import Pool
import uuid
import random
import os


def EmployeInterface(request):

    try:

        result=request.session['ADMIN']
        return render(request, "EmployeInterface.html")

    except Exception as e:

        return render(request,"AdminLogin.html")




def SubmitRecord(request):
    try:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        dob = request.POST['dob']
        paddress = request.POST['paddress']
        state = request.POST['state']
        city = request.POST['city']
        caddress = request.POST['caddress']
        email = request.POST['email']
        mnumber = request.POST['mnumber']
        designation = request.POST['designation']

        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]

        password = "".join(random.sample(['1', '2', '3', '4', '5', '@', '$', '#', '8', '88', '/', '9', 'a', 'v', 'l', 's', 'f', 'h', '2', 'w'], k=7))

        db, cmd = Pool.connectionPolling()

        q = "insert into employe(firstname, lastname, gender, dob, paddress, stateid, cityid, caddress, email, mnumber, designation, picture, password)values('{}','{}','{}','{}','{}',{},{},'{}','{}','{}','{}','{}','{}')".format(firstname, lastname, gender, dob, paddress, state, city, caddress, email, mnumber, designation, filename,password)

        cmd.execute(q)

        f = open("D:/MaterialManagement/assets/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "EmployeInterface.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "EmployeInterface.html", {'msg': "Record Not Submitted"})


def DisplayAll(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select E.*,(select C.cityname from cites C where C.cityid=E.cityid),(select S.statename from states S where S.stateid=E.stateid) from employe E"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayAllEmploye.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayAllEmploye.html", {'rows': []})


def Displayemployebyid(request):

    employeid = request.GET['employeid']

    try:
        db, cmd = Pool.connectionPolling()

        q = "select E.*,(select C.cityname from cites C where C.cityid=E.cityid),(select S.statename from states S where S.stateid=E.stateid) from employe E where employeid={}".format(employeid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "Displayemployebyid.html", {'row': row})

    except Exception as e:

        print("Error", e)

        return render(request, "Displayemployebyid.html", {'row': []})


def EditDeleteRecord(request):
    button = request.GET['button']

    empid = request.GET['empid']


    if (button == "EDIT"):
      firstname = request.GET['firstname']
      lastname = request.GET['lastname']
      gender = request.GET['gender']
      dob = request.GET['dob']
      paddress = request.GET['paddress']
      state = request.GET['state']
      city = request.GET['city']
      caddress = request.GET['caddress']
      email = request.GET['email']
      mnumber = request.GET['mnumber']
      designation = request.GET['designation']

      try:

        db, cmd = Pool.connectionPolling()

        q = "update employe set firstname='{}', lastname='{}', gender='{}', dob='{}', paddress='{}', stateid={}, cityid={}, caddress='{}', email='{}', mnumber='{}', designation='{}' where employeid={}".format(firstname, lastname, gender, dob, paddress, state, city, caddress, email, mnumber, designation, empid)

        cmd.execute(q)
        db.commit()
        db.close()

        return DisplayAll(request)

      except Exception as e:

        print("Error", e)
        return DisplayAll(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from employe where employeid={}".format(empid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayAll(request)

        except Exception as e:

            print("Error", e)

            return DisplayAll(request)

def EditEmployePicture(request):

    try:
        firstname = request.GET['firstname']
        lastname = request.GET['lastname']
        employeid = request.GET['employeid']
        picture=request.GET['picture']

        row=[employeid,firstname,lastname,picture]

        return render(request,"EditEmployePicture.html",{'row':row})

    except Exception as e:

        return render(request,"EditEmployePicture.html",{'row':[]})

def SaveEmployeeImage(request):
    try:
      employeid = request.POST['employeid']
      oldpic=request.POST['oldpic']
      picture = request.FILES['picture']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]


      q="update employe set picture='{}' where employeid={}".format(filename,employeid)

      db, cmd = Pool.connectionPolling()

      cmd.execute(q)
      F = open("D:/MaterialManagement/assets/"+filename, "wb")

      for chunk in picture.chunks():

          F.write(chunk)

      F.close

      db.commit()
      db.close()
      os.remove("D:/MaterialManagement/assets/"+oldpic)

      return DisplayAll(request)

    except Exception as e:
        print("Error:", e)
        return DisplayAll(request)