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

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# talisman = Talisman(app, force_https=True)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello World!'

@app.route('/transactions', methods=['GET', 'POST'])
@cross_origin()
def get_transactions():
    response = request.get_json()
    try:
        current_transactions = transactions.Transactions()

        for transaction in response:

            category = transaction['category']
            if len(category) > 1:
                category = category[1]
            else:
                continue

            current_transactions.add_transaction(category, transaction['amount'])

        res = []
        res.append((card_backtesting.amex_platinum(current_transactions), "amex_platinum"))
        res.append((card_backtesting.amex_gold(current_transactions), "amex_gold"))
        res.append((card_backtesting.amex_blue_cash_everyday(current_transactions), "amex_blue_cash_everyday"))
        res.append((card_backtesting.amex_blue_cash_preferred(current_transactions), "amex_blue_cash_preferred"))
        res.append((card_backtesting.amex_business_gold(current_transactions), "amex_business_gold"))
        res.append((card_backtesting.bofa_travel_rewards(current_transactions), "bofa_travel_rewards"))
        res.append((card_backtesting.bofa_premium_rewards(current_transactions), "bofa_premium_rewards"))
        res.append((card_backtesting.bofa_unlimited_rewards(current_transactions), "bofa_unlimited_rewards"))
        res.append((card_backtesting.barclays_aviator_red_world_elite_mastercard(current_transactions), "barclays_aviator_red_world_elite_mastercard"))
        res.append((card_backtesting.barclays_the_hawaiian_airlines_world_elite_mastercard(current_transactions), "barclays_the_hawaiian_airlines_world_elite_mastercard"))
        res.append((card_backtesting.barclays_jetblue(current_transactions), "barclays_jetblue"))
        res.append((card_backtesting.capital_one_quicksilver_cash_rewards(current_transactions), "capital_one_quicksilver_cash_rewards"))
        res.append((card_backtesting.capital_one_venture_rewards(current_transactions), "capital_one_venture_rewards"))
        res.append((card_backtesting.capital_one_venture_x_rewards(current_transactions), "capital_one_venture_x_rewards"))
        res.append((card_backtesting.capital_one_spark_miles_for_business(current_transactions), "capital_one_spark_miles_for_business"))
        res.append((card_backtesting.chase_sapphire_preferred(current_transactions), "chase_sapphire_preferred"))
        res.append((card_backtesting.chase_sapphire_reserve(current_transactions), "chase_sapphire_reserve"))
        res.append((card_backtesting.chase_ink_business_unlimited(current_transactions), "chase_ink_business_unlimited"))
        res.append((card_backtesting.citi_custom_cash(current_transactions), "citi_custom_cash"))
        res.append((card_backtesting.citi_double_cash(current_transactions), "citi_double_cash"))
        res.append((card_backtesting.citi_premier(current_transactions), "citi_premier"))
        res.append((card_backtesting.citi_rewards(current_transactions), "citi_rewards"))
        res.append((card_backtesting.citi_aadvantage_platinum_select(current_transactions), "citi_aadvantage_platinum_select"))
        res.append((card_backtesting.discover_it_cash_back(current_transactions), "discover_it_cash_back"))
        res.append((card_backtesting.discover_it_balance_transfer(current_transactions), "discover_it_balance_transfer"))
        res.append((card_backtesting.discover_student_credit_card(current_transactions), "discover_student_credit_card"))
        res.append((card_backtesting.discover_it_miles(current_transactions), "discover_it_miles"))
        res.append((card_backtesting.discover_it_chrome(current_transactions), "discover_it_chrome"))
        res.append((card_backtesting.synchrony_sams_club_mastercard(current_transactions), "synchrony_sams_club_mastercard"))
        res.append((card_backtesting.us_bank_cash_plus_visa_signature(current_transactions), "us_bank_cash_plus_visa_signature"))
        res.append((card_backtesting.us_bank_business_cash_rewards_world_elite_mastercard(current_transactions), "us_bank_business_cash_rewards_world_elite_mastercard"))
        res.append((card_backtesting.wells_fargo_active_cash(current_transactions), "wells_fargo_active_cash"))
        res.append((card_backtesting.discover_it_balance_transfer(current_transactions), "discover_it_balance_transfer"))
        res.append((card_backtesting.discover_student_credit_card(current_transactions), "discover_student_credit_card"))
        res.append((card_backtesting.wells_fargo_autograph(current_transactions), "wells_fargo_autograph"))
        res.append((card_backtesting.usaa_cashback_rewards_plus_american_express(current_transactions), "usaa_cashback_rewards_plus_american_express"))
        res.append((card_backtesting.usaa_preferred_cash_rewards_visa_signature(current_transactions), "usaa_preferred_cash_rewards_visa_signature"))
        res.append((card_backtesting.usaa_rewards_american_express(current_transactions), "usaa_rewards_american_express"))

        res.sort(key = lambda x: x[0], reverse=True)

        return [item for item in res[:5]]

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
     app.run(debug=True, port=(8000))

