#Импорт функций
from code.utils import Data, ReformattedData, main

#Путь к файлу с данными
PATH = 'data.json'

#Получение данных через присваивание класса
data = Data(PATH)
text = data.get_data()

#Реформатирование данных через присваивание класса
new_text = ReformattedData(text)
reformatted_text = new_text.reformat_data()

#Финальные данные для вывода
final_output = main(reformatted_text)[:5]

for operation in final_output:
    print(operation)
    print()
