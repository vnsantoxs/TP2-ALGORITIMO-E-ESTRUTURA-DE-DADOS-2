import csl as modelers

while True:
    print('<>'*5+' MENU '+'<>'*5)
    modelers.optionmains()
    print('<>' * 13)
    opmain = int(input('Opção: '))
    modelers.options_menu(opmain)
