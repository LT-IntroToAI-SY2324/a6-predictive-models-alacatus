# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
the r squard coefficient ranged from around .84->.86 so I would say that the model fits well to the type of data given 
2. Is your model accurate? Why or why not?
I would say that the model is relatively accurate considering that the value is above .75.
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
based on the sample data, for the ten year old car the model predicted the price to be around 8500 -> 9500 and for the second car the range was a bit more drastic(300 -> 2000, favoring the higher end), im assuming that in certain cases the data didn't pull from the higher range of values in the model and the higher values were also not as commonly found in the model itself. 
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
I think this is happening because as the age/mileage increases the price decreases, so if the a/m increases to a point where the model has not seen data like this since the dataset doesn't have a lot or any data points that are at these, the outcome is a negative number, even if not logically possible.