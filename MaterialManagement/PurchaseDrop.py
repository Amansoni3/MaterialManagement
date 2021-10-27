from django.shortcuts import render
from . import Pool
from django.http import JsonResponse


def FetchPurchaseCategory(request):
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

def FetchPurchaseSubcategory(request):
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

def FetchPurchaseProduct(request):
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

def FetchPurchaseFinalProduct(request):
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
