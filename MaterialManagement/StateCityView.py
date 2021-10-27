from django.http import JsonResponse
from . import Pool

def FetchAllStates(request):
    try:

      db,cmd=Pool.connectionPolling()
      q="select * from states"
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)

def FetchAllCities(request):
    try:

      db,cmd=Pool.connectionPolling()

      stateid=request.GET['stateid']

      q="select * from cites where stateid={}".format(stateid)
      cmd.execute(q)

      row=cmd.fetchall()
      db.close()

      return JsonResponse(row,safe=False)

    except Exception as e:
        print(e)
        return JsonResponse([],safe=False)



