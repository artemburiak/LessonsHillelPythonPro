from flask import Flask

app = Flask(__name__)

# Admin possibly can:
# 1. Tracking information about users and dishes
# 2. He can add new dishes
# 3. He can remove dishes or users (or edit them)
# 4. Maybe some other options...

# Admin Endoints:



# The first 4 endpoints for admin are similar to the endpoints for the common user: (admin, register, sign in, log out)



@app.route('/admin', methods = ['GET', 'POST', 'DELETE'])
def adminPage():
    return 'Admin Page'

@app.route('/admin/register', methods = ['POST'])
def adminRegisterPage():
    return 'Admin Resgister Page'

@app.route('/admin/signIn', methods = ['POST'])
def adminSignInPage():
    return 'Admin Sign In Page'

@app.route('/admin/logout', methods = ['GET', 'POST'])
def adminLogoutPage():
    return 'Admin Logout Page'



# The next 4 endpoints are connected with editing all available dishes: (dishes, add, edit, delete)



@app.route('/admin/dishes', methods = ['GET', 'PUT'])
def adminDishesPage():
    return 'Admin Dishes Page'

@app.route('/admin/dishes/add', methods = ['POST'])
def adminDishesAddPage():
    return 'Admin Dishes Add Page'

@app.route('/admin/dishes/edit', methods = ['POST'])
def adminDishesEditPage():
    return 'Admin Dishes Edit Page'

@app.route('/admin/dishes/delete', methods = ['POST'])
def adminDishesDeletePage():
    return 'Admin Dishes Delete Page'



# The last part (3 endpoins) connected with actions to users: (users, edit, delete)



@app.route('/admin/users', methods = ['GET', 'PUT'])
def adminUsersPage():
    return 'Admin Users Page'

@app.route('/admin/users/edit', methods = ['POST'])
def adminUsersEditPage():
    return 'Admin Users Edit Page'

@app.route('/admin/users/delete', methods = ['POST'])
def adminUsersDeletePage():
    return 'Admin Users Delete Page'

