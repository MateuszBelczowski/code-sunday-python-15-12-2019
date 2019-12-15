stan_konta = 100
wyplata = 152
debet = 50

if wyplata < stan_konta:
    print("Możesz wypłacić")
elif wyplata < stan_konta + debet:
    print("Mozesz wyplacic, ale bedziesz na minusie")
else:
    print("Masz za malo pieniedzy")
