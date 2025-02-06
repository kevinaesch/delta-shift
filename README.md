# README delta-shift
# Introduction
| **Input** | **Tasks** | **Output**                                    | **API, requests per {min, day}** |
|-----------|-----------|-----------------------------------------------|----------------------------------|
| Market    |           | y=$(t)                                        | alphavantage 5/m, 100/d req      |
| St        |           | multiline chart with multi-year $(t)          | tradedata 8/m, 800/d             |
| tFilter   |           | moving average $(t)                           |                                  |
|           |           | Event Calendar                                |                                  |
|           |           | average_$(t) extrapolation at defined buckets |                                  |
|           |           | Jupyter NB for analysis                       |                                  |

## Execution Scripts
<code>
$ poetry run ds
</code>

## Trading Data API: 
free tier limitations: requests per minute, requests per day  
* twelvedata.com 8/m, 800/d
* alphavantage 5/m, 100/d

