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


Company: American Express <br />
Card: American Express Business Gold Card <br />
Annual Fee: 295 <br />
Name in code: amex_business_gold <br >
Benefits:
-  Get 4X Membership Rewards points on the 2 select categories where your business spent the most each month. (**4X points apply to the first $150,000 in combined purchases from these 2 categories each calendar year.*)
- 1X is earned for other purchases. **
---
Company: Bank of America <br />
Card: Bank of America Travel Rewards credit card <br />
Annual Fee: 0 <br />
Name in code: bofa_travel_rewards <br >
Benefits:
- Earn unlimited 1.5 points per $1 spent on all purchases, with no annual fee and no foreign transaction fees and your points don't expire.
---
Company: Bank of America <br />
Card: Bank of America Customized Cash Rewards credit card <br />
Annual Fee: 0 <br />
Name in code: bofa_customized_cash_rewards <br >
Benefits:
- Earn 3% cash back in the category of your choice (up to $2,500 in combined choice category/grocery store/wholesale club quarterly purchases).
- 2% at grocery stores and wholesale clubs (up to $2,500 in combined choice category/grocery store/wholesale club quarterly purchases).
- 1% Earn unlimited 1% on all other purchases.
---
Company: Bank of America <br />
Card: Bank of America Business Advantage Customized Cash Rewards Mastercard credit card <br />
Annual Fee: 0 <br />
Name in code: bofa_business_advantage_customized_cash_rewards_mastercard <br >
Benefits:
- 3% cash back in the category of your choice (on the first $50,000 in combined choice category/dining purchases each calendar year, 1% thereafter).
- 2% cash back on dining purchases (on the first $50,000 in combined choice category/dining purchases each calendar year, 1% thereafter).
- 1% unlimited cash back on all other purchases.
---
Company: Bank of America <br />
Card: Bank of America Premium Rewards credit card <br />
Annual Fee: 95 <br />
Name in code: bofa_premium_rewards <br >
Benefits:
- 2 points for every $1 spent on travel and dining purchases
- 1.5 points for every $1 spent on all other purchases
---
Company: Bank of America <br />
Card: Bank of America Unlimited Cash Rewards credit card <br />
Annual Fee: 0 <br />
Name in code: bofa_unlimited_rewards <br >
Benefits:
- Earn unlimited 1.5% cash back on all purchases.
---
Company: Barclays <br />
Card: AAdvantage Aviator Red World Elite Mastercard <br />
Annual Fee: 99 <br />
Name in code: barclays_aviator_red_world_elite_mastercard<br >
Benefits:
- 2X miles per dollar spent on eligible American Airlines purchases and 1X miles on all other purchases
---
Company: Barclays <br />
Card: The Hawaiian Airlines World Elite Mastercard <br />
Annual Fee: 99 <br />
Name in code: barclays_the_hawaiian_airlines_world_elite_mastercard <br >
Benefits:
- Earn 3X miles per $1 on eligible Hawaiian Airlines purchases and 2X miles per $1 on grocery store (excluding Target and Walmart purchases), gas and dining transactions; 1X mile per $1 on all other transactions.
---
Company: Barclays <br />
Card: JetBlue Card <br />
Annual Fee: 0 <br />
Name in code: barclays_jetblue <br >
Benefits:
- 3X points on eligible JetBlue purchases, 2X points at restaurants and grocery stores and 1X points on all other purchases
---
Company: Capital One <br />
Card: Capital One Quicksilver Cash Rewards Credit Card <br />
Annual Fee: 0 <br />
Name in code: captial_one_quicksilver_cash_rewards <br >
Benefits:
-  Earn unlimited 5% cash back on hotels and rental cars booked through Capital One Travel, where you'll get Capital One's best prices on thousands of trip options. Terms apply
- Earn unlimited 1.5% cash back on every purchase, every day
---
Company: Capital One <br />
Card: Capital One SavorOne Cash Rewards Credit Card <br />
Annual Fee: 0 <br />
Name in code: captial_one_savorone_cash_rewards <br >
Benefits:
- Earn 10% Cash Back on purchases made through Uber & Uber Eats, plus complimentary Uber One membership statement credits through 11/14/2024
- Earn 8% Cash Back on Capital One Entertainment purchases
- Earn unlimited 5% Cash Back on hotels and rental cars booked through Capital One Travel, where you'll get Capital One's best prices on thousands of trip options. Terms apply
- Earn 3% Cash Back on dining and at grocery stores (excluding superstores like Walmart® and Target®)
- Earn 3% Cash Back on popular streaming services and entertainment
- Earn 1% Cash Back on all other purchases
---
Company: Capital One <br />
Card: Capital One Venture Rewards Credit Card <br />
Annual Fee: 95 <br />
Name in code: captial_one_venture_rewards <br >
Benefits:
- 5 Miles per dollar on hotels and rental cars booked through Capital One Travel
-  2 Miles per dollar on every purchase, every day
---
Company: Capital One <br />
Card: Capital One VentureOne Rewards Credit Card <br />
Annual Fee: 0 <br />
Name in code: captial_one_ventureone_rewards <br >
Benefits:
- 5 Miles per dollar on hotels and rental cars booked through Capital One Travel
- 1.25 Miles per dollar on every purchase, every day
---
Company: Capital One <br />
Card: Capital One Venture X Rewards Credit Card <br />
Annual Fee: 395 <br />
Name in code: captial_one_venture_x_rewards <br >
Benefits:
- 10 Miles per dollar on hotels and rental cars booked through Capital One Travel
- 5 Miles per dollar on flights booked through Capital One Travel
- 2 Miles per dollar on every purchase, every day
---
Company: Capital One <br />
Card: Capital One Spark Miles for Business <br />
Annual Fee: 95 <br />
Name in code: captial_one_spark_miles_for_business <br >
Benefits:
- Unlimited 5X miles on hotels and rental cars booked through Capital One Travel
-  Earn unlimited 2X miles per dollar on every purchase, everywhere, no limits or category restrictions, and miles won't expire for the life of the account.
---
Company: Chase <br />
Card: Chase Sapphire Preferred Card <br />
Annual Fee: 95 <br />
Name in code: chase_sapphire_preferred <br >
Benefits:
- 5x on travel purchased through Chase Ultimate Rewards®
- 3x on dining
- 2x on all other travel purchases, plus more
---
Company: Chase <br />
Card: Ink Business Cash® Credit Card <br />
Annual Fee: 0 <br />
Name in code: chase_ink_business_cash <br >
Benefits:
- Earn 5% cash back on the first $25,000 spent in combined purchases at office supply stores and on internet, cable and phone services each account anniversary year
- Earn 2% cash back on the first $25,000 spent in combined purchases at gas stations and restaurants each account anniversary year
- Earn 1% cash back on all other card purchases with no limit to the amount you can earn
---
Company: Chase <br />
Card: Chase Sapphire Reserve® <br />
Annual Fee: 550 <br />
Name in code: chase_sapphire_reserve <br >
Benefits:
- Earn 1 point per $1 spent on all other purchases
- Earn 3x points on other travel and dining.
- Earn 10x total points on hotels and car rentals when you purchase travel through Chase Ultimate Rewards®.
- Earn 1 point per $1 spent on all other purchases
---
Company: Chase <br />
Card: Ink Business Unlimited® Credit Card <br />
Annual Fee: 900 <br />
Name in code: chase_ink_business_unlimited <br >
Benefits:
-  Earn unlimited 1.5% cash back on every purchase made for your business
---
Company: Citi <br />
Card: Citi Custom Cash® Card <br />
Annual Fee: 0 <br />
Name in code: citi_custom_cash <br >
Benefits:
- Earn 5% cash back on purchases in your top eligible spend category each billing cycle, up to the first $500 spent, 1% cash back thereafter.
- Earn unlimited 1% cash back on all other purchases.
---
Company: Citi <br />
Card: Citi Double Cash Card <br />
Annual Fee: 0 <br />
Name in code: citi_double_cash <br >
Benefits:
- Up to 2% cash back (1% at time of purchase, then 1% at time of payment) on all purchases
---
Company: Citi <br />
Card: Citi Premier Card <br />
Annual Fee: 0 <br />
Name in code: citi_premier <br >
Benefits:
- 3X ThankYou Points per $1 on restaurant, supermarket, gas station, hotel and air travel purchases
- 1X Points on all other purchases.
- Plus, for a limited time, earn a total of 10 ThankYou® Points per $1 spent on hotel, car rentals, and attractions (excluding air travel) booked on the Citi TravelSM portal through June 30, 2024.
---
Company: Citi <br />
Card: Citi Rewards+ Card <br />
Annual Fee: 0 <br />
Name in code: citi_rewards <br >
Benefits:
- 2X ThankYou® Points at supermarkets and gas stations (for the first $6,000/year, then 1 point per $1), and 1 point on all other purchases
---
Company: Citi <br />
Card: Citi® / AAdvantage® Platinum Select® World Elite Mastercard® <br />
Annual Fee: 99 <br />
Name in code: citi_aadvantage_platinum_select <br >
Benefits:
- 2 AAdvantage® miles for every $1 spent at gas stations, restaurants and on eligible American Airlines purchases
---
Company: Discover <br />
Card: Discover it® Cash Back <br />
Annual Fee: 0 <br />
Name in code: discover_it_cash_back <br >
Benefits:
- Earn 5% cash back on everyday purchases at different places each quarter like Amazon.com, grocery stores, restaurants, and gas stations, up to the quarterly maximum when you activate.
- Plus, earn unlimited 1% cash back on all other purchases – automatically.
---
Company: Discover <br />
Card: Discover it® Balance Transfer <br />
Annual Fee: 0 <br />
Name in code: discover_it_balance_transfer <br >
Benefits:
- Earn 5% cash back on everyday purchases at different places each quarter like Amazon.com, grocery stores, restaurants, and gas stations, up to the quarterly maximum when you activate.
- Earn unlimited 1% cash back on all other purchases - automatically.
---
Company: Discover <br />
Card: Discover it® Miles <br />
Annual Fee: 0 <br />
Name in code: discover_it_miles <br >
Benefits:
-  Automatically earn unlimited 1.5x Miles on every dollar of every purchase - with no annual fee.
---
Company: Discover <br />
Card: Discover it® Chrome <br />
Annual Fee: 0 <br />
Name in code: discover_it_chrome <br >
Benefits:
- Plus, earn unlimited 1% cash back on all other purchases - automatically.
- Earn cash back on your next road trip with 2% cash back at Gas Stations and Restaurants on up to $1,000 in combined purchases each quarter.
---
Company: Discover <br />
Card: Discover it® Student Chrome<br />
Annual Fee: 0 <br />
Name in code: discover_it_student_chrome <br >
Benefits:
- Plus, earn unlimited 1% cash back on all other purchases - automatically.
- Earn 2% cash back at Gas Stations and Restaurants on up to $1,000 in combined purchases each quarter.
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
