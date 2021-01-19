import os

def read(f):
	with open(f, "r", encoding = "utf16") as file:
		l=file.read()
	return l
	
def write(c):
	with open("res.txt", "w", encoding = "utf8") as file:
		file.write(c)
	

def main():
	liste=os.listdir("notes")
	chain=""
	for i in liste:
		l = read("notes/" + i)
		#print(l)
		chain += l
		chain += "\n\n\n"
	write(chain)

def test():
	liste=os.listdir("notes")
	chain=""
	l=read("test.txt")
	print(l)


main()