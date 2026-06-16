# rb ==> read binary
# wb ==> write binary

# Copy

with open("img.png", "rb") as source:
    data = source.read()


with open("copy.png", "wb") as target:
    target.write(data)