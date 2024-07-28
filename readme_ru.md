<!-- <img src="\img\title_1.png"> -->

[Назад](README.md)   
# Krsatyn_CSV_Separator



Some content

Rus:
Модуль для быстрого создания датасета из одного CSV файла, с возможностью перевода набора данных на Русский




<!--Установка-->
## Установка (Windos)

1. Клонирование репозитория 

    >```git clone https://github.com/krsatyn/Krsatyn_CSV_Separator.git```

2. Переход в директорию Krsatyn_CSV_Separator

    >```cd Krsatyn_CSV_Separator```

3. Создание виртуального окружения

    >```python3 -m venv .venv```

4. Активация виртуального окружения

    >```.venv/Scripts/activate```

5. Обновите pip

    >```.venv\scripts\python.exe -m pip install --upgrade pip```

6. Установка зависимостей

    >```pip3 install -r requirements.txt```

7. Импортируйте класс _CsvDatasetSeparator_

    >```from Krsatyn_CSV_Separator.main import CsvDatasetSeparator```

8. Создайте экземпляр _CsvDatasetSeparator_ и передайте все нужные значения
    ```python
    cds = CsvDatasetSeparator(csv_path=csv_path,\
                              csv_column=['column_name_1', 'column_name_2', 'column_name_n']
                              eat_column_name='eat_column_name',
                              label_column_name='label_column_name',
                              translate_column_names=[' translate_column_name'],
                              dataset_name='dataset_name',
                              save_csv=True,
                              get_info=True,
                              check_input=True
                              )
    ```

9. Вызовите метод main()

    >```cds.main()```

<!--Пользовательская документация-->
## Документация

Пользовательскую документацию на Русском можно получить по [этой ссылке](./src/docs/ru/index.md).


<!--Поддержка-->
## Поддержка
Если у вас возникли сложности или вопросы по использованию пакета, напишите на электронную почту <kekwa2003@gmail.com>.
