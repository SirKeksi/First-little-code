# First-little-code

So, this was pretty much my first, more complicated code after I learned the basics of Python. It was a task given from an AI to test my abilites so here a little description [note that this is my first ever description and I don't know how detailed it should be:

It's a shopping system using three classes: one for a product, for a customer and the shop. I'd say many things are clear so I only go through some things

class product:
Here we have the deduct method. So if a customer buys something, we of course need to check if the product is available. That's the if-elif-else part. And I split two cases: the amount of the product is zero or the customer buys too much of it. I wanted to give the customer more precice information about what they did wrong so yeah. Also I let it return True and False, which will be important for another class

class customer:
First we have this empty dictionary. Here we collect every product and the amount the customer wants -> so the key is the an object from the product class and the value is the amount
Plus we have the value shop so the customer only buys things from the shop they belong to -> self.shop.pl is the list of the shop (further down)

Here we have the biggest method: buy. So first, we need to check if the product the customer searches even is available. I put an additional boolean variable "found" here to have better control over the process. So if the object the customer searched for is, well, selled by the shop, we need to check if the product is available. And that is where the True and False staes from the product method come into play. Because the customer additionaly gives how many items he wants to have, we of course need to check if the process is possible. If it's possible, we add the item to the dictionary

I believe the rest is a bit easier. We have a method to show the current shopping list, using .items so extract everything and add it into a new dictionary. Then a method to delete things from the list, again using a mechanism to check if the product is even in the shopping list. A method to increase the number of an item and the last method being to show the price of everything. Again using .items to get what I need

class shop:
We have two lists. One for the customers and one for the products. The products will be saved as an object which helps me with a lot of things (as seen at the customer class)

We have methods to add a new product to the list, using the product class. A method to check the amount of a product (again with a proccess to check if the product is even being sold) and lastly a method to show all the products



So, I know that there are things that can be done better or more. It just was important for me to get this code going without making it too complex first


