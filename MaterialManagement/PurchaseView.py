from django.shortcuts import render
from . import Pool
from django.http import JsonResponse

def PurchaseInterface(request):
    try:
        result = request.session['EMPLOYE']
        print(result)
        return render(request, "Purchase.html",{'result':result})

    except Exception as e:
        return render(request, "EmployeLogin.html")


def FetchPurchaseFinalProduct(request):
    try:

      db,cmd=Pool.connectionPolling()

      subcatid=request.GET['subcatid']

      q="select * from purchase where purchaseid={}".format(subcatid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def SubmitPurchaseRecord(request):

    try:
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        date = request.GET['datepurchase']
        supplierid = request.GET['supplierid']
        employeid = request.GET['employeid']
        stock = request.GET['stock']
        amount = request.GET['amount']


        db, cmd = Pool.connectionPolling()

        q = "insert into purchase(employeid, categoryid, subcategoryid, productid, finalproductid, datepurchase, supplierid, stock, amount)values({},{},{},{},{},'{}',{},{},{})".format(employeid, categoryid, subcategoryid, productid, finalproductid, date, supplierid, stock, amount)
        cmd.execute(q)

        q="update finalproduct set productprice=((productprice+{})/2) , stock=stock+{} where finalproductid={}".format(amount,stock,finalproductid)
        cmd.execute(q)
        
        db.commit()
        db.close()

        return render(request, "Purchase.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "Purchase.html", {'msg': "Record Not Submitted"})


def DisplayPurchaseProduct(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select PU.*,(select C.categoryname from category C where C.categoryid=PU.categoryid),(select S.subname from subcategory S where S.subcategoryid=PU.subcategoryid),(select P.productname from product P where P.productid=PU.productid),(select F.finalproductname from finalproduct F where F.finalproductid=PU.finalproductid),(select SU.suppliername from supplier SU where SU.supplierid=PU.supplierid) from purchase PU"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        result=request.session['EMPLOYE']

        return render(request, "DisplayPurchaseProduct.html", {'rows': rows,'result':result})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayPurchaseProduct.html", {'rows': []})

def EditDeletePurchaseRecord(request):

    button = request.GET['button']

    transactionid = request.GET['transactionid']


    if (button == "EDIT"):

        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        date = request.GET['datepurchase']
        supplierid = request.GET['supplierid']
        employeid = request.GET['employeid']
        stock = request.GET['stock']
        amount = request.GET['amount']

        try:

            db, cmd = Pool.connectionPolling()

            q = "update purchase set employeid={}, categoryid={}, subcategoryid={}, productid={}, finalproductid={}, datepurchase='{}', supplierid={}, stock={}, amount={} where transactionid={}".format(employeid, categoryid, subcategoryid, productid, finalproductid, date, supplierid, stock, amount,transactionid)

            cmd.execute(q)
            db.commit()

            db.close()

            return DisplayPurchaseProduct(request)

        except Exception as e:

            print("Error", e)
            return DisplayPurchaseProduct(request)

    elif (button == "DELETE"):

        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from purchase where transactionid={}".format(transactionid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayPurchaseProduct(request)

        except Exception as e:

            print("Error", e)

            return DisplayPurchaseProduct(request)