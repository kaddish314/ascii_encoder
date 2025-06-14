import itertools

flag = input("flag: ")

def text_to_fixed_binres(s: str, total_bits: int) -> str:
   b = s.encode("ascii")
   bitstr = "".join(f"{byte:08b}" for byte in b)
   if len(bitstr) < total_bits:
       bitstr = bitstr.rjust(total_bits, "0")
   else:
       bitstr = bitstr[-total_bits:]
   return bitstr

binres = "".join(f"{b:08b}" for b in flag.encode("ascii"))

def forward_bit(a, b, c, d):
   return (a and b) or (c and d)

print("\nreconstructed inputs:")
for idx, ch in enumerate(binres):
   desired = int(ch)
   for combo in itertools.product((0, 1), repeat=4):
       if forward_bit(*combo) == desired:
           string = (f"{','.join(str(bit) for bit in combo)}")
           print(f"{desired} -> {string}")
           break

print("\nbit stream:", binres)
