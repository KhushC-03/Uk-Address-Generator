# Uk Address Generator
import requests, os
def addygen():
    os.system('cls')
    amount = input('\x1b[1;37mHow Many Addresses Would You Link To Generate\x1b[1;36m:\x1b[1;37m ')
    print("""            AL B BA BB BD BH BL BN BR BS CA CB CF CH CM CO CR CT CV CW D
            A DE DH DL DN DT DY E EC EN EX FY GL GU HA HD HG HP HR HU HX
            IG IP KT L LA LD LE LL LN LS LU M ME MK N NE NG NN NP NR NW OL 
            OX PE PL PO PR RG RH RM S SA SE SG SK SL SM SN SO SP SR SS ST 
            SW SY TA TF TN TQ TR TS TW UB W WA WC WD WF WN WR WS WV YO""")
    postcode = input('\x1b[1;37mPost Code Prefix \x1b[1;36m:\x1b[1;37m ')
    headers = {
        'authority': 'www.doogal.co.uk',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51',
        'referer': 'https://www.doogal.co.uk/RandomAddresses.php'
    }
    params = {
        'startWith': postcode
    }
    for i in range(int(amount)):
        r = requests.get('https://www.doogal.co.uk/CreateRandomAddress.ashx', headers=headers, params=params)
        adddress = r.text
        addy = adddress.split(',')
        a = addy[0].split(',')[-1]
        b = addy[1].split(',')[-1]
        c = addy[2].split(',')[-1]
        d = addy[3].split(',')[-1]
        mainaddress = ('{} {} {} {} \n').format(a,b,c,d)
        mainaddress1 = ('{} {} {} {}').format(a,b,c,d)
        addys = open('C:\\Users\\Khush Chauhan\\Desktop\\SNS SCRIPT\\addesses.txt','a')
        addys.write(str(mainaddress))
        print(mainaddress1)
    addys.close()
addygen()