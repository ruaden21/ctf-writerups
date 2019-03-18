e = '[OIonU2_<__nK<KsK'

k = 72

for i in range(0,len(e)-1):
    for u in range(32,127):
        temp = (((u + 12) * k + 17) % 70) + 48
        if(temp == ord(e[i])):
            print(chr(u))
    k = ord(e[i])
    print('-------------')
    
#G4Z2S79570095926