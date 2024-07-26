import pandas
import os

from sklearn.model_selection import train_test_split
from translatepy import Translator
from tqdm import tqdm


class CsvDatasetSeparator:
    
    def __init__(self, 
                csv_path:str,                          # Path to the file
                csv_column:list,                       # Column names
                eat_column_name:str,                   # Name of the column to feed
                label_column_name:str,                 # Name of the column to feed labels
                get_info:bool=False,                   # Marker for displaying information about the dataset
                save_csv:bool=False,                   # Marker for saving dataset in a folder
                dataset_name:str='dataset_folder',     # Name the folder to save the dataset
                translate_column_names:list=None,      # Marker and a column with the name for the translation
                check_input:bool=False                 # Marker for check input parameters info
                 ) -> None:
        
        self.csv_path = csv_path,
        self.csv_column = csv_column,
        self.eat_column_name = eat_column_name,
        self.label_column_name = label_column_name,
        self.get_info = get_info,
        self.save_csv = save_csv,
        self.dataset_name = dataset_name,
        self.translate_column_names = translate_column_names
        self.check_input = check_input
        
    """ Get the basic information dataset """
    def get_dataframe_info(self, data_frame:pandas.core.frame.DataFrame) -> None:
        
        print()
        print('--->DF information<---\n')
        print(f'>shape:\n{data_frame.shape}\n')
        print(f'>columns:\n{data_frame.columns}\n')
        print(f'>index:\n{data_frame.index}\n')
        print(f'>dtypes:\n{data_frame.dtypes}\n')
        print('Первые 3:\n', data_frame[0:3])
        print('-----------------------------\n')
    
    ''' Get dtype and value input params'''
    def get_input_parameter_info(self,) -> None:

                print('--->Input_parameter information<---\n')
                csv_path = self.csv_path[0]
                csv_column = self.csv_column[0]
                get_info = self.get_info[0]
                eat_column_name = self.eat_column_name[0]
                label_column_name = self.label_column_name[0]
                save_csv = self.save_csv[0]
                dataset_name = str(self.dataset_name[0])
                translate_column_names = self.translate_column_names

                data_frame = pandas.read_csv(csv_path, delimiter=',')
                data_frame.columns = csv_column
        
                print()
                print("csv_path: ", csv_path, "\n", type(csv_path), "\n")
                print("csv_column: ", csv_column, "\n", type(csv_column), "\n")
                print("get_info: ", get_info, "\n", type(get_info), "\n")
                print("eat_column_name: ", eat_column_name, "\n", type(eat_column_name), "\n")
                print("label_column_name: ", label_column_name, "\n", type(label_column_name), "\n")
                print("save_csv: ", save_csv, "\n", type(save_csv), "\n")
                print("dataset_name: ", dataset_name, "\n", type(dataset_name), "\n")
                print("translate_column_names: ", translate_column_names, "\n", type(translate_column_names), "\n")
                print()
                print('-----------------------------\n')
    
    """ Сreating a data set structure """
    def create_dataset_dir(self, dataset_name:str="dataset_folder") -> None:
        '''
        
        structure dataset: _
                           |
                           |->train_
                           |       |->train_labels.csv
                           |       |->train_set.csv
                           | 
                           |->test_ 
                           |      |->test_labels.csv 
                           |      |->test_set.csv
                           |         
                           |->valid_ 
                                   |->valid_labels.csv 
                                   |->valid_set.cs
        '''
        
        if not os.path.isdir(dataset_name):
            os.mkdir(dataset_name)
            os.chdir(dataset_name)

            if not os.path.isdir('train'):
                os.mkdir('train')

            if not os.path.isdir('test'):
                os.mkdir('test')

            if not os.path.isdir('valid'):
                os.mkdir('valid')
    
    """ Saving a dataset by the specified name"""
    def save_dataset(self, dataset_name:str="dataset_folder", dataset_dict:dict=None) -> None:
    
        '''
        !!!IT IS IMPORTANT TO OBSERVE THE INDEXES IN THE LIST:
                                                                [0] THE INDEX IS A SET OF DATA 
                                                                [1] THESE ARE LABELS
        
        dataset_dict structure:
        {"train":[train_set:pandas.core.frame.DataFrame,   
                  train_label:pandas.core.frame.DataFrame],
                  
         "test":[train_set:pandas.core.frame.DataFrame,   
                 train_label:pandas.core.frame.DataFrame],
                  
         "valid":[train_set:pandas.core.frame.DataFrame,   
                  train_label:pandas.core.frame.DataFrame],
        '''

        self.create_dataset_dir(dataset_name=dataset_name)

        try:
            dataset_dict['train'][0].to_csv(r'train\train_set.csv', header=False, index=False)
            dataset_dict['train'][1].to_csv(r'train\train_label.csv', header=False, index=False)

            dataset_dict['test'][0].to_csv(r'test\test_set.csv', header=False, index=False)
            dataset_dict['test'][1].to_csv(r'test\test_label.csv', header=False, index=False)

            dataset_dict['valid'][0].to_csv(r'valid\valid_set.csv', header=False, index=False)
            dataset_dict['valid'][1].to_csv(r'valid\valid_label.csv', header=False, index=False)

            print(f"\nСохранено в {os.getcwd()}\{dataset_name}")


        except OSError:
            print("!Ошибка сохранения!\nПроверьте нет ли папки с таким же именем и проверьте пуста ли она.")
    
    """ Translation of the data set by column into Russian """
    def translate_dataset(self, data_frame:pandas.core.frame.DataFrame, column_name:str) -> pandas.core.frame.DataFrame:
        
        tqdm.pandas() # initialization progressbar
        
        translator = Translator()
        
        print(f"Translate: >{column_name}< column")

        data_frame[column_name] = data_frame[column_name].progress_apply(lambda x: translator.translate(str(x), destination_language='Russian'))

        return data_frame
    
    """main function"""
    def main(self) -> dict:
        
        # main parameters (check __init__ to get more information)
        csv_path = self.csv_path[0]
        csv_column = self.csv_column[0]
        get_info = self.get_info[0]
        eat_column_name = self.eat_column_name[0]
        label_column_name = self.label_column_name[0]
        save_csv = self.save_csv[0]
        dataset_name = str(self.dataset_name[0])
        translate_column_names = self.translate_column_names
        check_input = self.check_input 
        
        if check_input:
            self.get_input_parameter_info()
                
        data_frame = pandas.read_csv(csv_path, delimiter=',')
        data_frame.columns = csv_column

        data_frame = data_frame

        # checking for translation of a dataset column 
        if translate_column_names is not None:
            for translate_column_name in translate_column_names:
                data_frame = self.translate_dataset(data_frame=data_frame, column_name=translate_column_name)
        
        # checking if additional information about the dataset is needed
        if get_info == True:
            self.get_dataframe_info(data_frame)

        eat = data_frame[eat_column_name]
        label = data_frame[label_column_name]

        """
        distribution of the dataset: 
                                     60% for the training set 
                                     20% for the test set 
                                     205 for the valid set
        """
        train_set, test_set, train_label, test_label = train_test_split(eat, label, test_size=0.4, random_state=42)
        test_set, valid_set, test_label, valid_label = train_test_split(test_set, test_label, test_size=0.5, random_state=42)

        dataset_dict = {"train":[train_set, train_label],
                        "test":[test_set, test_label],
                        "valid":[valid_set, valid_label]}

        
        
        # checking to save the dataset
        if save_csv == True:
            self.save_dataset(dataset_name=dataset_name, dataset_dict=dataset_dict)

        return dataset_dict


if __name__ == '__main__':
    
    csv_path = 'twitter_training.csv'
    
    cds = CsvDatasetSeparator(csv_path=csv_path,
                              csv_column=['source_id', 'source', 'mood', 'context'],
                              eat_column_name='context',
                              label_column_name='mood',
                              translate_column_names=['mood'],
                              dataset_name='KEKWA',
                              save_csv=True,
                              get_info=True,
                              check_input=True
                              )
    
    cds.main()
