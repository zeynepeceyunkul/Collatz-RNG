from rng import CollatzRNG, default_seed

rng = CollatzRNG(default_seed())
print("Seed:", rng.seed)

nums = [rng.next_mod30() for _ in range(30)]
print("Çıktılar (0–29):")
print(nums)
