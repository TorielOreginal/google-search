import webbrowser

search = input("Input your search: ")
print("Redirecting to search " + search)
webbrowser.open("www.google.com/search?q=" + search)
