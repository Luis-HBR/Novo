import random
import time

lvl=int(0)
id=int(0)
up=[3,6,9,12,15,18,21,24,27,30]

jogador = {
    'vida':50,
    'ataque':10,
    'defesa':10,
    'lvl':lvl
}

inimigo ={
    'vida':50,
    'ataque':10,
    'defesa':10
}


inimigo['vida']=inimigo['vida']+random.randint(-5,5)
inimigo['ataque']=inimigo['ataque']+random.randint(-5,5)
inimigo['defesa']=inimigo['defesa']+random.randint(-5,5)

print('Jogador:')
print(f'HP:{jogador['vida']}')
print(f'Ataque:{jogador['ataque']}')
print(f'Defesa:{jogador['defesa']}')
print(f'Level:{lvl}')
print('Inimigo:')
print(f'HP:{inimigo['vida']}')
print(f'Ataque:{inimigo['ataque']}')
print(f'Defesa:{inimigo['defesa']}')


while jogador['vida'] >= 1:
    vj=int(jogador['vida'])
    dj= max(1, int(jogador['ataque']) - int(inimigo['defesa']))

    vi=int(inimigo['vida'])
    di= max(1, int(inimigo['ataque']) - int(jogador['defesa']))

    if id in up:
        lvl=lvl+1
        jogador['ataque']=jogador['ataque']+(2*lvl)
        jogador['defesa']=jogador['defesa']+(2*lvl)
        jogador['vida']=jogador['vida']+(10*lvl)

    print('Inimigo a vista')

    decisao = input('Atacar ou Fugir? a/f:')
    if decisao == 'a' and inimigo['vida']>=1:
        inimigo['vida'] = vi - dj
        jogador['vida'] = vj - di
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print(f'Level:{lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')
    elif decisao == 'f':
        print('fuga')
        inimigo['vida']=50+(10*lvl)+random.randint(-5,5)
        inimigo['ataque']=10+(2*lvl)+random.randint(-5,5)
        inimigo['defesa']=10+(2*lvl)+random.randint(-5,5)
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print(f'Level:{lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')
    elif inimigo['vida']<=1 and decisao == 'a':
        print('Inimigo Derrotado')
        id=id+1
        inimigo['vida']=50+(10*lvl)+random.randint(-5,5)
        inimigo['ataque']=10+(2*lvl)+random.randint(-5,5)
        inimigo['defesa']=10+(2*lvl)+random.randint(-5,5)
        jogador['vida']=jogador['vida']+15
        print('Jogador:')
        print(f'HP:{jogador['vida']}')
        print(f'Ataque:{jogador['ataque']}')
        print(f'Defesa:{jogador['defesa']}')
        print(f'Level:{lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']}')
        print(f'Ataque:{inimigo['ataque']}')
        print(f'Defesa:{inimigo['defesa']}')
    elif jogador['lvl']:
        print('Venceu')


print('Game Ovo')
