# Nostradamus: Weathering Worth

## Sources

### US stock market data

- ZEPL US Stock Market Data for Data Science
- yfinance API

### Environmental Data

- Knoema Environmental Data Atlas
- NOAA Climate Data Online

### Finding Correlations with Environmental Factors

From our environmental dataset, we first analyze the factors that can affect stocks or the other way: companies have an effect on these factors.

For example, the following environmental factors were present in our dataset, among others:

```
Use of potash
Methane emissions
CO2 emissions
Terrestrial and marine protected areas
CO2 emissions from gaseous fuel consumption
CO2 intensity
Use of nitrogen
```

### Correlating with Stocks

We considered all these environmental factors and some example stocks.

We plotted the yearly average open prices of these stocks. We also plotted the yearly value of these environmental factors.

Along with the plots, we also found out the value of correlation between the average yearly opening prices and the yearly value for the environmental factors.

![img](https://cdn.discordapp.com/attachments/809873815050911798/899330204676272128/unknown.png)

where rxy is the value of correlation (or the correlation coefficient) between x and y.

Here are the results:

![Untitled](assets/Untitled.png)

Here, we have normalized values of Open, Close and Volume of several stocks contrasted with normalized values of several environmental factors, meant to depeict whether there is any sign of possible correlation.

### Inferences

Some of the correlation values were extremely low (including negative values). And some of the values were very high.

### **What can we infer from these values?**

**Strong Correlations**

High values of correlation **usually** mean that there is an interdependence (Strong Correlation) between a stock and an environmental factor.

Consider the stock **BP** (British petroleum Company) and the factor **CO2 emmissions**:

![Untitled](assets/Untitled%201.png)

These have a high correlation value of `0.8159` .

We know that BP is an oil and gas company. Hence, it is very sensible reasoning that the company's production has a direct effect on the CO2 emmission.

Hence, we can infer that CO2 emmission values are affected by BP's stock.

**Causation $\neq$ Correlation.**

It is not always true that a high value of correlation means that there is an interdependence between the stocks.

Consider the stock **AAPL** (Apple) ****and the factor **CO2 emissions from gaseous fuel consumption:**

![Untitled](assets/Untitled%202.png)

These two have a high correlation of **0.93.**

We know know that Apple (a tech company), is obviously not dependent on CO2 emmissions from gaseous fuel consumption. Inspite of that, it has a high correlation with that factor.

This is not a result of a dependence between the two things. The high correlation is simply a coincidence as CO2 emmissions from gaseous fuels are rising because of the rapid population growth and because nuclear and other clean energy sources are not very prevalant.

Hence Correlation is not always a result of Causation.

**Hidden Correlations**

Sometimes, a stock and a factor which seem unrelated have a high correlation.

There are two possible explanations to this:

- It is a coincidence (as shown above)
- Or it has a hidden correlation

Consider the stock **EOD** (Wells Fargo Global) and the factor **CO2 emmissions:**

![Untitled](assets/Untitled%203.png)

This has a high correlation value of **0.927**.

On first thought, it seems like Well Fargo Global, a finance company is unrelated to CO2 emmissions.

However, it is likely that there are hidden correlations due to dependencies of carbon emissions on an industry which also determines whether the prices of companies which own/invest in the same.

This means large companies such as large banks and firms.

Hence, this high correlation is very likely not a result of coincidence but a result of purposeful investing/decisions taken by the company.

**Low Positive Correlations**

A low positive correlation usually means that the stock and the environmental factor in consideration is independent of each other.

Consider **XOM** and **Agricultural Methane Emissions**.

![Untitled](assets/Untitled%204.png)

This has a low correlation of **0.234**

Hence, we can most of the times conclude that these two are independent of each other.

In rare cases though, they could be dependent and still have a low correlation.

**Highly Negative Correlations**

Highly negative values of correlation **usually** imply an inverse effect between the company's production/success and the factor in consideration.

Consider the volume of the stock **CVX** (Chevron Corporation) ****and the factor **Terrestrial and marine protected areas**.

![Untitled](assets/Untitled%205.png)

This has a highly negative correlation of **-0.899**

It is fair to assume that when the number of terrestrial and marine protected areas increases, the volume of the stock CVX, which is an energy industry decreases.

Hence, a highly negative correlation value means inverse dependence.

### Predictions

![Untitled](assets/Untitled%206.png)

The global emission levels are predicted to be stranded due to growing awareness about climate change and a noticeable switch to renewable sources as a primary energy sources.

As we earlier saw the high correlation between the carbon emission levels and the stock price of BP, it can be analyzed that in coming times the stock price of BP and other large oil companies will begin to fall. This also means that there will be a rise in the stock prices of companies that provide an alternative source of fuels such as solar panels and wind mills.

# Natural Disasters

We will also explore what kind of effect Natural Disasters have on stock values.

### California Wildfires

![Untitled](assets/Untitled%207.png)

(The blue line is the duration of the disaster)

### Katrina Hurricane

In August 2005, Katrina was a category 5 Atlantic hurricane that caused over 1,800 deaths and $125 billion in damage. This damage was mainly focused on New Orleans and the surrounding areas.

Large transportation companies such as C.H. Robinson had to face a heavy loss due to denial of services. Since hurricanes leave a relatively smaller effect on companies, they are able to resume their services. so the loss is made back.

![Untitled](assets/Untitled%208.png)

![Untitled](assets/Untitled%209.png)

![Untitled](assets/Untitled%2010.png)

### Texas Storm

In February 2021, the state of Texas suffered a major power crisis, which came about as a result of three severe winter storms sweeping across the United States. The storms caused a massive electricity generation failure in the entire state leading to shortages of water, food, and heat.

More than 4.5 million homes and businesses were left without power, at least 210 people were killed directly or indirectly with some estimates going as high as 702.

The Texas Grid failure was majorly caused by the inadequately winterized natural gas equipment.

NRG suffered the most as can be seen in the following plots. It can also be emphasized that the analysis has to be done on a small time scale as companies often bounce back from such losses over a longer period of time such as a year. 

![Untitled](assets/Untitled%2011.png)

![Untitled](assets/Untitled%2012.png)

### 9/11 Disaster

Although 9/11 is not a natural disaster, it is worth considering how it affected the stock market. The effect is very visible on the entire stock market due to direct or indirect loss. As seen in the bottom graphs, the prices go down relatively fast after the event took place.

Due to its surprising nature, the impact's nature and magnitude were no less than a natural disaster over the country.

![Untitled](assets/Untitled%2013.png)

![Untitled](assets/Untitled%2014.png)

![Untitled](assets/Untitled%2015.png)

For all these disasters, stocks of companies that seemed related to those events were taken into consideration.

In agreement to our hypothesis, the stocks of those companies suffered a heavy hit after those events.

**Interdependence between companies**

It is also interestingly evident from the graphs that some companies are dependent on each other.

Consider the California fires:

![Untitled](assets/Untitled%2016.png)

![Untitled](assets/Untitled%2017.png)

The stock of **PCG** which is a gas and electric company was affected right after the disaster took place.

But now consider **EIX.** Its stock fell sharply some time after **PCG**'s.

We know that EIX depends on PCG for its production. This is also evident through the graph as its stock was not affected directly after the wildfires but a few days later.

This gives clear information about dependence of companies on each other. 

 

## Industrial Revolution

The example of correlation and not causation can further be understood by considering the rise in the population and workforce. The rise in population meant more consumption of energy and since we lack any large source of energy other than fossil fuels it means that there will be a rise in the pollution levels.

### Lack of Data

![Untitled](assets/Untitled%2018.png)

![Untitled](assets/Untitled%2019.png)

If the stock history of the industrial revolution times along with the carbon emission levels of the same was available, it can be seen that the rising workforce and demand directly meant a rise in carbon levels. This is a correlation due to common sources of the rise.

## Future Work

The data has been analyzed so far which has us given some insights, it can be used to build upon for prediction and more analysis for determining the effect of stocks on future natural events. 

Once the prediction model has been built, it can be used to analyze environmental factors. For example, when we compare the predicted value of a stock to its actual value, and there is a big difference at some point, it implies that some kind of environmental factor affected that stock at that point.

### Repeated events

Events such as hurricanes and heatwaves recur periodically. Due to rising climate change, they will only become more frequent. This means that past analysis on such events will help us determine the kind of impact it will happen on the companies it had an impact on.

# Conclusion

This analysis has revealed that there are correlations underlying between the stock value and the environmental factors such as weather and natural disasters. Further, major events which were unpredictable but aren't natural causes also have a heavy effect on the market. It can also be seen that the increase in supply and demand had a direct impact on the market stock, along with which there was an impact on environmental factors such as carbon emissions.

There are cases that have been explained where the impact of a natural disaster first hit the company which had a direct link to the resources that were lost followed by a loss in the companies that depended upon the primary companies after a delay.

The data can be understood and analyzed with graphs and other tools, predictions can be made with the help of machine learning models which could be trained on used in a case such events are repeated again.
