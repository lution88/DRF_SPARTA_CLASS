#urls.py

    urlpatterns = [

        path('', message),
        path('test/', PlaceAPI.as_view()),
    ]

#views.py

    def message(request):

        message = {'message':'success!!!'}

        return JsonResponse(message)
