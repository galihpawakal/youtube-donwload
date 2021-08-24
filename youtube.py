import pafy

data = input("link: ")
url = pafy.new(data)
print(url.title)

hasil = url.getbest()
hasil.download()