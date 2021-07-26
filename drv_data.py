

d = []
with open("drive-data", 'rb') as f:
	d = list(f.read())


d = [0xff for _ in range(0x2000)] + d


with open("Nov91.srm", 'wb') as f:
	f.write(bytes(d))