import requests 

def main():
    
    resp = 0
    
    comeco_ = (input('Pressione [1] para iniciar o teste \nPressione [2] para sair\n'))
    if comeco_ == '1':
        print('\n INICIANDO... \n')
    else:
        print('Obrigado por utilizar! \nSaindo...')
        return
        exit()

    nome = input('Por favor informe seu nome: ')
    cep_input = input('\nDigite seu CEP com 8 digitos, somente números para consulta: \n')
    print()

    if len(cep_input) != 8:
        print('Quantidade de dígitos inválida, por favor informe 8 digitos!')
        main()

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    enderecodata = request.json()

    while 'erro' in enderecodata:
        print('CEP não localizado, por favor digite corretamente!')
        print('Saindo...')
        exit()

    print('''
                Seja bem-vindo ao teste digital de Coronavirus. 
            Responda algumas perguntas para analisarmos seu caso!
            ''')

    print('\n{}, vamos iniciar seu teste:\n'.format(nome))

    #QUESTAO1
    q1 = '0'
    while q1 == '0':        
        q1 = input('Você teve algum sintoma de febre nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n')
        if q1 == '1':
            resp = 1
            q1 = '99'
            print('Você respondeu SIM')
        elif q1 == '2':
            resp = resp   
            print('Você respondeu NAO')
            q1 = '99'
        else:
            print('Reposta invalida')
            q1 = '0'  

    #QUESTAO2
    q2 = '0'
    while q2 == '0':  
        q2 = input('\n{}, você se sentiu fadigado nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n'.format(nome))
        if q2 == '1':
            print('Você respondeu SIM')
            q2 = '99'
            resp+=1
        elif q2 == '2':
            print('Você respondeu NAO')
            q2 = '99'
            resp = resp
        else:
            print('Digite um valor correto: ')
            q2 = '0'

    #QUESTAO3
    q3 = '0'
    while q3 == '0': 
        q3 = input('\nVocê sentiu dores de garganta nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n')         
        if q3 == '1':
            print('Você respondeu SIM')
            q3 = '99'
            resp+=1
        elif q3 == '2':
            print('Você respondeu NAO')
            q3 = '99'
            resp = resp
        else:
            print('Digite um valor correto')
            q3 = '0'

    #QUESTAO4
    q4 = '0'
    while q4 =='0':  
        q4 = input('\n{}, você teve tosses constantes nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n'.format(nome))
        if q4 == '1':
            print('Você respondeu SIM')
            q4 = '99'
            resp+=1
        elif q4 == '2':
            resp = resp
            print('Você respondeu NAO')
            q4 = '99'
        else:
            print('Digite um valor correto')
            q4 = '0'

    #QUESTAO5
    q5 = '0'
    while q5 == '0':   
        q5 = input('\nVocê sentiu fortes dores de cabeça nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n')
        if q5 == '1':
            print('Você respondeu SIM')
            q5 = '99'
            resp+=1
        elif q5 == '2':
            print('Você respondeu NAO')
            q5 = '99'
            resp = resp
        else:
            print('Digite um valor correto')
            q5 = '0'

    #QUESTAO6
    q6 = '0'
    while q6 == '0':
        q6 = input('\n{}, e você sentiu falta de ar nos últimos dias? \n[1] SIM \n[2] NÃO \nRESPOSTA: \n'.format(nome))
        if q6 == '1':
            print('Você respondeu SIM')
            q6 = '99'
            resp+=1
        elif q6 == '2':
            print('Você respondeu NAO')
            q6 = '99'
            resp = resp
        else:
            print('Digite um valor correto')
            q6 = '0'

    if resp >= 5:
        print('\n{}, em uma escala de 1 a 6 você obteve {}. \nAconselhamos fortemente que procure um médico em {} e se mantenha isolado!\n'.format(nome, resp, enderecodata['localidade']))
    elif resp >= 2:
        print('\n{}, em uma escala de 1 a 6 você obteve {}. \nVocê pode estar gripado, porém caso aumentem seus sintomas procure a unidade de saúde mais próxima a {}!\n'.format(nome, resp, enderecodata['bairro']))
    elif resp >= 0:
        print('\n{}, em uma escala de 1 a 6 você obteve {}. você pode estar resfriado pois seus sintomas são poucos, mas mantenha o cuidado!\n'.format(nome, resp))

    print('Desenvolvido por Wellington Oliveira')

if __name__ == '__main__':
    main()