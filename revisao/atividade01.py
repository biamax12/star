for i in range (5,0,-1):
    print('rodada',i)
print('começou')
 
def ganhou_partida(pontos):
    if pontos>=500:
        return True
    else:
        return False
    
p= int(input('sua pontuação: '))
while ganhou_partida(p):
    print('você ganhou')
else:
    print('continue')
    