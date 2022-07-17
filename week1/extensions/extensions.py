# Author kflood
# Prints the http header for the extension of the given filename

filename = input("Filename: ").strip().lower()

if filename.endswith(".gif"):
    print("image/gif")
elif filename.endswith(".jpeg") or filename.endswith(".jpg"):
    print("image/jpeg")
elif filename.endswith(".png"):
    print("image/png")
elif filename.endswith(".pdf"):
    print("application/pdf")
elif filename.endswith(".txt"):
    print("text/plain")
elif filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")




