available_toppings = ['蘑菇', '橄榄', '青椒', '菠萝', '额外芝士']#可选
requested_toppings = ['蘑菇','薯条', '额外芝士']#顾客点餐

for i in available_toppings:
    if i in requested_toppings:
        print('您点了' + requested_toppings + '.')
    else:
        print('抱歉，我们没有' + requested_toppings + '.')
        
print('\n披萨制作结束')
