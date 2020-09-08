# Growth Hacker Demo: Growth and Price Prediction.

This project is for predicting 🔮 sell prices 💰 of Online Businesses 🖥 . As well as predicting Growth Targets📈📊for Online Business owners 👩‍💻👨‍💻.

What are Growth Targets 🎯 you may ask ?? 🤔. Simple, it is a target for a business to reach in order to sell at a particular price 😁.

![Making-of Animation](https://media.giphy.com/media/W2X3rtLoqq2GxfN4L5/giphy.gif)

# So how does it work ?

Data is scraped from online business marketplace sites. These sites include [Empire Flippers](https://empireflippers.com/), [Flippa](https://flippa.com/), and [Exchange Market](https://exchangemarketplace.com/shops?page=1&sortBy=salePriceHighToLow). Veiw the web scrapers here 
[Empire Scraper](https://github.com/alxanderpierre/My_EmpireProject), [Flippa Scraper](https://github.com/alxanderpierre/My_FlippaProject/tree/master/flippa_/flippa).

Data is then stored in a database to later be used for modeling purposes. Models are pickled and then used to make predictions. 

# How to run application locally?
```
pip install streamlit
streamlit run app.py 
```
