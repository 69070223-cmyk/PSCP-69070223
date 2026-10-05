"""BIGframe"""
text = []
for _ in range(5):
    text.append(input().strip())
long = max(text, key=len)

print(f"**{"*"*len(long)}**")
for t in text:
    print("* " + t.ljust(len(long)) + " *")
print(f"**{"*"*len(long)}**")
