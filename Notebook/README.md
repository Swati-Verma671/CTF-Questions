
# Notebook

Author: [Swati Verma](https://github.com/Swati-Verma671)

## Description

This challenge requires you to use very basics of web scrapping. The password is hidden in one of the inline elements used while building this website. All one has to do is to filter and extract the contents of the inline element, and you will get the flag.



```

The flag is hidden somewhere in this notebook but it is too difficult to make out can you search for it? Using inline elements might help.  -https://swati-verma671.github.io/Notebook/
```

## Exploit

Web scrapping is widely used for extracting information from websites and in this case a webpages too. We would need to use a module for this. In this case we use BeautifulSoup. Using this module we can get arranged and specifically described element from the html page source.
Now to get the flag, you will have to write a code to simply filter and extract all the paragraphs under the inline element-(span). Store them in a file preferably .csv and look for the flag.
 
<br />

If you were able to do this, you will get the flag which is:

<br />


```
wtfCTF{2_h4rd_2_s33}
```
