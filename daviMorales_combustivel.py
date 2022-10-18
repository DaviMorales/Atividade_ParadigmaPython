import sys 

etanol = float(sys.argv[1])
gasolina = float(sys.argv[2])

if etanol / gasolina <= 0.7 :
    print('Vale mais a pena o etanol!')
else :
    print('Vale mais a pena a gasolina!')
