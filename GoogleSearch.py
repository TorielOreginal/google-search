import webbrowser

search = input("Digite a sua pesquisa: ")
print("Redirecionando para a pesquisa " + search)
webbrowser.open("www.google.com/search?q=" + search)
