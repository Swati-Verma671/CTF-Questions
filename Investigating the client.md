# Investigating the client

Author: [Swati](https://github.com/Swati-Verma671)

## Description

A login page that requires a certain password to unlock the hint for getting the flag.

```
Challenge description to go up on the website.

A very secure login form that can be opened only if you have the required password.
https://swati-verma671.github.io/Password/
```

## Exploit

The player would have to scourge the page source to get a collection of strings that make up the password require to get another hint which asks to visit hint.html. Upon arriving there we see another hint stating us to convert the password used to base64.

<br />

The flag is:

```
wtfCTF{c1i3nt_s1d3_l0g1n}
```
