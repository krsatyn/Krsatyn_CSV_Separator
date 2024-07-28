<img src="src\img\title_1.png">

# Krsatyn_CSV_Separator


Rus:
Модуль для быстрого создания датасета из одного CSV файла, с возможностью перевода набора данных на Русский\
[Инструкция на русском](readme_ru.md#sub-section)   

Eng:
A module for quickly creating a dataset from a single CSV file, with the ability to translate a dataset into Russian



<!--Установка-->
## Installation (Windows)

1. Cloning a repository

    >```git clone https://github.com/krsatyn/Krsatyn_CSV_Separator.git```

2. Going to the directory _Krsatyn_CSV_Separator_

    >```cd Krsatyn_CSV_Separator```

3. Creating a virtual environment

    >```python3 -m venv .venv```

4. Activating the virtual environment

    >```.venv/Scripts/activate```

5. Update pip

    >```.venv\scripts\python.exe -m pip install --upgrade pip```

6. Installing dependencies

    >```pip3 install -r requirements.txt```

7. Import class _CsvDatasetSeparator_

    >```from Krsatyn_CSV_Separator.main import CsvDatasetSeparator```

8. Create an instance _CsvDatasetSeparator_ and pass all the necessary values
    
    >cds = CsvDatasetSeparator(csv_path=csv_path,\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; csv_column=['column_name_1', 'column_name_2', 'column_name_n']\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; eat_column_name='column_name',\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; label_column_name='column_name',\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; translate_column_names=['column_name'],\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; dataset_name='dataset_name',\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; save_csv=True,\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; get_info=True,\
    >                          &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; check_input=True\
    >                          )

9. Call the main() method

    >```cds.main()```

<!--Пользовательская документация-->
## Documentation

Пользовательскую документацию на Русском можно получить по [этой ссылке](./docs/ru/index.md).

User documentation in English can be obtained from [this link](./docs/en/index.md).


<!--Поддержка-->
## Support
If you have any difficulties or questions about using the package, please email <kekwa2003@gmail.com >.