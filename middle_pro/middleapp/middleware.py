def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        print("this is befor view")
        response = get_response(request)
        print("this after view")
        return response
    return my_function

    
