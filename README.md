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
if we try and enter it as the solution we get told it is incorrect. We must
look closer. One of the variable names is `key_part_dynamic1_trial`, which
seems to suggest that it might change. Now we just have to figure out to
what.

My next step is to continue looking through the code and just try to piece
together what is going on.
