# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?
The model becomes around 20% less accurate, based upon the r^2 val, this is becasue without the scaler the individual variables are weighted diffrenty and have a disproportinate effect on the model.
2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.
the model has an r^2 value of around .8 so I would say that generally, this is accurate enough. Although I don't know if I would say that it is accurate enough for the given use case, since there are more factors that go into the purchase of a car that are not represented by the model, such as the location of the dealership or maybe even the time of year. 
3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

