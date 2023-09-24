import os
import json

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from flask_cors import CORS, cross_origin
from flask_talisman import Talisman
import card_backtesting
import transactions
import requests

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# talisman = Talisman(app, force_https=True)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello World!'

@app.route('/transactions', methods=['GET'])
@cross_origin()
def get_transactions():
    response.headers.add('Access-Control-Allow-Origin', '*')
    try:
        res = get_transactions().json()
        current_transactions = Transactions()

        for transaction in res:

            category = transaction['category']
            if len(category) > 1:
                category = category[1]
            else:
                continue

            current_transactions.add_transaction(category, transaction['amount'])

        res = []
        res.append((amex_platinum(current_transactions), "amex_platinum"))
        res.append((amex_gold(current_transactions), "amex_gold"))
        res.append((amex_blue_cash_everyday(current_transactions), "amex_blue_cash_everyday"))
        res.append((amex_blue_cash_preferred(current_transactions), "amex_blue_cash_preferred"))
        res.append((amex_business_gold(current_transactions), "amex_business_gold"))
        res.append((bofa_travel_rewards(current_transactions), "bofa_travel_rewards"))
        res.append((bofa_premium_rewards(current_transactions), "bofa_premium_rewards"))
        res.append((bofa_unlimited_rewards(current_transactions), "bofa_unlimited_rewards"))
        res.append((barclays_aviator_red_world_elite_mastercard(current_transactions), "barclays_aviator_red_world_elite_mastercard"))
        res.append((barclays_the_hawaiian_airlines_world_elite_mastercard(current_transactions), "barclays_the_hawaiian_airlines_world_elite_mastercard"))
        res.append((barclays_jetblue(current_transactions), "barclays_jetblue"))
        res.append((capital_one_quicksilver_cash_rewards(current_transactions), "capital_one_quicksilver_cash_rewards"))
        res.append((capital_one_venture_rewards(current_transactions), "capital_one_venture_rewards"))
        res.append((capital_one_venture_x_rewards(current_transactions), "capital_one_venture_x_rewards"))
        res.append((capital_one_spark_miles_for_business(current_transactions), "capital_one_spark_miles_for_business"))
        res.append((chase_sapphire_preferred(current_transactions), "chase_sapphire_preferred"))
        res.append((chase_sapphire_reserve(current_transactions), "chase_sapphire_reserve"))
        res.append((chase_ink_business_unlimited(current_transactions), "chase_ink_business_unlimited"))
        res.append((citi_custom_cash(current_transactions), "citi_custom_cash"))
        res.append((citi_double_cash(current_transactions), "citi_double_cash"))
        res.append((citi_premier(current_transactions), "citi_premier"))
        res.append((citi_rewards(current_transactions), "citi_rewards"))
        res.append((citi_aadvantage_platinum_select(current_transactions), "citi_aadvantage_platinum_select"))
        res.append((discover_it_cash_back(current_transactions), "discover_it_cash_back"))
        res.append((discover_it_balance_transfer(current_transactions), "discover_it_balance_transfer"))
        res.append((discover_student_credit_card(current_transactions), "discover_student_credit_card"))
        res.append((discover_it_miles(current_transactions), "discover_it_miles"))
        res.append((discover_it_chrome(current_transactions), "discover_it_chrome"))
        res.append((synchrony_sams_club_mastercard(current_transactions), "synchrony_sams_club_mastercard"))
        res.append((us_bank_cash_plus_visa_signature(current_transactions), "us_bank_cash_plus_visa_signature"))
        res.append((us_bank_business_cash_rewards_world_elite_mastercard(current_transactions), "us_bank_business_cash_rewards_world_elite_mastercard"))
        res.append((wells_fargo_active_cash(current_transactions), "wells_fargo_active_cash"))
        res.append((discover_it_balance_transfer(current_transactions), "discover_it_balance_transfer"))
        res.append((discover_student_credit_card(current_transactions), "discover_student_credit_card"))
        res.append((wells_fargo_autograph(current_transactions), "wells_fargo_autograph"))
        res.append((usaa_cashback_rewards_plus_american_express(current_transactions), "usaa_cashback_rewards_plus_american_express"))
        res.append((usaa_preferred_cash_rewards_visa_signature(current_transactions), "usaa_preferred_cash_rewards_visa_signature"))
        res.append((usaa_rewards_american_express(current_transactions), "usaa_rewards_american_express"))

        res.sort(lambda x: x[0], reverse=True)

        return [item[1] for item in res[:5]]

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
     app.run(debug=True, port=(8000))

