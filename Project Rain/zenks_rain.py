#Zenks1 - 4intelligence :)
#Script pra realizar o teste de missing headers na URL informada
#A lista de headers a serem procurados poderá ser alterada a qualquer momento no código

#Script that validates the informed headers in a certain URL
#The header list searched by the lib, can be changed at any point in this code

import requests

url = str(input('[+] USAGE(HTTPS://YYY.XXX) URL: '))

def check_security_headers(url):
    check_following = [
        'Content-Security-Policy',
        'Strict-Transport-Security',
        'X-Frame-Options',
        'X-XSS-Protection',
        'X-Content-Type-Options',
        'Referrer-Policy',
        'Feature-Policy',
        'Set-Cookie',
        'Acess-Control-Allow-Origin',
        'Cross-Origin-Opener-Policy',
        'Cross-Origin-Embedder-Policy',
        'Cross-Origin-Resource-Policy',
        'X-DNS-Prefetch-Control',
        'Public-Key-Pins'
        #Adicione headers aqui // Add your custom headers here

        #Cada header tem um princípio diferente de funcionamento e configuração, mais informações a respeito dos mesmos, checar a url: 
        #Each header has it's own config and use, for more information about each header, please visit: 

        #https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
        
    ]
    response = requests.head(url)
    missing_headers = []
    
    for header in check_following:
        print('''                
██╗  ██╗██╗    ██╗███╗   ███╗    ███████╗███████╗███╗   ██╗██╗  ██╗███████╗    ██╗       
██║  ██║██║    ██║████╗ ████║    ╚══███╔╝██╔════╝████╗  ██║██║ ██╔╝██╔════╝    ██║       
███████║██║    ██║██╔████╔██║      ███╔╝ █████╗  ██╔██╗ ██║█████╔╝ ███████╗    ██║       
██╔══██║██║    ██║██║╚██╔╝██║     ███╔╝  ██╔══╝  ██║╚██╗██║██╔═██╗ ╚════██║    ╚═╝       
██║  ██║██║    ██║██║ ╚═╝ ██║    ███████╗███████╗██║ ╚████║██║  ██╗███████║    ██╗       
╚═╝  ╚═╝╚═╝    ╚═╝╚═╝     ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝    ╚═╝   ''')
        if header not in response.headers:
            missing_headers.append(header)

            if len(missing_headers) == 0:
                print(f'[+] {url} : all headers OK')
                #Headers OK!
            else:
                print(f'[-] {url} is missing or they may have a bad config: ')
                #Mostra a lista de headers faltando, quando houverem
                for header in missing_headers:
                    print(header)

check_security_headers(url)

print('#########################################################################################################################')

print('Please open a request on 4intelligence JIRA or e-mail r.paiva@4intelligence.ai to validate the headers config parameters')
