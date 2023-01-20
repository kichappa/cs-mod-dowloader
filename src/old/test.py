import struct

# Open the file in binary mode
with open(r"C:\Users\kicha\AppData\Local\Colossal Order\Cities_Skylines\userGameState.cgs", "rb") as file:
    # Read the binary data
    data = file.read()

print("'{}'".format(data))

print("\n\n\n")

# Use the struct.unpack function to parse the binary data
# The format string "f" stands for a single float value
value = struct.unpack("f", data[:4])[0]

print(value)