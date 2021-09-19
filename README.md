# radix_string 
Function for python to convert integer to any base


## Installation
```bash
pip install 
```

## Usage
```python
from radix_string import radix_string

assert radix_string(10, 2) == bin(10)[2:]
x = 100500
base = 15

print(f"Integer {x}(10) in {base} base is {radix_string(x, base)}({base})")
```
