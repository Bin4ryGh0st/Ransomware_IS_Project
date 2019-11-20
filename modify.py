def modify_file_inplace(filename, crypto, blocksize=16):
    with open(filename, 'r+b') as f:
        plaintext = f.read(blocksize)

        while plaintext:
            ciphertext = crypto(plaintext)
            if len(plaintext) != len(ciphertext):
                raise ValueError('''Ciphertext({})is not of the same length of the Plaintext({}).
                Not a stream cipher.'''.format(len(ciphertext), len(plaintext)))

            f.seek(-len(plaintext), 1) # return to same point before the read
            f.write(ciphertext)

            plaintext = f.read(blocksize)

