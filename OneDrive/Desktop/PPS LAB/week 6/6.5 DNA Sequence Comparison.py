
s1 = input("Enter first DNA sequence: ")
s2 = input("Enter second DNA sequence: ")

dna = {'A', 'T', 'C', 'G'}
a = set(s1)
b = set(s2)

c = a.intersection(b)   # common nucleotides
u1 = a.difference(b)    # unique to first sequence
u2 = b.difference(a)    # unique to second sequence
m1 = dna.difference(a)  # missing from first sequence
m2 = dna.difference(b)  # missing from second sequence

print("Common nucleotides:", c)
print("Unique to first sequence:", u1)
print("Unique to second sequence:", u2)
print("Missing from first sequence:", m1)
print("Missing from second sequence:", m2)
