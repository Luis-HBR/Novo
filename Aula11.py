import random
import time

lvl=int(1)
id=int(0)

jogador = {
    'vida':50*lvl,
    'ataque':10*lvl,
    'defesa':10*lvl
}

inimigo ={
    'vida':50*lvl,
    'ataque':10*lvl,
    'defesa':10*lvl
}


inimigo['vida']=inimigo['vida']+random.randint(-5,5)
inimigo['ataque']=inimigo['ataque']+random.randint(-5,5)
inimigo['defesa']=inimigo['defesa']+random.randint(-5,5)

print('Jogador:')
print(f'HP:{jogador['vida']}')
print(f'Ataque:{jogador['ataque']}')
print(f'Defesa:{jogador['defesa']}')
print('Inimigo:')
print(f'HP:{inimigo['vida']}')
print(f'Ataque:{inimigo['ataque']}')
print(f'Defesa:{inimigo['defesa']}')


while jogador['vida'] >= 1:
    vj=int(jogador['vida'])
    dj= max(1, int(jogador['ataque']) - int(inimigo['defesa']))

    vi=int(inimigo['vida'])
    di= max(1, int(inimigo['ataque']) - int(jogador['defesa']))

    print('Inimigo a vista')

    decisao = input('Atacar ou Fugir? a/f:')
    if decisao == 'a' and inimigo['vida']>=1:
        inimigo['vida'] = vi - dj
        jogador['vida'] = vj - di
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')
    elif decisao == 'f':
        print('fuga')
        inimigo['vida']=50+random.randint(-5,5)
        inimigo['ataque']=10+random.randint(-5,5)
        inimigo['defesa']=10+random.randint(-5,5)
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')
    elif inimigo['vida']<=0:
        print('Inimigo Derrotado')
        inimigo['vida']=50+random.randint(-5,5)
        inimigo['ataque']=10+random.randint(-5,5)
        inimigo['defesa']=10+random.randint(-5,5)
        jogador['vida']=jogador['vida']+15
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')

print('Game Ovo')