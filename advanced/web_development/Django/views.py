# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        # Retrieve a list of users
        users = [{'user_id': 1, 'name': 'John Doe', 'age': 30}, {'user_id': 2, 'name': 'Jane Smith', 'age': 25}]
        return JsonResponse(users, safe=False)

    elif request.method == 'POST':
        # Create a new user based on request data
        data = request.POST
        # Process and store the new user data

        # Return a JSON response
        response = {'message': 'User created successfully'}
        return JsonResponse(response, status=201)  # 201 - Created status code

@csrf_exempt
def user_detail(request, user_id):
    if request.method == 'GET':
        # Retrieve user data based on the given user_id
        # Process and retrieve the user data

        # Return a JSON response
        response = {'user_id': user_id, 'name': 'John Doe', 'age': 30}
        return JsonResponse(response)

    elif request.method == 'PUT':
        # Update an existing user with the given user_id
        data = request.POST
        # Process and update the user data

        # Return a JSON response
        response = {'message': f'User {user_id} updated successfully'}
        return JsonResponse(response)

    elif request.method == 'DELETE':
        # Delete an existing user with the given user_id
        # Process and delete the user data

        # Return a JSON response
        response = {'message': f'User {user_id} deleted successfully'}
        return JsonResponse(response)

