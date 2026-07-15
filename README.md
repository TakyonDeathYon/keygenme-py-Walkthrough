# keygenme-py Walkthrough

You can find the original challenge [here](https://learn.cylabacademy.org/library/121?page=1&search=keygen).

In this repository you can find the file given to you in the challenge,
`keygenme-trial.py`, and a file with some code to my solution, `picoCTFgen.py`.
In this walkthrough, I will not only provide the answers, but also try
to give context to my though process while solving it and how you might
come to the same solution for a similar problem yourself.

First things first, we are given not context to what the `keygenme-trial.py`
is or might do, all we know is that we are looking for a flag in the form of
`picoCTF{*flag*}`. So now we have to do some hunting.

Looking at the code we can see the following lines near the start:

```python
key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

This is promising, it appears to be exactly what we are looking for with the
`key_full_template_trial` being `picoCTF{1n_7h3_kk3y_of_xxxxxxxx}`. However,
if we try and enter it as the solution, it is incorrect. Notice one of the
variable names is `key_part_dynamic1_trial`, which suggests that it will
change. However, it is unclear as to how.

My next step is to continue looking through the code and try to get an
overall idea of what it does. It has the following functions: `intro_trial()`,
`menu_trial()`, `validate_choice()`, `estimate_burn()`,
`locked_estimate_vector()`, `enter_license()`, `check_key()`,
`decrypt_full_version()` and `ui_flow()`. A few of these look interesting
just from their names: `decrypt_full_version()` and `check_key()`. Both of
these have something to do with decrypting or a key, which seems like a good
place to start for finding the rest of the flag.

`decrypt_full_version()` changes a lot of global variables and also writes to
a file a decrypted `full_version_code`. This could be promising, the full
version code may have the rest of the flag, but before going deeper it is
a good idea to keep skimming through the code for anything more obvious.

`check_key()` looks very interesting, it directly compares a `key` variable
against the static part of `key_full_template_trial`, but then compares
the indexes of the dynamic part to something else. This looks exactly
like what we need. The dynamic indexes are being compared against
different indexes of `hashlib.sha256(username_trial).hexdigest()`. So
all we need to do is, get what this value is and change the dynamic
indexes to the indexes of this has specified in `check_key()`.

In order to do this I am just going to edit the file to print this value
before it does anything else on line 260:

```python
print(hashlib.sha256(bUsername_trial).hexdigest())
# Enter main loop
ui_flow()
```

There is a slight difference to what you might have expected here, the
inputted variable is `bUsername_trial` not `username_trial`, as
`username_trial` is a local variable in `check_key()` (which happens to
be named the same as a global variable!). Then when `check_key()` is
called (in the `enter_license()` function), the value that is passed is
`bUsername_trial`.

Now if you run the file, you will get the following output:

```
ba6c084a4d888e1f7c3b0fc71d61c4625708bd915b5e0e60eb73e1667251b567

===============================================
Welcome to the Arcane Calculator, BENNETT!

This is the trial version of Arcane Calculator.
The full version may be purchased in person near
the galactic center of the Milky Way galaxy. 
Available while supplies last!
=====================================================


___Arcane Calculator___

Menu:
(a) Estimate Astral Projection Mana Burn
(b) [LOCKED] Estimate Astral Slingshot Approach Vector
(c) Enter License Key
(d) Exit Arcane Calculator
What would you like to do, BENNETT (a/b/c/d)? 
```

At the top we can see the value we want. Now all there is to do is
to replace the dynamic indexes of the flag with the correct indexes
we can see in the `check_key()` function:

```python
def check_key(key, username_trial):

    global key_full_template_trial

    if len(key) != len(key_full_template_trial):
        return False
    else:
        # Check static base key part --v
        i = 0
        for c in key_part_static1_trial:
            if key[i] != c:
                return False

            i += 1

        # TODO : test performance on toolbox container
        # Check dynamic part --v
        if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
            return False
        else:
            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
            return False

        return True

```

From this you can see that the dynamic indexes are replaced by
the 4^th^, 5^th^, 3^rd^, 6^th^, 2^nd^, 7^th^, 1^st^ and 8^th^ of
`hashlib.sha256(bUsername_trial).hexdigest()` in that order. You
could do this by hand, but I decided to just write a short piece
of code to do this for me, which you can see in `picoCTFgen.py`.

And voila! If we enter the key we get, it is correct:

```
picoCTF{1n_7h3_kk3y_of_08c46aa4}
```
