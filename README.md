![Landing page](https://i.imgur.com/8LdxuK5.png)

# Inspiration
As college students, many of us are starting to think about building our credit score and getting a credit card, but websites like Credit Karma have sponsored affiliate links that make it hard to get unbiased reviews of the best credit cards.

# What it does
Introducing cardforme, a website that uses your previous bank transaction history to suggest the best credit cards for you. 

Our features include:
- Securely accessing your bank transactions through the Plaid API
- Top 5 credit card suggestions with the best discounts based on transaction categories and calculated with backtesting
- Data visualization for spending categories

# How we built it
 ![](https://i.imgur.com/Aolfqmg.jpg)
 The grind never stops >_< (waiting in the food line)

## Back End: 

We handled communications with banks through the **Plaid API**. To get the authentication to work, we used Plaid's version called Link, that takes a token from the user and exchanges it with an access token to secure a connection with the bank in question. 

After auth, we took the transactions data from the generated JSON in the post request and sent it to our Flask backend.

From this, we individually created functions for each credit card in our list and calculated the amount of benefits you would get. So for example, if you had a credit card that gave you 3x points per purchase on hotels, the calculation for the card would be and 1% on everything else, we could do something like. Each point and mile is being treated as 0.01 cents.

def hotel_card(card):
    tot = 0
    tot += (card.hotels * 3) / 100
    tot += (card.total - card.hotels) / 100
    return tot

![](https://i.imgur.com/cJaz7f1.jpg)

## Front End: 
We did the frontend with **Next.js** and **Typescript** creating a beautiful landing page and a main page with the suggested credit cards and data visualization.

Spent lots of time on Figma with color options, typography and several views for the design of the website. 

For our research on the cards, we gathered information from a wide range of sources to understand the various benefits they offer. We ended up examining close to **50 cards**, spanning a vast range of potential financial advantages.

After collecting the information, we realized that we needed a PNG image of each card and a link to its application. Given the number of companies we were dealing with, this was a daunting task. I wished there was an API for credit card bonuses so we didn't have to search manually! >:(

Nonetheless, this endeavor provided a valuable data layer, enhancing the functionality of our project. 😎 The benefits also resulted in a calculation for added rewards you would recieve should you choose any of our cards, and in order to find the best, we calculated every card to show you the one for you!

# Challenges we ran into

The **Plaid API** was definitely one of the more time consuming things that we did during the hackathon because authentication just refused to work. We were able to get it to work eventually and pulling the transactions thankfully didn't take as much time. 

Brandon also spent ~8 hours trying to fix an API request that just wouldn't work. Turns out it was working the entire time and his backend code was scuffed ^.^

# Accomplishments that we're proud of

Website design do be popping off, definitely a different theme than we usually pivot to. We were able to get everything onto the website that we wanted, although it took much longer that we would have liked.

# What we learned

- Plaid API can go spontaneously combust! >:(((
- Stuti's first time trying backend (that was an ....experience)
- Burrito bowls are amazing but do not make the stomach happy :(

# What's next for cardforme
- moving to mobile
- wider range of data, showing more details about spending history
- adding more cards, hopefully we can automate that bc it was sm time and effort D:
