from flask import Flask
import database

app = Flask(__name__)

# Main:



@app.route('/', methods = ['GET', 'POST'])
def mainPage():
    return 'Main Page'



# Cart:



@app.route('/cart', methods = ['GET', 'PUT'])
def cartPage():
    return 'Cart Page'

@app.route('/cart/order', methods = ['POST'])
def cartOrderPage():
    return 'Cart Order Page'

@app.route('/cart/add', methods = ['POST', 'PUT'])
def cartAddPage():
    return 'Cart Add Page'



# User: 



@app.route('/user', methods = ['GET', 'POST', 'DELETE'])
def userPage():
    return 'User Page'

@app.route('/user/register', methods = ['POST'])
def userRegisterPage():
    return 'User Resgister Page'

@app.route('/user/signIn', methods = ['POST'])
def userSignInPage():
    return 'User Sign In Page'

@app.route('/user/logout', methods = ['GET', 'POST'])
def userLogoutPage():
    return 'User Logout Page'

@app.route('/user/restore', methods = ['POST'])
def userRestorePage():
    return 'User Restore Page'

@app.route('/user/orders', methods = ['GET'])
def userOrdersHistoryPage():
    return 'User Orders History Page'

@app.route('/user/orders/<id>', methods = ['GET'])
def userOrderPage(id : int):
    return 'User Order Page'

@app.route('/user/address', methods = ['GET', 'POST'])
def userAddressListPage():
    return 'User Address List Page'

@app.route('/user/address/<id>', methods = ['GET', 'POST'])
def userAddressPage(id : int):
    return 'User Address Page'



# Menu: 



@app.route('/menu', methods = ['GET'])
def menuPage():
    res = database.cursor.execute("SELECT * FROM Dishes").fetchall()
    return res

@app.route('/menu/<cat_name>', methods = ['GET'])
def menuCategoryPage():
    return 'Menu <category name> Page'

@app.route('/menu/<cat_name>/<dish>', methods = ['GET'])
def menuCategoryDishPage():
    return 'Menu <category name> <dish> Page'

@app.route('/menu/<cat_name>/<dish>/review', methods = ['POST'])
def menuCategoryDishReviewPage():
    return 'Menu <category name> <dish> Review Page'

@app.route('/menu/search', methods = ['GET', 'POST'])
def menuSearchPage():
    return 'Menu Search Page'



# Admin: 



@app.route('/admin', methods = ['GET'])
def adminPage():
    return 'Admin Page'

@app.route('/admin/dishes', methods = ['GET', 'POST'])
def adminDishesPage():
    return 'Admin dishes Page'

@app.route('/admin/dishes/<dish>', methods = ['GET', 'PUT', 'DELETE'])
def adminDishPage():
    return 'Admin Dish Page'

@app.route('/admin/categories', methods = ['GET', 'POST'])
def adminCategoriesPage():
    return 'Admin Categories Page'

@app.route('/admin/categories/<category>', methods = ['GET', 'PUT', 'DELETE'])
def adminCategoryPage():
    return 'Admin Category Page'

@app.route('/admin/orders', methods = ['GET'])
def adminOrdersPage():
    return 'Admin Orders Page'

@app.route('/admin/orders/<order>', methods = ['GET', 'PUT'])
def adminOrderPage():
    return 'Admin Order Page'

@app.route('/admin/search', methods = ['GET'])
def adminSearchPage():
    return 'Admin Search Page'

if __name__ == '__main__':
    app.run()

    
