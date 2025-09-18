dimensions = (200,50, 300)
count = 0
for dimension in dimensions:
    print(f"dimension: {dimensions[count]}")
    count += 1

original_dimensions = (200,50)
print("Original dimensions:")
for dimension in original_dimensions:
    print(dimension)

original_dimensions = (400, 100)
print("Modified dimensions:")
for dimension in original_dimensions:
    print(dimension)