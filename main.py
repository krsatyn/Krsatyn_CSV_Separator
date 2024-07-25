import pandas
import os

from sklearn.model_selection import train_test_split
from translatepy import Translator
from tqdm import tqdm



tqdm.pandas()

# Получение информации о Фрейме 
def dataframe_info(data_frame:pandas.core.frame.DataFrame) -> None:

    print('--->Информация по DF<---\n')
    print(f'>shape:\n{data_frame.shape}\n')
    print(f'>columns:\n{data_frame.columns}\n')
    print(f'>index:\n{data_frame.index}\n')
    print(f'>dtypes:\n{data_frame.dtypes}\n')
    
    print('Первые 3:\n', data_frame[0:3])

def create_dataset_dir(dataset_name:str="dataset_folder") -> None:
    
    if not os.path.isdir(dataset_name):
        os.mkdir(dataset_name)
        os.chdir(dataset_name)
        
        if not os.path.isdir('train'):
            os.mkdir('train')
        
        if not os.path.isdir('test'):
            os.mkdir('test')
        
        if not os.path.isdir('valid'):
            os.mkdir('valid')
    
    else:
        print("Данная папка уже существует")
            
def save_dataset(dataset_name:str="dataset_folder", dataset_dict:dict=None) -> None:
    
    create_dataset_dir(dataset_name=dataset_name)
    
    try:
        dataset_dict['train'][0].to_csv(r'train\train_set.csv', header=False, index=False)
        dataset_dict['train'][1].to_csv(r'train\train_label.csv', header=False, index=False)

        dataset_dict['test'][0].to_csv(r'test\test_set.csv', header=False, index=False)
        dataset_dict['test'][1].to_csv(r'test\test_label.csv', header=False, index=False)

        dataset_dict['valid'][0].to_csv(r'valid\valid_set.csv', header=False, index=False)
        dataset_dict['valid'][1].to_csv(r'valid\valid_label.csv', header=False, index=False)
        
        print(f"Сохранено в {os.getcwd()}\{dataset_name}")
        
        
    except OSError:
        print("!Ошибка сохранения!\nПроверьте нет ли папки с таким же именем и проверьте пуста ли она.")
        

    
 
    


# Перевод данных
def translate_dataset(data_frame:pandas.core.frame.DataFrame, column_name:str) -> pandas.core.frame.DataFrame:
    translator = Translator()
    print(f"Перевод: {column_name}")
    
    data_frame[column_name] = data_frame[column_name].progress_apply(lambda x: translator.translate(str(x), destination_language='Russian'))
      
    return data_frame
    
    
# Получение датасета
def get_dataset(csv_path:str,
                csv_column:list,
                eat_column_name:str,
                label_column_name:str,
                get_info:bool=False,
                save_csv:bool=False,
                dataset_name:str='dataset_folder',
                translate_column_names:list=None
                ) -> dict:
    
    data_frame = pandas.read_csv(csv_path, delimiter=',')
    data_frame.columns = csv_column
    
    data_frame = data_frame[:11]
    
    if translate_column_names is not None:
        for translate_column_name in translate_column_names:
            data_frame = translate_dataset(data_frame=data_frame, column_name=translate_column_name)
    
    if get_info == True:
        dataframe_info(data_frame)

    eat = data_frame[eat_column_name]
    label = data_frame[label_column_name]

    # 60 20 20
    train_set, test_set, train_label, test_label = train_test_split(eat, label, test_size=0.4, random_state=42)
    test_set, valid_set, test_label, valid_label = train_test_split(test_set, test_label, test_size=0.5, random_state=42)
    
    dataset_dict = {"train":[train_set, train_label],
                    "test":[test_set, test_label],
                    "valid":[valid_set, valid_label]}
    
    if save_csv == True:
        save_dataset(dataset_name=dataset_name, dataset_dict=dataset_dict)
    
    return dataset_dict



# main
if __name__ == '__main__':
    
    dataset = get_dataset(csv_path='twitter_training.csv',
                          csv_column=['source_id', 'source', 'mood', 'context'],
                          eat_column_name='context',
                          label_column_name='mood',
                          translate_column_names=['mood','context'],
                          #dataset_name='KEKWA',
                          save_csv=True,)
    
    #print('\n\n',len(dataset['train'][0]), 
    #      len(dataset['test'][0]), 
    #      len(dataset['valid'][0]))