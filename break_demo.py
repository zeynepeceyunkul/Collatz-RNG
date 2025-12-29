from rng import CollatzRNG

def gen(seed, k=6):
    r = CollatzRNG(seed)
    return [r.next_mod30() for _ in range(k)]

def break_seed(observed, max_seed=100000):
    for s in range(1, max_seed):
        if gen(s, len(observed)) == observed:
            return s
    return None

secret = 42421
observed = gen(secret)

print("Gözlenen:", observed)
guess = break_seed(observed)
print("Tahmin edilen seed:", guess)
