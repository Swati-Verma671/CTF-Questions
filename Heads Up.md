# Heads Up

Author: [Swati](https://github.com/Swati-Verma671)

## Description
This challenge requires the player to send HTTP headers to the server to get the flag.

```
This website was only accessible to a single agent a long time ago.
https://ctfwho.herokuapp.com/

```

## Exploit

Use any API platform like Postman to send HTTP headers to the website. The objective is to pretend to be a user who is accepted by the site to obtain the page with the flag.
The flaw exploited is in the HTTP request, and more precisely in the headers thereof, which we send to the server that we can modify and which allows us to access the different pages.
The key-value pairs should be like:-
 - 'User-Agent':'wtfBrowser'
 - 'Date':'2002'
 -  'Accept-Language':'ja'
<br />

The flag is:

```
turingCTF{v3rY_5m4rT_v3rY_c00L}
```
