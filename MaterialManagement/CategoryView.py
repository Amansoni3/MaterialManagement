from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
import uuid
import os


def CategoryInterface(request):
    return render(request, "CategoryInterface.html")

def SubmitCategory(request):
    try:
        CN = request.POST['CN']

        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]

        db, cmd = Pool.connectionPolling()

        q = "insert into category(categoryname, categorypic)values('{}','{}')".format(CN,filename)

        cmd.execute(q)

        f = open("D:/MaterialManagement/assets/CategoryImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "CategoryInterface.html", {'msg': "Category Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "CategoryInterface.html", {'msg': "Category Not Submitted"})

def DisplayCategory(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from category"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplayCategory.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayCategory.html", {'rows': []})

def GetCategoryJason(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from category"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return JsonResponse(rows,safe=False)

    except Exception as e:

        print("Error", e)

        return JsonResponse(rows, safe=False)

def DisplayCategoryById(request):

    categoryid = request.GET["categoryid"]

    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from category where categoryid={}".format(categoryid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "DisplayCategoryById.html", {'row': row})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplayCategoryById.html", {'row': []})


def EditDeleteCategory(request):

    button = request.GET['button']

    categoryid = request.GET["categoryid"]


    if (button == "EDIT"):


      try:

        CN = request.GET['CN']

        db, cmd = Pool.connectionPolling()

        q = "update category set categoryname='{}' where categoryid={}".format(CN,categoryid)

        cmd.execute(q)
        print(q)
        db.commit()
        db.close()

        return DisplayCategory(request)

      except Exception as e:

        print("Error", e)
        return DisplayCategory(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from category where categoryid={}".format(categoryid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplayCategory(request)

        except Exception as e:

            print("Error", e)

            return DisplayCategory(request)

def EditCategoryImages(request):

 try:

    categoryid = request.GET["categoryid"]
    categoryname = request.GET["categoryname"]
    categorypic = request.GET["categorypic"]

    row=[categoryid,categoryname,categorypic]

    return render(request, "EditCategoryImages.html", {'row': row})

 except Exception as e:
    print("Error",e)

    return render(request, "EditCategoryImages.html", {'row': []})

def SaveCategoryImage(request):
    try:
      categoryid = request.POST["categoryid"]

      picture = request.FILES['picture']
      oldpic=request.POST['oldpic']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]


      q="update category set categorypic='{}' where categoryid={}".format(filename,categoryid)

      db, cmd = Pool.connectionPolling()

      cmd.execute(q)
      F = open("D:/MaterialManagement/assets/CategoryImages/"+filename, "wb")

      for chunk in picture.chunks():

          F.write(chunk)

      F.close

      db.commit()
      db.close()
      os.remove("D:/MaterialManagement/assets/CategoryImages/"+oldpic)

      return DisplayCategory(request)

    except Exception as e:
        print("Error:", e)
        return DisplayCategory(request)