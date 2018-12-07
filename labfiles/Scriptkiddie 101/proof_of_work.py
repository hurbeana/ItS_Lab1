# proof-of-work.py
import hashlib
import sys

try:
    suffix = sys.argv[1]
except:
    suffix = "KKNrwOJpSoPnMS98rV5DXYWWSqod0aKs"
done = False
n = 100000

def mask(n, m):
    return ((1 << n) - 1) << (m - n)

def test_0bits(digest_bytes, n_bits):
    m = 8 * len(digest_bytes) 
    #print("{0:b}".format(mask(n_bits, m)))
    digest_num = int.from_bytes(digest_bytes, 'big')
    return digest_num & mask(n_bits, m) == 0

while done is False:
    m = hashlib.sha384()
    # 48 bytes total for sha384
    tohash = str(n) + suffix
    m.update(bytes(tohash, 'ascii'))

    #print(f"{tohash} with {n}")

    if test_0bits(m.digest(), 17):
        print(f"Found the hash with number {n}")
        done = True
    n = n + 1