import transactions

# American Express Platinum
def amex_platinum(card):
    tot = 0
    tot += (card.flights * 5) / 100
    tot += (card.hotels * 5) / 100
    tot += (card.total - card.hotels - card.flights) / 100
    tot -= 695
    return tot

# American Express Gold
def amex_gold(card):
    tot = 0
    tot += (card.restaurants * 4) / 100
    tot += (card.groceries * 4) / 100
    tot += (card.flights * 3) / 100
    tot += (card.total - card.restaurants - card.groceries - card.flights) / 100
    tot -= 250
    return tot

# American Express Blue Cash Everyday
def amex_blue_cash_everyday(card):
    tot = 0
    if card.groceries > 6000:
        tot += (6000 * 3) / 100 + ((card.groceries - 6000) * 1) / 100
    else:
        tot += (card.groceries * 3) / 100

    if card.gas > 6000:
        tot += (6000 * 3) / 100 + ((card.gas - 6000) * 1) / 100
    else:
        tot += (card.gas * 3) / 100

    if self.retail > 6000:
        tot += (6000 * 3) / 100 + ((card.retail - 6000) * 1) / 100
    else:
        tot += (card.retail * 3) / 100

    tot += (card.total - card.groceries - card.gas - card.retail) / 100
    return tot

# American Express Blue Cash Preferred
def amex_blue_cash_preferred(card): #SUS CARD
    tot = 0
    if card.groceries > 6000:
        tot += (6000 * 6) / 100 + ((card.groceries - 6000) * 1) / 100
    else:
        tot += (card.groceries * 6) / 100

    if card.entertainment > 6000:
        tot += (card.entertainment * 6) / 100 + (card.entertainment - 6000) / 100
    else:
        tot += (card.entertainment * 6) / 100
    if card.gas > 6000:
        tot += (6000 * 3) / 100 + ((card.gas - 6000) * 1) / 100
    else:
        tot += (card.gas * 3) / 100

    tot += (card.total - card.groceries - card.entertainment - card.gas - card.transit) / 100

    tot -= 95
    return tot

# American Express Business Gold Card
def amex_business_gold(card):
    v1, v2 = card.extract_max_values(2)
    tot = 0
    if v1[1] == "Flights" or v2[1] == "Flights":
        tot += (card.flights * 4) / 100
    else:
        tot += (card.flights * 1) / 100

    if v1[1] == "Restaurants" or v2[1] == "Restaurants":
        tot += (card.restaurants * 4) / 100
    else:
        tot += (card.restaurants * 1) / 100

    if v1[1] == "Gas" or v2[1] == "Gas":
        tot += (card.gas * 4) / 100
    else:
        tot += (card.gas * 1) / 100

    if v1[1] == "Groceries" or v2[1] == "Groceries":
        tot += (card.groceries * 4) / 100
    else:
        tot += (card.groceries * 1) / 100

    if v1[1] == "Entertainment" or v2[1] == "Entertainment":
        tot += (card.entertainment * 4) / 100
    else:
        tot += (card.entertainment * 1) / 100

    if v1[1] == "Car Rental" or v2[1] == "Car Rental":
        tot += (card.car_rental * 4) / 100
    else:
        tot += (card.car_rental * 1) / 100

    if v1[1] == "Hotel" or v2[1] == "Hotel":
        tot += (card.hotel * 4) / 100
    else:
        tot += (card.hotel * 1) / 100

    if v1[1] == "Retail" or v2[1] == "Retail":
        tot += (card.retail * 4) / 100
    else:
        tot += (card.retail * 1) / 100

    tot -= 295
    return tot


# Bank of America Travel Rewards credit card
def bofa_travel_rewards(card):
    tot = (card.total * 1.5) / 100
    return tot

# Bank of America Premium Rewards credit card
def bofa_premium_rewards(card):
    tot = 0
    tot += (card.flights * 2) / 100
    tot += (card.dining * 2) / 100
    tot += (card.total - card.flights - card.dining) * 1.5 / 100
    tot -= 95
    return tot

# Bank of America Unlimited Cash Rewards credit card
def bofa_unlimited_rewards(card):
    tot = (card.total * 1.5) / 100
    return tot

# Barclays Advantage Aviator Red World Elite Mastercard
def barclays_aviator_red_world_elite_mastercard(card):
    tot = 0
    tot += (card.airlines * 2) / 100 # assuming airlines = eligible American Airlines purchases
    tot += (card.total - card.airlines) / 100
    tot -= 99
    return tot

# Barclays The Hawaiian Airlines World Elite Mastercard
def barclays_the_hawaiian_airlines_world_elite_mastercard(card):
    tot = 0
    tot += (card.airlines * 3) / 100 # assuming airlines = eligible Hawaiian Airlines purchases
    tot += (card.groceries * 2) / 100 # assuming groceries = grocery store (excluding Target and Walmart purchases)
    tot += (card.gas * 2) / 100
    tot += (card.dining * 2) / 100
    tot += (card.total - card.airlines - card.groceries - card.gas - card.dining) / 100
    tot -= 99
    return tot

# Barclays JetBlue Card
def barclays_jetblue(card):
    tot = 0
    tot += (card.airlines * 3) / 100 # assuming airlines = eligible JetBlue purchases
    tot += (card.restaurants * 2) / 100
    tot += (card.groceries * 2) / 100
    tot += (card.total - card.airlines - card.restaurants - card.groceries) / 100
    return tot

# Capital One Quicksilver Cash Rewards Credit Card
def capital_one_quicksilver_cash_rewards(card):
    tot = 0
    tot += (card.hotels * 5) / 100 # assuming hotels = hotels booked through Capital One Travel
    tot += (card.rental_cars * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotels - card.rental_cars) * 1.5 / 100
    return tot

# Capital One Venture Rewards Credit Card
def capital_one_venture_rewards(card):
    tot = 0
    tot += (card.hotels * 5) / 100 # assuming hotels = hotels booked through Capital One Travel
    tot += (card.rental_cars * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotels - card.rental_cars) * 2 / 100
    tot -= 95
    return tot

# Capital One Venture X Rewards Credit Card
def capital_one_venture_x_rewards(card):
    tot = 0
    tot += (card.hotels * 10) / 100 # assuming hotels = hotels booked through Capital One Travel
    tot += (card.rental_cars * 10) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.flights * 5) / 100 # assuming flights = flights booked through Capital One Travel
    tot += (card.total - card.hotels - card.rental_cars - card.flights) * 2 / 100
    tot -= 395
    return tot

# Capital One Spark Miles for Business
def capital_one_spark_miles_for_business(card):
    tot = 0
    tot += (card.hotels * 5) / 100 # assuming hotels = hotels booked through Capital One Travel
    tot += (card.rental_cars * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotels - card.rental_cars) * 2 / 100
    tot -= 95
    return tot

# Chase Sapphire Preferred Card
def chase_sapphire_preferred(card):
    tot = 0
    tot += (card.flights * 5) / 100 # assuming travel = travel purchased through Chase Ultimate Rewards
    tot += (card.dining * 3) / 100
    tot += (card.total - card.flights - card.dining) * 2 / 100
    tot -= 95
    return tot

# Chase Sapphire Reserve
def chase_sapphire_reserve(card):
    tot = 0
    tot += (card.flights * 10) / 100 # assuming travel = travel purchased through Chase Ultimate Rewards
    tot += (card.dining * 3) / 100
    tot += (card.total - card.flights - card.dining) * 1 / 100
    tot -= 550
    return tot

# Chase Ink Business Unlimited
def chase_ink_business_unlimited(card):
    tot = 0
    tot += (card.total * 1.5) / 100
    tot -= 900
    return tot

# Citi Custom Cash
def citi_custom_cash(card):
    tot = 0
    v1 = card.extract_max_values(1)
    if v1[1] == "Flights":
        if card.flights > 500:
            tot += (500 * 5) / 100 + ((card.flights - 500) * 1) / 100
        else:
            tot += (card.flights * 5) / 100
    else:
        tot += (card.flights * 1) / 100

    if v1[1] == "Groceries":
        if card.groceries > 500:
            tot += (500 * 5) / 100 + ((card.groceries - 500) * 1) / 100
        else:
            tot += (card.groceries * 5) / 100
    else:
        tot += (card.groceries * 1) / 100

    if v1[1] == "Gas":
        if card.gas > 500:
            tot += (500 * 5) / 100 + ((card.gas - 500) * 1) / 100
        else:
            tot += (card.gas * 5) / 100
    else:
        tot += (card.gas * 1) / 100

    if v1[1] == "Dining":
        if card.dining > 500:
            tot += (500 * 5) / 100 + ((card.dining - 500) * 1) / 100
        else:
            tot += (card.dining * 5) / 100
    else:
        tot += (card.dining * 1) / 100
    if v1[1] == "Entertainment":
        if card.entertainment > 500:
            tot += (500 * 5) / 100 + ((card.entertainment - 500) * 1) / 100
        else:
            tot += (card.entertainment * 5) / 100
    if v1[1] == "Car Rental":
        if card.car_rental > 500:
            tot += (500 * 5) / 100 + ((card.car_rental - 500) * 1) / 100
        else:
            tot += (card.car_rental * 5) / 100
    else:
        tot += (card.car_rental * 1) / 100

    if v1[1] == "Hotel":
        if card.hotel > 500:
            tot += (500 * 5) / 100 + ((card.hotel - 500) * 1) / 100
        else:
            tot += (card.hotel * 5) / 100
    else:
        tot += (card.hotel * 1) / 100
    if v1[1] == "Retail":
        if card.retail > 500:
            tot += (500 * 5) / 100 + ((card.retail - 500) * 1) / 100
        else:
            tot += (card.retail * 5) / 100
    else:
        tot += (card.retail * 1) / 100
    return tot

# Citi Double Cash Card
def citi_double_cash(card):
    tot = 0
    tot += (card.total * 2) / 100
    return tot

# Citi Premier Card
def citi_premier(card):
    tot = 0
    tot += (card.flights * 3) / 100
    tot += (card.groceries * 3) / 100
    tot += (card.gas * 3) / 100
    tot += (card.dining * 3) / 100
    tot += (card.hotel * 3) / 100
    tot += (card.total - card.flights - card.groceries - card.gas - card.dining - card.hotel) / 100
    tot -= 95
    return tot

# Citi Rewards+ Card
def citi_rewards(card):
    tot = 0
    tot += (card.groceries * 2) / 100
    tot += (card.gas * 2) / 100
    tot += (card.total - card.groceries - card.gas) / 100
    return tot

# Citi AAdvantage Platinum Select World Elite Mastercard
def citi_aadvantage_platinum_select(card):
    tot = 0
    tot += (card.flights * 2) / 100
    tot += (card.gas * 2) / 100
    tot += (card.dining * 2) / 100
    tot += (card.total - card.flights - card.gas - card.dining) / 100
    tot -= 99
    return tot

# Discover It Cash Back
def discover_it_cash_back(card):
    tot = 0
    tot += (card.groceries * 5) / 100
    tot += (card.total - card.groceries) / 100
    return tot

# Discover It Balance Transfer
def discover_it_balance_transfer(card):
    tot = 0
    tot += (card.retail * 5) / 100
    tot += (card.total - card.retail) / 100
    return tot

# Discover It Miles
# def discover_it_miles(card):
#     tot = 0
#     tot += (card.gas * 1.5) / 100s
#     return tot
#
# Company: Discover <br />
# Card: Discover it® Miles <br />
# Annual Fee: 0 <br />
# Name in code: discover_it_miles <br >
# Benefits:
# -  Automatically earn unlimited 1.5x Miles on every dollar of every purchase - with no annual fee.
# ---

# Discover It Chrome
def discover_it_chrome(card):
    tot = 0
    tot += (card.gas * 2) / 100
    tot += (card.restaurants * 2) / 100
    tot += (card.total - card.gas - card.restaurants) / 100
    return tot

Company: Synchrony <br />
Card: Sam's Club® Mastercard®<br />
Annual Fee: 0 <br />
Name in code: synchrony_sams_club_mastercard <br >
Benefits:
-Its excellent 5 percent cash back on gas (on up to $6,000 in yearly purchases, then 1 percent) is one of the best gas rewards rates available
-Your first $30 of Sam’s Club purchases within 30 days are covered with a matching statement credit
-Serves as both a credit card and your Sam’s Club membership card(monthly payment can be calculated for, very spec)
---
Company: Synchrony <br />
Card: Sam's Club® Mastercard®<br />
Annual Fee: 0 <br />
Name in code: synchrony_sams_club_mastercard <br >
Benefits:
-Its excellent 5 percent cash back on gas (on up to $6,000 in yearly purchases, then 1 percent) is one of the best gas rewards rates available
-Your first $30 of Sam’s Club purchases within 30 days are covered with a matching statement credit
-Serves as both a credit card and your Sam’s Club membership card(monthly payment can be calculated for, very spec)
---
Company: Synchrony <br />
Card:PayPal Cashback Mastercard<br />
Annual Fee: 0 <br />
Name in code: synchrony_paypal_cashback_mastercard <br >
Benefits:
-Offers a unique combo of 2 percent cash back on all purchases with the chance to earn 3 percent cash back at merchants that accept Paypal.
-The card charges no annual fee, making it affordable to pair with other rewards cards.
-PayPal integration makes this a great card for people who use PayPal and want to manage their card, payments and cashback rewards all in one place.
---
Company: US Bank <br />
Card: U.S. Bank Visa® Platinum Card<br />
Annual Fee: 0 <br />
Name in code: us_bank_visa_platinum <br >
Benefits:
-It comes with cellphone protection when you pay your monthly phone bill with your card (up to two $600 claims per 12-month period, $25 deductible).
-Its intro APR offer is relatively long, giving cardholders one of the longest breaks from interest on balance transfers and new purchases.
---
Company: US Bank <br />
Card: U.S. Bank Cash+® Visa Signature® Card<br />
Annual Fee: 0 <br />
Name in code: us_bank_cash_plus_visa_signature <br >
Benefits:
- You can tailor your cash back rewards to the products and services on which you spend the most each quarter.
- You won’t have to pay an annual fee for this card.
- This card offers an introductory APR on purchases and balance transfers (for transfers made within 60 days of account opening).
---
Company: US Bank <br />
Card: U.S. Bank Cash+® Visa Signature® Card<br />
Annual Fee: 0 <br />
Name in code: us_bank_cash_plus_visa_signature <br >
Benefits:
- You can tailor your cash back rewards to the products and services on which you spend the most each quarter.
- You won’t have to pay an annual fee for this card.
- This card offers an introductory APR on purchases and balance transfers (for transfers made within 60 days of account opening).
---
Company: US Bank <br />
Card: U.S. Bank Altitude® Reserve Visa Infinite® Card<br />
Annual Fee: 400 <br />
Name in code: us_bank_altitude_reserve_visa_infinite <br >
Benefits:
- Lower annual fee compared to other cards in this category.
- Valuable annual travel credits that, if used, effectively brings the cost of the card down to $75.
- Up to $100 statement credit for Global Entry to TSA Precheck every four years
