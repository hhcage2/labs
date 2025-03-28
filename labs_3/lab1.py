# TODO Напишите функцию для поиска индекса товара
def foo(list_, item):
    return list_.index(item) # еще можно добавить проверки по типу если item'а нету
    # в списке то вернуть valueerror


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']


for find_item in ['банан', 'груша', 'персик']:
    index_item = foo(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
