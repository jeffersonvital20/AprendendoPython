x = input('Digite o primeiro valor')
y = input('Digite o segundo valor')
if x.isnumeric()& y.isnumeric():
    x = int(x)
    y = int(y)
    print('a soma dos numeros digitados é {} e eles são numericos? {}'.format(x+y, True))
else:
    print('O primeiro valor é numerico? {}, é uma letra(s)? {}, é alpha numerico? {}'.format(x.isnumeric(), x.isalpha(), x.isalnum()))
    print('O segundo valor é numerico? {}, é uma letra(s)? {}, é alpha numerico? {}'.format(y.isnumeric(), y.isalpha(), y.isalnum()))
