import random
import time

lvl=int(1)      #Aqui fica o Level do cenario
id=int(0)       #Aqui é a quantidade de Inimigos Derrotados
up=[3,6,9,12,15,18,21,24,27,30]     #Aqui fica a marcação de quando deve aumentar o Level

jogador = {#Status do jogador
    'vida':50,
    'ataque':10,
    'defesa':10
}

inimigo ={      #Status do inimigo
    'vida':50,
    'ataque':10,
    'defesa':10
}


inimigo['vida']=inimigo['vida']+random.randint(-5,5)  #Randomizar os status do inimigo
inimigo['ataque']=inimigo['ataque']+random.randint(-5,5)
inimigo['defesa']=inimigo['defesa']+random.randint(-5,5)

print('Jogador:')                                     #Mostrar ao usuário os status dos combatentes
print(f'HP:{jogador['vida']} Ataque:{jogador['ataque']} Defesa:{jogador['defesa']}')
print(f'Level: {lvl}')
print('Inimigo a vista')
print('Inimigo:')
print(f'HP:{inimigo['vida']} Ataque:{inimigo['ataque']} Defesa:{inimigo['defesa']}')

while jogador['vida'] >= 1:

    decisao = input('Atacar ou Fugir? a/f:')            #Escolha do usuário

    if decisao == 'a' and inimigo['vida']>=1:           #Decisão de combate
        while inimigo['vida']>=1:                       #Ataque
            vj=int(jogador['vida'])                     #Esquema de vida e dano para os combatentes
            dj= max(random.randint (1,3), int(jogador['ataque']) - int(inimigo['defesa']))

            vi=int(inimigo['vida'])
            di= max(random.randint (1,3), int(inimigo['ataque']) - int(jogador['defesa']))

            print(f'Dano causado: {vi}-{dj}={vi - dj}\n')#Quantidade de dano  
            time.sleep(1)
            inimigo['vida'] = vi - dj
            print(f'Dano recebido: {vj}-{di}={vj - di}\n')
            time.sleep(1)
            jogador['vida'] = vj - di
            time.sleep(0.3)
        else:
            print('Golpe de misericordia')
            decisao

    elif decisao == 'a' and lvl == 10:                  #Vitória
        print('Vitoria')
        break

    elif decisao == 'f':                               #Decisão de fuga
        print('fuga')
        inimigo['vida']=50+random.randint(-5,5)        #Criar novo inimigo pós fuga
        inimigo['ataque']=10+random.randint(-5,5)
        inimigo['defesa']=10+random.randint(-5,5)
        print('.')
        time.sleep(0.3)
        print('..')
        time.sleep(0.3)
        print('...')
        time.sleep(0.3)
        print('Novo Inimigo')
        time.sleep(1)
        print('Jogador:')
        print(f'HP:{jogador['vida']} Ataque:{jogador['ataque']} Defesa:{jogador['defesa']}')#Mostrar novas informações para usuário
        print(f'Level: {lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']} Ataque:{inimigo['ataque']} Defesa:{inimigo['defesa']}')

    elif inimigo['vida']<=0 and id in up:               #Derrota do inimigo e upar
        print('Inimigo Derrotado')
        inimigo['vida']=50+(10*lvl)+random.randint(-5,5)         #Criar novo inimigo pós vitória
        inimigo['ataque']=10+(2*lvl)+random.randint(-5,5)
        inimigo['defesa']=10+(2*lvl)+random.randint(-5,5)
        jogador['vida']=50+(10*lvl)                     #Recuperar toda vida e upar de level
        jogador['ataque']=10000+(2*lvl)
        jogador['defesa']=10+(2*lvl)
        id=id+1                                         #Aumenta a quantidade de Inimigo Derrotado
        lvl=lvl+1                                       #Aumentar o level
        print('.')
        time.sleep(0.3)
        print('..')
        time.sleep(0.3)
        print('...')
        time.sleep(0.3)
        print('Novo Inimigo')
        print('Jogador:')
        print(f'HP:{jogador['vida']} Ataque:{jogador['ataque']} Defesa:{jogador['defesa']}')#Mostrar novas informações para usuário
        print(f'Level: {lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']} Ataque:{inimigo['ataque']} Defesa:{inimigo['defesa']}')

    elif inimigo['vida']<=0 and id not in up:           #Derrota do inimigo sem upar
        print('Inimigo Derrotado')
        inimigo['vida']=50+random.randint(-5,5)         #Criar novo inimigo pós vitória
        inimigo['ataque']=10+random.randint(-5,5)
        inimigo['defesa']=10+random.randint(-5,5)
        jogador['vida']=jogador['vida']+15              #Recuperar 15 de vida pós vitória
        id=id+1                                         #Aumenta a quantidade de Inimigo Derrotado
        print('.')
        time.sleep(0.3)
        print('..')
        time.sleep(0.3)
        print('...')
        time.sleep(0.3)
        print('Novo Inimigo')
        print('Jogador:')
        print(f'HP:{jogador['vida']} Ataque:{jogador['ataque']} Defesa:{jogador['defesa']}')#Mostrar novas informações para usuário
        print(f'Level: {lvl}')
        print('Inimigo:')
        print(f'HP:{inimigo['vida']} Ataque:{inimigo['ataque']} Defesa:{inimigo['defesa']}')


print('Game Ovo')                                       #Fim