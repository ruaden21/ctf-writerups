# Cheesy

## Information

**Category** | **Point** | **References**
--- | --- | ---
Reversing | 100 | Nah

**Description:**

>Where will you find the flag?

>#easy

**File:**

[reversing1](./reversing1)

## Solution

Check file information and run it.

<p align = "center">
    <img src = "./images/run_it.png">
</p>

It's an ELF 64-bit object and it gives us some strings look like base64 encoding strings. Try to decode them.

<p align = "center">
    <img src = "./images/decode_string.png">
</p>

Did I miss the flag string? Dump all the strings of the file.

<p align = "center">
    <img src = "./images/find_string.png">
</p>

I missed this string, didn't I? Decode it.

<p align = "center">
    <img src = "./images/flag.png">
</p>

**Flag:**
> gigem{3a5y_R3v3r51N6!}