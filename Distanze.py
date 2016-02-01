import math
import itertools

xcentro = 41.891969
ycentro = 12.495644
longitudini = [41.914456, 41.990672, 41.793883, 41.812566, 41.956277]
latitudini = [12.615807, 12.502714, 12.511297, 12.396628, 12.384611]
distanza = []

for (x,y) in zip(longitudini,latitudini):
    raggio = math.sqrt((xcentro-x)**2+(ycentro-y)**2)
    distanza.append(raggio)

media = 0
for i in distanza:
	media += i
media /= len(distanza)

print media 

def distanza(x, y)
    d = math.sqrt((x-xcentro)**2+(y-ycentro)**2)
    return d

map(distanza, x, y)

filter(d < raggio, x, y)

