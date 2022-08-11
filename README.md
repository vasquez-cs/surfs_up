# surfs_up

## Overview of the analysis: Explain the purpose of this analysis.
W. Avy, a potential investor of my surf shop that sells ice cream, likes my initial analysis of the weather dataset from Oahu. Despite liking the initial analysis, he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for June and December in Oahu, to determine if the surf and ice cream shop business is sustainable year-round. 

### Results:

<img src="https://user-images.githubusercontent.com/107224632/184074503-c4f9d902-ebae-480f-80ff-036987971a77.png" width=25% height=25%><br />
*Figure 1: df_jun Output*<br />

Figure 1 above is the output for June, which is the month that marks the start of summer with the summer solstice.

- Lowest temperature of the month is 64 degrees Fahrenheit
  - Expected to still have decent sales with a low temp of 64 degrees Fahrenheit
- Q1 or the 25% percentile is 73 degrees Fahrenheit 
  - Median for the lower set of data supports the investment of shop as sales during "cooler" days of the month would be steady as the temperature is still high
- Q1, Overall Median or 50% percentile, and Q3 or 75% percentile are all 2 degrees within each other
  - This again consistent temperature during the start of summer supports the hypothesis for steady sales during the month.

<img src="https://user-images.githubusercontent.com/107224632/184074326-0e87d106-de24-4a6d-9677-c277be8798e5.png" width=25% height=25%><br />
*Figure 2: df_dec Output*<br />

Figure 2 above is the output for December, which is the month that marks the start of winter with the winter solstice. Despite most of the mainland experiencing major changes in temperature in the summer months, we can see that:

- Lowest temperature of the month is 56 degrees Fahrenheit
  - Sales for ice cream may be slow, however, surfing in 56 degree weather is not unheard of, so surf shops will still have business
- Median for December is 71 degrees Fahrenheit
  - The median temperature is only 4 degrees off from the 74 degrees Fahrenheit median for June
  - This December median temperature supports the idea that business may be slow on a few days for ice cream, however, the average temp will have surfing gear or ice cream sales not experience a drastic dip in comparison to December
- Q1, Overall Median or 50% percentile, and Q3 or 75% percentile are all 5 degrees within each other
  - This again consistent temperature during the start of winter supports the hypothesis for perhaps a lower overall month of sales than June, but not wildly inconsistent weather that would disrupt sales and cause overall revenue to experience a large drop in comparison to June.

### Summary
We see in our summary of temperatures for June and December that our sales will be strong and consistent, considering the weather data for June. December may experience a drop off in overall sales, however, weather data tells us that despite a few extremes, our median temperature is comparable to June. Two additional queries that I would make would be for September and March. Having the summary of temperature data for these two months would allow us to get more information on temperature changes year-round, as we would have data in 3-month increments. We could create accurate plots to show the minimal changes in data and better visualize how consistent the temperatures are year around. In addition to temperature data, I would also pull similar summary statistics on the available precipitation data for the same months. This could give us a better idea of where precipitation might affect surfing sales. Overall, I think our data shows a strong argument for why our surf/ice cream shop has a good chance of being successful year-round.
