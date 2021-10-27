from django.shortcuts import render
from . import PoolDict
from . import Pool

def EmployeeLogin(request):

    try:
        result=request.session['EMPLOYE']

        return render(request, "EmployeDashboard.html",{'result':result})

    except Exception as e:

        return render(request, "EmployeLogin.html")

def EmployeLogout(request):

    del request.session['EMPLOYE']
    return render(request, "EmployeLogin.html")



def EmployeDashboard(request):

    try:
        result=request.session['EMPLOYE']
        return render(request, "EmployeDashboard.html",{'result':result})
    except Exception as e:
        return render(request,"EmployeLogin.html")

def CheckEmployeLogin(request):

    try:

        emailid=request.POST['emailid']
        password=request.POST['password']

        db,cmd=PoolDict.connectionPolling()

        q="select * from employe where email='{}' and password='{}'".format(emailid,password)

        cmd.execute(q)

        result=cmd.fetchone()
        print(result)

        if(result):

            request.session['EMPLOYE']=result

            return render(request,"EmployeDashboard.html",{'result':result})
        else:

            return render(request,"EmployeLogin.html",{'result':result,'msg':"Invalid/Username or Password"})

    except Exception as e:

        print(e)

        return render(request, "EmployeLogin.html", {'result':{},'msg':'Server Error'})


def DisplayProductEmployeLogin(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from product"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        result=request.session['EMPLOYE']

        return render(request, "DisplayProductEmployee.html", {'rows': rows,'result':result})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayProductEmployee.html", {'rows': []})

def DisplayFinalProductEmploye(request):

    try:
        db, cmd = Pool.connectionPolling()

        q = "select FP.*,(select S.unit from sizeunit S where S.sizeunitid=FP.sizeunitid),(select W.unit from weightunit W where W.weightunitid=FP.weightunitid),(select C.categoryname from category C where C.categoryid=FP.categoryid),(select S.subname from subcategory S where S.subcategoryid=FP.subcategoryid),(select P.productname from product P where P.productid=FP.productid) from finalproduct FP"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        result=request.session['EMPLOYE']

        return render(request, "DisplayFinalProductEmploye.html", {'rows': rows,'result':result})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayFinalProductEmploye.html", {'rows': []})


