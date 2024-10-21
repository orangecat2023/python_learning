s = float(input())
if s < 1000:
    tax_paid = s
    print('%.2f'% s)
elif 1000 <= s < 2000:
    tax_paid = 0.9*s
    print('%.2f'% tax_paid)
elif 2000 <= s < 3000:
    tax_paid = 0.85*s
    print('%.2f'% tax_paid)
elif 3000 <= s < 4000:
    tax_paid = 0.8*s
    print('%.2f'% tax_paid)
elif 4000 <= s:
    tax_paid = 0.75*s
    print('%.2f'% tax_paid)