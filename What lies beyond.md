# What_lies_beyond

Author: [Swati](https://github.com/Swati-Verma671)

## Description
Look for the hints and clues in the source of the website to find the flag.


## Sources

- [Galaxies](https://swati-verma671.github.io/WhatLiesBeyond/)

```

The creator of this website left a really important information here. Can you look for it?
https://swati-verma671.github.io/WhatLiesBeyond/
```

## Exploit

<!-- Much more detailed description than the following. -->
Check the page source of the given website. There are many comments, one of the comments talks about the caesar's comet and also gives a string -(fdhoxp).
This is the clue that the string is encrypted in caesar cipher. Decrypt the string and the string now spells "caelum". Download the image used for caelum
and use any steganograpy tool to decode the text hidden beneath. You will get the flag.
<br />

The flag is:

```
turingCTF{wh4t_l13s_b3n34th}
```
