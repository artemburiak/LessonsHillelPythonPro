from flask import Flask

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

@app.route('/cart/add', methods = ['POST'])
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
    return 'Menu Page'

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

if __name__ == '__main__':
    app.run()

    
