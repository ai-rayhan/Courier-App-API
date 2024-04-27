#Deprecated

# from functools import wraps
# from rest_framework.response import Response

# def has_role(role_name):
#     """
#     Custom decorator to check if the user has the specified role.
#     """
#     def decorator(view_func):
#         @wraps(view_func)
#         def wrapper(request,*args, **kwargs):  # Accepts any arguments
         
#             print( request.user.role )
#             print(role_name )
#             if request.user.role == role_name:
#                 return view_func(*args, **kwargs)
#             else:
#                 return Response({'error': 'Unauthorized'}, status=403)
#         return wrapper
#     return decorator
