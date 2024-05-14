# PEDIL

PEDIL (Prime Extended Decimal Index Listing) is a Python package designed for generating unique IDs using prime numbers. It leverages an innovative indexing method that uses prime numbers to uniquely identify software components.

## Features

- **Unique ID Generation**: Generate unique IDs using prime numbers.
- **Scalable**: Supports multiple levels of depth for ID generation, offering a vast number of unique identifiers.
- **Efficient**: Optimized for performance with manageable chunk sizes for prime generation.

## Installation

You can install the package using pip:

```sh
pip install pedil
```

Usage

Here is a simple example demonstrating how to use PEDIL to generate unique IDs.

```python

from pedil import PEDIL

# Create an instance of the PEDIL class
pedil = PEDIL()

# Generate unique IDs
id1 = pedil.get_or_create_prime_id("1")
id2 = pedil.get_or_create_prime_id("1,1")
id3 = pedil.get_or_create_prime_id("2,3,5")

# Print the generated IDs
print(f"ID for '1': {id1}")
print(f"ID for '1,1': {id2}")
print(f"ID for '2,3,5': {id3}")
```

![example](1.png)

Prime Extended Decimal Index Listing (PEDIL)
Annotation System

The PEDIL notation uses commas to separate different levels. Each level represents a multiplier for the corresponding power of the base array size. The notation allows for scalable and flexible ID generation.

For example, consider the notation (1,3,5) with a base array size of N primes:

    1 * N^2
    3 * N^1
    5 * N^0

The final prime index is the sum of these values.
Example Notations

    Single Level: "1" -> Represents the 1st prime.
    Two Levels: "1,1" -> Represents the sum of 1 * N^1 + 1 * N^0.
    Three Levels: "2,3,5" -> Represents the sum of 2 * N^2 + 3 * N^1 + 5 * N^0.

Maximum Unique IDs
Using the First 78,498 Primes (Primes up to 1 Million)

    1 Level of Depth: 78,498 unique IDs
    2 Levels of Depth: 78,498^2 = 6,161,251,004 unique IDs
    3 Levels of Depth: 78,498^3 = 4,847,646,381,177,992 unique IDs

Performance Considerations

    1 Level of Depth: Suitable for most applications, providing a large number of unique IDs efficiently.
    2 Levels of Depth: Suitable for applications requiring even more unique IDs, with manageable computational overhead.
    3 Levels of Depth: Provides an enormous number of unique IDs but may involve significant computational time and resources.

Applications and Use Cases
Practical Use

For most real-world applications, using 1 or 2 levels of PEDIL notation should be sufficient to provide a vast number of unique IDs efficiently without excessive computational overhead.
Big Data and Machine Learning

For applications like big data and machine learning, where handling trillions of tokens and long processing times are common, PEDIL can scale to higher levels and larger base arrays, offering unique IDs in the trillions.
License

This project is licensed under the MIT License.