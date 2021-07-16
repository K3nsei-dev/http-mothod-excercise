from flask import *

app = Flask(__name__)


@app.route('/')
def shopping():
    return render_template('shopping.html')


@app.route('/showitems', methods=['POST'])
def show_items():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_id = request.form['item_id']
        quantity = request.form['quantity']
        price = request.form['price']
        return render_template('showitems.html', item_name=item_name, item_id=item_id, quantity=quantity, price=price)


if __name__ == '__main__':
    app.run(debug=True)
