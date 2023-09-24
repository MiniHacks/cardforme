import transactions

# American Express Platinum
def amex_platinum(card):
    tot = 0
    tot += (card.flights * 5) / 100
    tot += (card.hotel * 5) / 100
    tot += (card.total - card.hotel - card.flights) / 100
    tot -= 695
    return tot

# American Express Gold
def amex_gold(card):
    tot = 0
    tot += (card.dining * 4) / 100
    tot += (card.groceries * 4) / 100
    tot += (card.flights * 3) / 100
    tot += (card.total - card.dining - card.groceries - card.flights) / 100
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

    if card.retail > 6000:
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

    tot += (card.total - card.groceries - card.entertainment - card.gas - card.car_rental) / 100

    tot -= 95
    return tot

# American Express Business Gold Card
def amex_business_gold(card):
    v1, v2 = card.extract_max_values(2)
    tot = 0
    if v1 == "Flights" or v2 == "Flights":
        tot += (card.flights * 4) / 100
    else:
        tot += (card.flights * 1) / 100

    if v1 == "dining" or v2 == "dining":
        tot += (card.dining * 4) / 100
    else:
        tot += (card.dining * 1) / 100

    if v1 == "Gas" or v2 == "Gas":
        tot += (card.gas * 4) / 100
    else:
        tot += (card.gas * 1) / 100

    if v1 == "Groceries" or v2 == "Groceries":
        tot += (card.groceries * 4) / 100
    else:
        tot += (card.groceries * 1) / 100

    if v1 == "Entertainment" or v2 == "Entertainment":
        tot += (card.entertainment * 4) / 100
    else:
        tot += (card.entertainment * 1) / 100

    if v1 == "Car Rental" or v2 == "Car Rental":
        tot += (card.car_rental * 4) / 100
    else:
        tot += (card.car_rental * 1) / 100

    if v1 == "Hotel" or v2 == "Hotel":
        tot += (card.hotel * 4) / 100
    else:
        tot += (card.hotel * 1) / 100

    if v1 == "Retail" or v2 == "Retail":
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
    tot += (card.flights * 2) / 100 # assuming airlines = eligible American Airlines purchases
    tot += (card.total - card.flights) / 100
    tot -= 99
    return tot

# Barclays The Hawaiian Airlines World Elite Mastercard
def barclays_the_hawaiian_airlines_world_elite_mastercard(card):
    tot = 0
    tot += (card.flights * 3) / 100 # assuming airlines = eligible Hawaiian Airlines purchases
    tot += (card.groceries * 2) / 100 # assuming groceries = grocery store (excluding Target and Walmart purchases)
    tot += (card.gas * 2) / 100
    tot += (card.dining * 2) / 100
    tot += (card.total - card.flights - card.groceries - card.gas - card.dining) / 100
    tot -= 99
    return tot

# Barclays JetBlue Card
def barclays_jetblue(card):
    tot = 0
    tot += (card.flights * 3) / 100 # assuming airlines = eligible JetBlue purchases
    tot += (card.dining * 2) / 100
    tot += (card.groceries * 2) / 100
    tot += (card.total - card.flights - card.dining - card.groceries) / 100
    return tot

# Capital One Quicksilver Cash Rewards Credit Card
def capital_one_quicksilver_cash_rewards(card):
    tot = 0
    tot += (card.hotel * 5) / 100 # assuming hotel = hotel booked through Capital One Travel
    tot += (card.car_rental * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotel - card.car_rental) * 1.5 / 100
    return tot

# Capital One Venture Rewards Credit Card
def capital_one_venture_rewards(card):
    tot = 0
    tot += (card.hotel * 5) / 100 # assuming hotel = hotel booked through Capital One Travel
    tot += (card.car_rental * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotel - card.car_rental) * 2 / 100
    tot -= 95
    return tot

# Capital One Venture X Rewards Credit Card
def capital_one_venture_x_rewards(card):
    tot = 0
    tot += (card.hotel * 10) / 100 # assuming hotel = hotel booked through Capital One Travel
    tot += (card.car_rental * 10) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.flights * 5) / 100 # assuming flights = flights booked through Capital One Travel
    tot += (card.total - card.hotel - card.car_rental - card.flights) * 2 / 100
    tot -= 395
    return tot

# Capital One Spark Miles for Business
def capital_one_spark_miles_for_business(card):
    tot = 0
    tot += (card.hotel * 5) / 100 # assuming hotel = hotel booked through Capital One Travel
    tot += (card.car_rental * 5) / 100 # assuming rental_cars = rental cars booked through Capital One Travel
    tot += (card.total - card.hotel - card.car_rental) * 2 / 100
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
    if v1 == "Flights":
        if card.flights > 500:
            tot += (500 * 5) / 100 + ((card.flights - 500) * 1) / 100
        else:
            tot += (card.flights * 5) / 100
    else:
        tot += (card.flights * 1) / 100

    if v1 == "Groceries":
        if card.groceries > 500:
            tot += (500 * 5) / 100 + ((card.groceries - 500) * 1) / 100
        else:
            tot += (card.groceries * 5) / 100
    else:
        tot += (card.groceries * 1) / 100

    if v1 == "Gas":
        if card.gas > 500:
            tot += (500 * 5) / 100 + ((card.gas - 500) * 1) / 100
        else:
            tot += (card.gas * 5) / 100
    else:
        tot += (card.gas * 1) / 100

    if v1 == "Dining":
        if card.dining > 500:
            tot += (500 * 5) / 100 + ((card.dining - 500) * 1) / 100
        else:
            tot += (card.dining * 5) / 100
    else:
        tot += (card.dining * 1) / 100
    if v1 == "Entertainment":
        if card.entertainment > 500:
            tot += (500 * 5) / 100 + ((card.entertainment - 500) * 1) / 100
        else:
            tot += (card.entertainment * 5) / 100
    if v1 == "Car Rental":
        if card.car_rental > 500:
            tot += (500 * 5) / 100 + ((card.car_rental - 500) * 1) / 100
        else:
            tot += (card.car_rental * 5) / 100
    else:
        tot += (card.car_rental * 1) / 100

    if v1 == "Hotel":
        if card.hotel > 500:
            tot += (500 * 5) / 100 + ((card.hotel - 500) * 1) / 100
        else:
            tot += (card.hotel * 5) / 100
    else:
        tot += (card.hotel * 1) / 100
    if v1 == "Retail":
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

def discover_student_credit_card(card):
    tot = 0
    tot += (card.total * 5) / 100 #fix later lol
    return tot

# Discover It Miles
def discover_it_miles(card):
    tot = 0
    tot += (card.total * 1.5) / 100
    return tot

# Discover It Chrome
def discover_it_chrome(card):
    tot = 0
    tot += (card.gas * 2) / 100
    tot += (card.dining * 2) / 100
    tot += (card.total - card.gas - card.dining) / 100
    return tot

# Synchrony Sam's Club Mastercard
def synchrony_sams_club_mastercard(card):
    tot = 0
    tot += (card.gas * 5) / 100
    tot += (card.total - card.gas) / 100
    return tot

# Synchrony PayPal Cashback Mastercard
# def synchrony_paypal_cashback_mastercard(card):
#     tot = 0
#     if card.digital_wallet:
#         tot += (card.total * 3) / 100
#     else:
#         tot += (card.total * 2) / 100
#     return tot

# Apple Card
# def apple_card(card):
#     tot = 0
#     if card.digital_wallet:
#         tot += (card.total * 2) / 100
#     else:
#         tot += (card.total * 1) / 100
#     return tot

# US Bank Cash+ Visa Signature Card
def us_bank_cash_plus_visa_signature(card):
    v1, v2 = card.extract_max_values(2)
    tot = 0
    if v1 == "Flights" or v2 == "Flights":
        if card.flights > 2000:
            tot += (2000 * 5) / 100 + ((card.flights - 2000) * 1) / 100
        else:
            tot += (card.flights * 5) / 100
    else:
        tot += (card.flights * 1) / 100

    if v1 == "Groceries" or v2 == "Groceries":
        if card.groceries > 2000:
            tot += (2000 * 5) / 100 + ((card.groceries - 2000) * 1) / 100
        else:
            tot += (card.groceries * 5) / 100
    else:
        tot += (card.groceries * 2) / 100

    if v1 == "Gas" or v2 == "Gas":
        if card.gas > 2000:
            tot += (2000 * 5) / 100 + ((card.gas - 2000) * 1) / 100
        else:
            tot += (card.gas * 5) / 100
    else:
        tot += (card.gas * 2) / 100

    if v1 == "Dining" or v2 == "Dining":
        if card.dining > 2000:
            tot += (2000 * 5) / 100 + ((card.dining - 2000) * 1) / 100
        else:
            tot += (card.dining * 5) / 100
    else:
        tot += (card.dining * 2) / 100

    if v1 == "Entertainment" or v2 == "Entertainment":
        if card.entertainment > 2000:
            tot += (2000 * 5) / 100 + ((card.entertainment - 2000) * 1) / 100
        else:
            tot += (card.entertainment * 5) / 100
    else:
        tot += (card.entertainment * 1) / 100

    if v1 == "Car Rental" or v2 == "Car Rental":
        if card.car_rental > 2000:
            tot += (2000 * 5) / 100 + ((card.car_rental - 2000) * 1) / 100
        else:
            tot += (card.car_rental * 5) / 100
    else:
        tot += (card.car_rental * 1) / 100

    if v1 == "Hotel" or v2 == "Hotel":
        if card.hotel > 2000:
            tot += (2000 * 5) / 100 + ((card.hotel - 2000) * 1) / 100
        else:
            tot += (card.hotel * 5) / 100
    else:
        tot += (card.hotel * 1) / 100

    if v1 == "Retail" or v2 == "Retail":
        if card.retail > 2000:
            tot += (2000 * 5) / 100 + ((card.retail - 2000) * 1) / 100
        else:
            tot += (card.retail * 5) / 100
    else:
        tot += (card.retail * 1) / 100

    return tot

# U.S. Bank Altitude® Reserve Visa Infinite® Card

# def us_bank_altitude_reserve_visa_infinite(card):
#      tot_points = 0
#      tot_dollar_value = 0
#     if card.digital_wallet:
#         tot_points += card.hotel * 3
#         tot_points += card.car_rental * 3
#     else:
#         tot_points += card.hotel * 5 # Assuming 1x points for these categories
#         tot_points += card.car_rental * 5
#     tot_dollar_value += tot_points / 5  # Convert points to dollar value
#     tot_dollar_value = min(tot_dollar_value, 325)  # Ensure the reward does not exceed $325
#     tot_dollar_value += card.total
#     tot_dollar_value -= 400  # Deducting the annual fee (or whatever this value represents)
#     return tot_dollar_value

#U.S. Bank Business Cash Rewards World Elite™ Mastercard® review 
def us_bank_business_cash_rewards_world_elite_mastercard(card):
    tot = 0
    tot += (card.flights * 3) / 100
    tot += (card.hotel * 3) / 100
    return tot

#Wells Fargo Active Cash® Card 
def wells_fargo_active_cash(card):
    tot = 0
    tot += (card.total * 2) / 100
    return tot

# Wells Fargo Reflect® Card
def wells_fargo_autograph(card):
    tot_points = 0
    tot = 0
    if card.dining:
        tot_points += card.dining * 3
    if card.gas:
        tot_points += card.flights * 3
    if card.groceries:      
        tot_points += card.gas * 3
    if card.entertainment:    
        tot_points += card.entertainment * 3
    tot += tot_points / 100
    return tot

# hotel.com® Rewards Visa® Credit 
# def wells_fargo_hotel_com_rewards_visa(card):

# USAA Cashback Rewards Plus American Express Card
def usaa_cashback_rewards_plus_american_express(card):
    tot = 0
    tot += (card.gas * 5) / 100
    tot += (card.groceries * 2) / 100
    tot += (card.total - card.gas - card.groceries) / 100
    return tot

#Preferred Cash Rewards Visa® Signature Credit Cards Card
def usaa_preferred_cash_rewards_visa_signature(card):
    tot = 0
    tot += (card.total * 1.5) / 100
    return tot

def usaa_rewards_american_express(card):
    tot_points = 0
    tot = 0
    if card.dining:
        tot_points += card.dining * 3
    if card.gas:
        tot_points += card.flights * 2
    if card.groceries:      
        tot_points += card.gas * 2
    if card.hotel:
        tot_points += card.hotel * 2
    if card.entertainment:    
        tot_points += card.entertainment * 3
    tot += tot_points / 100
    return tot

