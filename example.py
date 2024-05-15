from pedil import PEDIL

# Create an instance of the PEDIL class
pedil = PEDIL()

# Generate 5 IDs with 1 level of depth
id1 = pedil.get_or_create_prime_id("1")
id2 = pedil.get_or_create_prime_id("2")
id3 = pedil.get_or_create_prime_id("3")
id4 = pedil.get_or_create_prime_id("4")
id5 = pedil.get_or_create_prime_id("5")

# Generate 5 IDs with 2 levels of depth
id6 = pedil.get_or_create_prime_id("1,1")
id7 = pedil.get_or_create_prime_id("1,2")
id8 = pedil.get_or_create_prime_id("2,1")
id9 = pedil.get_or_create_prime_id("2,2")
id10 = pedil.get_or_create_prime_id("3,3")

# Print the generated IDs
print(f"{id1}")
print(f"{id2}")
print(f"{id3}")
print(f"{id4}")
print(f"{id5}")

print(f"{id6}")
print(f"{id7}")
print(f"{id8}")
print(f"{id9}")
print(f"{id10}")
