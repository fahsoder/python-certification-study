### Flask RestFul API ###


from flask import Flask, request, jsonify

## GET
app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    # Retrieve and return a list of users
    return 'Get Users'

if __name__ == '__main__':
    app.run()


## POST
@app.route('/api/users', methods=['POST'])
def create_user():
    # Create a new user based on request data
    data = request.json
    # Process and store the new user data

    # Return a JSON response
    response = {'message': 'User created successfully', 'data': data}
    return jsonify(response), 201  # 201 - Created status code

if __name__ == '__main__':
    app.run()


## PUT
@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Update an existing user with the given user_id
    data = request.json
    # Process and update the user data
    return f'Update User {user_id}, data: {data}'

if __name__ == '__main__':
    app.run()


## DELETE
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Delete an existing user with the given user_id
    return f'Delete User {user_id}'

if __name__ == '__main__':
    app.run()
