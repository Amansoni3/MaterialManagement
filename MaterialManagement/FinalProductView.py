from django.shortcuts import render
from . import Pool
from. import PoolDict
from django.http import JsonResponse
import uuid
import os

def FinalProductInterface(request):
    return render(request, "FinalProduct.html")

def GetFinalProductStockJason(request):

    try:

      finalproductid=request.GET['finalproductid']

      db,cmd=PoolDict.connectionPolling()

      # q = "select FP.*,(select S.unit from sizeunit S where S.sizeunitid=FP.sizeunitid),(select W.unit from weightunit W where W.weightunitid=FP.weightunitid),(select C.categoryname from category C where C.categoryid=FP.categoryid),(select S.subname from subcategory S where S.subcategoryid=FP.subcategoryid),(select P.productname from product P where P.productid=FP.productid) from finalproduct FP where finalproductid={}".format(finalproductid)

      q= "select * from finalproduct where finalproductid={}".format(finalproductid)

      cmd.execute(q)

      result=cmd.fetchone()
      db.close()

      return JsonResponse(result,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse({},safe=False)


def FetchAllSizeUnit(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from sizeunit"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchAllWeightUnit(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from weightunit"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)


def FetchFinalCategory(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from category"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchFinalSubcategory(request):
    try:

      db,cmd=Pool.connectionPolling()

      catid=request.GET['catid']

      q="select * from subcategory where categoryid={}".format(catid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchFinalProduct(request):
    try:

      db,cmd=Pool.connectionPolling()

      subcatid=request.GET['subcatid']

      q="select * from product where subcategoryid={}".format(subcatid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)



def SubmitFinalProduct(request):

    db, cmd = Pool.connectionPolling()

    try:
        catid = request.POST['catid']
        subcatid = request.POST['subcatid']
        productid = request.POST['productid']
        fpname = request.POST['fpname']
        size = request.POST['size']
        sizeunit = request.POST['sizeunit']
        weight = request.POST['weight']
        weightunit = request.POST['weightunit']
        colour = request.POST['colour']
        price = request.POST['price']
        stock = request.POST['stock']

        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]


        q = "insert into finalproduct(categoryid, subcategoryid, productid, finalproductname, sizee, sizeunitid, weight, weightunitid, colour, productprice, stock, picture)values({},{},{},'{}',{},{},{},{},'{}','{}','{}','{}')".format(catid,subcatid ,productid ,fpname ,size ,sizeunit ,weight ,weightunit,colour ,price,stock ,filename)

        cmd.execute(q)

        f = open("D:/MaterialManagement/assets/FinalProductImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()

        return render(request, "FinalProduct.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "FinalProduct.html", {'msg': "Record Not Submitted"})


def DisplayFinalProduct(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select FP.*,(select S.unit from sizeunit S where S.sizeunitid=FP.sizeunitid),(select W.unit from weightunit W where W.weightunitid=FP.weightunitid),(select C.categoryname from category C where C.categoryid=FP.categoryid),(select S.subname from subcategory S where S.subcategoryid=FP.subcategoryid),(select P.productname from product P where P.productid=FP.productid) from finalproduct FP"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayFinalProduct.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayFinalProduct.html", {'rows': []})


def EditDeleteFinalRecord(request):

    button = request.GET['button']

    fpid = request.GET['fpid']
    oldpic=request.GET['oldpic']

    if (button == "EDIT"):

      catid = request.GET['catid']
      subcatid = request.GET['subcatid']
      productid = request.GET['productid']
      fpname = request.GET['fpname']
      size = request.GET['size']
      sizeunit = request.GET['sizeunit']
      weight = request.GET['weight']
      weightunit = request.GET['weightunit']
      colour = request.GET['colour']
      price = request.GET['price']
      stock = request.GET['stock']

      try:

        db, cmd = Pool.connectionPolling()

        q = "update finalproduct set categoryid={}, subcategoryid={}, productid={}, finalproductname='{}', sizee={}, sizeunitid={}, weight={}, weightunitid={}, colour='{}', productprice={}, stock={} where finalproductid={}".format(catid, subcatid, productid, fpname, size, sizeunit, weight, weightunit, colour, price, stock, fpid)

        cmd.execute(q)
        db.commit()
        db.close()

        return DisplayFinalProduct(request)

      except Exception as e:

        print("Error", e)
        return DisplayFinalProduct(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from finalproduct where finalproductid={}".format(fpid)

            cmd.execute(q)
            db.commit()
            db.close()

            os.remove('D:/MaterialManagement/assets/FinalProductImages/'+oldpic)

            return DisplayFinalProduct(request)

        except Exception as e:

            print("Error", e)

            return DisplayFinalProduct(request)

def SaveFinalImage(request):
    try:
      finalid = request.POST["finalid"]

      picture = request.FILES['picture']
      oldimg=request.POST['oldimg']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]


      q="update finalproduct set picture='{}' where finalproductid={}".format(filename,finalid)

      db, cmd = Pool.connectionPolling()

      cmd.execute(q)
      F = open("D:/MaterialManagement/assets/FinalProductImages/"+filename, "wb")

      for chunk in picture.chunks():

          F.write(chunk)

      F.close

      db.commit()
      db.close()
      os.remove("D:/MaterialManagement/assets/FinalProductImages/"+oldimg)

      return DisplayFinalProduct(request)

    except Exception as e:
        print("Error:", e)
        return DisplayFinalProduct(request)
