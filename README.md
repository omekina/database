# Plory's database

Trying to create something like SQL just for fun. :) I'm trying to optimize everything from the start, so new updates might not come right away.<br />
This is still just a development version and should not be used in production


## Table file structure
> ## HEAD (10 octets)
> Version (12-bit unsigned integer)<br />
> Flags (16 x 1-bit boolean)<br />
> Layout length (12-bit unsigned integer)<br />
> LUT length (36-bit unsigned integer)<br />
> LUT padding length (4-bit unsigned integer)
> ## LAYOUT (variable length)
> Columns
> > IsKey (1-bit boolean)<br />
> > IsAutoIncrement (1-bit boolean)<br />
> > Datatype (6-bit unsigned integer)<br />
> > Name length (8-bit)
>
> > ...
> ## LUT (variable length)
> Rows
> > IsFull (1-bit boolean)<br />
> > If row is full, then the following is defined<br />
> > Pointer length (7-bit unsigned integer)<br />
> > Value length/Pointer (?-bit unsigned integer)
>
> Padding (?x 1-bit null)
> ## Data (variable length)
> Row names<br />
> Values
