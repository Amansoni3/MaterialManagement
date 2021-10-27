from django.shortcuts import render
from django.http import JsonResponse
from . import Pool
import uuid
import os

def SubCategoryInterface(request):

    return render(request, "SubCategory.html")

def SubSubmitCategory(request):

    db, cmd = Pool.connectionPolling()

    try:
        CI = request.POST['CI']
        SCN = request.POST['SCN']
        D = request.POST['D']

        picture = request.FILES['picture']

        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]


        q = "insert into subcategory(categoryid, subname, description, picture)values({},'{}','{}','{}')".format(CI,SCN,D,filename)

        cmd.execute(q)

        f = open("D:/MaterialManagement/assets/SubCategoryImages/" + filename, "wb")

        for chunk in picture.chunks():
            f.write(chunk)
        f.close()

        db.commit()
        db.close()
        return render(request, "SubCategory.html", {'msg': "Record Submitted Succesfully"})

    except Exception as e:

        print(e)
        return render(request, "SubCategory.html", {'msg': "Record Not Submitted"})

def DisplaySubCategory(request):
    try:
        db, cmd = Pool.connectionPolling()

        q = "select * from subcategory"

        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()

        return render(request, "DisplaySubCategory.html", {'rows': rows})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplaySubCategory.html", {'rows': []})


def displaysubcategorybyid(request):

    subcategoryid = request.GET["subcategoryid"]

    try:
        db, cmd = Pool.connectionPolling()

        q = "select sc.*,(select c.categoryname from category c where c.categoryid=sc.categoryid) from subcategory sc where subcategoryid={}".format(subcategoryid)

        cmd.execute(q)
        row = cmd.fetchone()
        db.close()

        return render(request, "DisplaySubCategoryById.html", {'row': row})

    except Exception as e:

        print("Error", e)
        return render(request, "DisplaySubCategoryById.html", {'row': []})

def EditDeleteSubCategory(request):

    button = request.GET['button']
    subcategoryid = request.GET["subcategoryid"]

    if (button == "EDIT"):


      try:

        CI = request.GET["CI"]
        SCN = request.GET["SCN"]
        D = request.GET["D"]

        db, cmd = Pool.connectionPolling()

        q = "update subcategory set categoryid={},subname='{}',description='{}' where subcategoryid={}".format(CI,SCN,D,subcategoryid)

        cmd.execute(q)
        print(q)
        db.commit()
        db.close()

        return DisplaySubCategory(request)

      except Exception as e:

        print("Error", e)
        return DisplaySubCategory(request)

    elif (button == "DELETE"):


        try:

            db, cmd = Pool.connectionPolling()

            q = "delete from subcategory where subcategoryid={}".format(subcategoryid)

            cmd.execute(q)
            db.commit()
            db.close()

            return DisplaySubCategory(request)

        except Exception as e:

            print("Error", e)

            return DisplaySubCategory(request)

def EditSubCategoryImages(request):

 try:

    subcategoryid = request.GET["subcategoryid"]
    subname = request.GET["subname"]
    description = request.GET["description"]
    picture= request.GET["picture"]

    row=[subcategoryid,subname,description,picture]

    return render(request, "EditSubCategoryImages.html", {'row': row})

 except Exception as e:
    print("Error",e)

    return render(request, "EditSubCategoryImages.html", {'row': []})


def SaveSubCategoryImage(request):
    try:
      subcategoryid = request.POST["subcategoryid"]
      picture = request.FILES['picture']
      oldpic=request.POST['oldpic']
      filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]


      q="update subcategory set picture='{}' where subcategoryid={}".format(filename,subcategoryid)

      db, cmd = Pool.connectionPolling()

      cmd.execute(q)
      F = open("D:/MaterialManagement/assets/SubCategoryImages/"+filename, "wb")

      for chunk in picture.chunks():

          F.write(chunk)

      F.close

      db.commit()
      db.close()
      os.remove("D:/MaterialManagement/assets/SubCategoryImages/"+oldpic)

      return DisplaySubCategory(request)

    except Exception as e:
        print("Error:", e)
        return DisplaySubCategory(request)
