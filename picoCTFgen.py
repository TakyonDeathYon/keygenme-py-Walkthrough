key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = (
    key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
)
hashed = "ba6c084a4d888e1f7c3b0fc71d61c4625708bd915b5e0e60eb73e1667251b567"


def test(key, hashed):

    # Just indexing to the correct position where the dynamic part starts
    i = len(key_part_static1_trial)

    print(i, i + 8)
    # Make a string with the indexes at the correct positions
    out_key = (
        key[:i]
        + hashed[4]
        + hashed[5]
        + hashed[3]
        + hashed[6]
        + hashed[2]
        + hashed[7]
        + hashed[1]
        + hashed[8]
        + key[i + 8 :]
    )

    # Return the key value
    return out_key


print(test(key_full_template_trial, hashed))
