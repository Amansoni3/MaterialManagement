from django.shortcuts import render
from . import Pool
from django.http import JsonResponse


def SupplierInterface(request):
    return render(request, "Supplier.html")

def SubmitSupplierRecord(request):

    try:
        suppliername = request.GET['suppliername']
        contactno = request.GET['contactno']
        mobileno = request.GET['mobileno']
        emailid = request.GET['emailid']
        address = request.GET['address']
        state = request.GET['state']
        city = request.GET['city']

        db, cmd = Pool.connectionPolling()

        q = "insert into supplier(suppliername, contactno, mobileno, emailid, address, state, city)values('{}','{}','{}','{}','{}','{}','{}')".format(suppliername, contactno, mobileno, emailid, address, state, city)

        cmd.execute(q)

        db.commit()
        db.close()

        return render(request, "Supplier.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "Supplier.html", {'msg': "Record Not Submitted"})

def DisplayAllSupplier(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select SP.*,(select C.cityname from cites C where C.cityid=SP.city),(select S.statename from states S where S.stateid=SP.state) from supplier SP"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayAllSupplier.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayAllSupplier.html", {'rows': []})


def FetchSupplierJason(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from supplier"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)
