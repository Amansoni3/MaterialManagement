from django.shortcuts import render
from . import Pool
import uuid
import os

def ProductInterface(request):

    try:

        result=request.session['ADMIN']
        
        return render(request, "ProductInterface.html")

    except Exception as e:

        return render(request, "EmployeLogin.html")

def SubmitProduct(request):

    db, cmd = Pool.connectionPolling()
    try:
        I = request.POST['I']
        SCI = request.POST['SCI']
        PN = request.POST['PN']
        DI = request.POST['DI']
        GST = request.POST['GST']

        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]


        q = "insert into product(categoryid, subcategoryid, productname, description, gst, picture)values({},{},'{}','{}',{},'{}')".format(I,SCI,PN,DI,GST,filename)

        cmd.execute(q)

        f = open("D:/MaterialManagement/assets/ProductImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "ProductInterface.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "ProductInterface.html", {'msg': "Record Not Submitted"})

def DisplayProduct(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from product"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayProduct.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayProduct.html", {'rows': []})

def displayproductbyid(request):

    productid = request.GET["productid"]

    try:
        db, cmd = Pool.connectionPolling()

        q = "select p.*,(select c.categoryname from category c where c.categoryid=p.categoryid),(select sc.subname from subcategory sc where sc.subcategoryid=p.subcategoryid) from product p where productid={}".format(productid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "DisplayProductById.html", {'row': row})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayProductById.html", {'row': []})

def EditDeleteProduct(request):

    button = request.GET['button']
    productid = request.GET["productid"]

    if (button == "EDIT"):


      try:

        CI = request.GET["CI"]
        SCI = request.GET["SCI"]
        PN = request.GET["PN"]
        DI = request.GET["DI"]
        GST = request.GET["GST"]

        db, cmd = Pool.connectionPolling()

        q = "update product set categoryid={}, subcategoryid={},productname='{}', description='{}', gst={} where productid={}".format(CI,SCI,PN,DI,GST,productid)

        cmd.execute(q)
        print(q)
        db.commit()
        db.close()

        return DisplayProduct(request)

      except Exception as e:

        print("Error", e)
        return DisplayProduct(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from product where productid={}".format(productid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayProduct(request)

        except Exception as e:

            print("Error", e)

            return DisplayProduct(request)

def EditProductImages(request):

 try:

    productid = request.GET["productid"]
    productname = request.GET["productname"]
    picture = request.GET["picture"]

    row=[productid,productname,picture]

    return render(request, "EditProductImages.html", {'row': row})

 except Exception as e:
    print("Error",e)

    return render(request, "EditProductImages.html", {'row': []})

def SaveProductImage(request):
    try:
      productid = request.POST["productid"]
      picture = request.FILES['picture']
      oldpic=request.POST['oldpic']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]


      q="update product set picture='{}' where productid={}".format(filename,productid)

      db, cmd = Pool.connectionPolling()

      cmd.execute(q)
      F = open("D:/MaterialManagement/assets/ProductImages/"+filename, "wb")

      for chunk in picture.chunks():

          F.write(chunk)

      F.close

      db.commit()
      db.close()
      os.remove("D:/MaterialManagement/assets/ProductImages/"+oldpic)

      return DisplayProduct(request)

    except Exception as e:
        print("Error:", e)
        return DisplayProduct(request)