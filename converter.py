import requests
from flask import Flask, request, render_template

app = Flask(__name__)


def get_currencies():
    try:
        response = requests.get("https://open.er-api.com/v6/latest/USD")
        rates = response.json()
        currencies = rates["rates"]
        return currencies
    except Exception as e:
        return '<h1>Bad Request : {}</h1>'.format(e)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            from_rate_to_dollar = 1
            to_rate_to_dollar = 1
            amount = float(request.form['amount'])
            from_curr = request.form['from_curr']
            to_curr = request.form['to_curr']
            currencies = get_currencies()
            for key, value in currencies.items():
                if key == from_curr:
                    from_rate_to_dollar = float(value)
            for key, value in currencies.items():
                if key == to_curr:
                    to_rate_to_dollar = float(value)

            result = (amount / from_rate_to_dollar) * to_rate_to_dollar

            return render_template('converter.html', result=round(result, 2), amount=amount, currencies=currencies, from_curr=from_curr, to_curr=to_curr)
        except Exception as e:
            return '<h1>Bad Request : {}</h1>'.format(e)

    else:
        currencies = get_currencies()
        return render_template('converter.html', currencies=currencies)


if __name__ == '__main__':
    app.run(debug=True)
