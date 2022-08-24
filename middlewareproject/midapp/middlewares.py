from django.shortcuts import HttpResponse
## -----=====Function Based Middleware=====-----

# def custom_middleware(get_response):
#     print('Initialisation!')
#     def custom_function(request):
#         print('this executes before the view inside the middleware...')
#         response = get_response(request)
#         print("this executes after the view's execution inside the middleware...")
#         return response
#     return custom_function



## -----=====Class Based Middleware=====-----

# class custom_middleware():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation============')

#     def __call__(self, request):
#         print('this executes before the view inside the middleware...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside the middleware...")
#         return response



## -----=====Multiple Middlewares=====-----

# class custom_middleware_one():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation ONE============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE ONE...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE ONE...")
#         return response

# class custom_middleware_two():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation TWO============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE TWO...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE TWO...")
#         return response

# class custom_middleware_three():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation THREE============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE THREE...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE THREE...")
#         return response



## -----=====returning response from middlewares only & not letting it pass through=====-----

# from http.client import HTTPResponse


# class custom_middleware_one():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation ONE============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE ONE...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE ONE...")
#         return response

# class custom_middleware_two():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation TWO============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE TWO...')
#         response = HttpResponse("************HALT!!**************")
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE TWO...")
#         return response

# class custom_middleware_three():
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('===========Initialisation THREE============')

#     def __call__(self, request):
#         print('this executes before the view inside CUSTOM MIDDLEWARE THREE...')
#         response = self.get_response(request)
#         print("this executes after the view's execution inside CUSTOM MIDDLEWARE THREE...")
#         return response



## -----=====Middleware Hooks=====-----

class process_middleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        print(("************Entered process_view**************"))
        # return HttpResponse('This is executed before the View...')
        return None

class exception_middleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print(("************Entered exception_view**************"))
        msg = exception
        return HttpResponse(msg)

class template_response_middleware():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print(("************Entered process_template_view**************"))
        response.context_data['name'] = 'Rahul Rajesh Mohan Raj'
        return response
