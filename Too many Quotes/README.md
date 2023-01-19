
# Too many Quotes

Author: [Swati Verma](https://github.com/Swati-Verma671)

## Description

This challenge will need the player to know what web scraping is. The quotes in the provided website are all jumbled and will need to be arranged in order if you want to look for particular hints.

```
https://swati-verma671.github.io/Motivational-Quotes/

The website which motivates you through your tiresome and gruesome trial to find the flag. Your best bet is to look for and filter perseverance-quotes.
Also, enclose the word you get in- wtfCTF{}

```

## Exploit

The website has a collection of many quotes and sayings from different, famous persons. However, it isn't specified the values they exhibhit. You will have to find out that by going to the source code. But instead of looking for the class 'perseverance' everywhere and looking for the hint, you can write a code and use a web scraper to get the results.

First you web scrape perseverance quotes, you will get:-
"If you wish to look for the flag look for ""grit"" -Anonymous"

Second, you search for the word grit on the webpage, go to next if it isn't there. Web scraping another page for grit-quotes gives you:-
Looking for the flag, keep it up now look for "humility" -Anonymous

Third, as per given hint you will need to look for humility-related sayings. Looking for it in another page gives us:-
"Very well done, your answer is ScrapPed" -Anonymous

<br />

The flag is:
<br />

```
wtfCTF{ScrapPed}
```
