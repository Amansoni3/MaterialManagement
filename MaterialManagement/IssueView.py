from django.shortcuts import render
from . import Pool
from django.http import JsonResponse

def IssueInterface(request):
    try:
        result=request.session['EMPLOYE']
        print(result)
        return render(request, "IssueInterface.html",{'result':result})
    except Exception as e:
        return render(request,"EmployeLogin.html")

def SubmitIssueRecord(request):

    try:
        employeid = request.GET['employeid']
        categoryid = request.GET['categoryid']
        subcategoryid = request.GET['subcategoryid']
        productid = request.GET['productid']
        finalproductid = request.GET['finalproductid']
        demandemployeid = request.GET['demandemployeid']
        issuedate = request.GET['issuedate']
        quantityissue = request.GET['quantityissue']
        remark = request.GET['remark']


        db, cmd = Pool.connectionPolling()

        q = "insert into issue(employeid, categoryid, subcategoryid, productid, finalproductid, demandemployeid, issuedate, quantityissue, remark)values({},{},{},{},{},{},'{}',{},'{}')".format(employeid, categoryid, subcategoryid, productid, finalproductid, demandemployeid, issuedate, quantityissue, remark)

        cmd.execute(q)

        db.commit()
        db.close()

        return render(request, "IssueInterface.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "IssueInterface.html", {'msg': "Record Not Submitted"})

def FetchIssueCategory(request):
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

def FetchIssueSubcategory(request):
    try:

      db,cmd=Pool.connectionPolling()

      categoryid=request.GET['categoryid']

      q="select * from subcategory where categoryid={}".format(categoryid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchIssueProduct(request):
    try:

      db,cmd=Pool.connectionPolling()

      subcategoryid=request.GET['subcategoryid']

      q="select * from product where subcategoryid={}".format(subcategoryid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchIssueFinalProduct(request):
    try:

      db,cmd=Pool.connectionPolling()

      productid=request.GET['productid']

      q="select * from finalproduct where productid={}".format(productid)

      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchAllEmployeJSON(request):

    try:

      db,cmd=Pool.connectionPolling()
      q="select * from employe"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:

        print(e)
        return JsonResponse([],safe=False)

def DisplayAllIssue(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select I.*,(select E.firstname from employe E where E.employeid=I.demandemployeid),(select E.lastname from employe E where E.employeid=I.demandemployeid),(select C.categoryname from category C where C.categoryid=I.categoryid),(select S.subname from subcategory S where S.subcategoryid=I.subcategoryid),(select P.productname from product P where P.productid=I.productid),(select F.finalproductname from finalproduct F where F.finalproductid=I.finalproductid) from issue I"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        result=request.session['EMPLOYE']

        return render(request, "DisplayIssue.html", {'rows': rows,'result':result})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayIssue.html", {'rows': []})


