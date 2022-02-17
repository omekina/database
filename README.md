# Plory's database

Trying to create something like SQL just for fun. :) I'm trying to optimize everything from the start, so new updates might not come right away.<br />
This is still just a development version and should not be used in production


## Table file structure
> ## HEAD
> Version (12-bit unsigned integer)<br />
> Flags (12 x 1-bit booleans)<br />
> Layout length (12-bit unsigned integer)<br />
> LUT length (36-bit unsigned integer)<br />
