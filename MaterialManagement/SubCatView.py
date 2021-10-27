from django.http import JsonResponse
from . import Pool

def FetchAllCategory(request):
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

def FetchAllSubcategory(request):
    try:

      db,cmd=Pool.connectionPolling()

      I=request.GET['I']

      q="select * from subcategory where categoryid={}".format(I)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)



