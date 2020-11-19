# python_modhex

When working with yubikeys, you get OTPs in `modhex`, which according to https://developers.yubico.com/OTP/Modhex_Converter.html
> is similar to hex encoding but with a different encoding alphabet.

The alphabet is `ALPHABET = "cbdefghijklnrtuv"`.

This module merely does what https://developers.yubico.com/OTP/Modhex_Converter.html offers as well:
* Convert a `modhex` string to `hex`.
* Convert a `hex` string to `modhex`.


## Installation

`pip install python_modhex`

## 

The installation also creates an executable, thatprovidesa simple interfaces:
```
python_modhex --version
python_modhex --help

# From modhex.
python_modhex from-modhex cccccctcjhhrrrdeejrtrvdldhthenggvuedgfevjecu <list_of_modhex_strings>

# To modhex.
python_modhex to-modhex 000000d0866ccc2338cdcf2a26d63b55fe32543f830e <list_of_hex_strings>
```


## Use as module
```
>>> from python_modhex.python_modhex import from_modhex, to_modhex
>>> modhex = "cccccccgklgcvnkcvnnegrnhgrjkhlkfhdkclfncvlgj"
>>> hex_ = "000000059a50fb90fbb35cb65c896a946290a4b0fa58
>>>
>>> from_modhex(modhex)
>>> 000000059a50fb90fbb35cb65c896a946290a4b0fa58
>>>
>>> to_modhex(hex_)
>>> cccccccgklgcvnkcvnnegrnhgrjkhlkfhdkclfncvlgj
```
