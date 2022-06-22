'''В шести примерах ниже комментарии на мой взгляд уместны. Объясняют назначение методов'''

class Data_Preprocess:
    '''Класс предобработки данных'''
    def __init__(self, df, text_rows, category_rows, dell_rows):
        self.df = df
        self.text_rows = text_rows
        self.category_rows = category_rows
        self.dell_rows = dell_rows
        self.new_name = None # ПРИМЕР: локальная Переменная инициирована внутри класса, используется в разных методах для трансформации датафрейма
    
    def lemmatize(self, doc):
        '''Лемматизация, получим нормальную (начальную) форму слова'''
        #doc - это содержимое в каждой ячейке, предложение, которое нужно изменить
        doc = re.sub(patterns, ' ', str(doc)) #?
        tokens = [] # ПРИМЕР: переменная инициируется непосредственно перед исполнением кода только в данном методе
        for token in doc.split():
            if token and token not in stopwords_ru:
                token = token.strip()
                token = morph.normal_forms(token)[0]
                tokens.append(token)
        return tokens
    
    def vector_row_1(self, row_name):
        '''Метод получения данных для векторизации текстового поля'''
        self.df[row_name] = self.df[row_name].fillna('пусто') 
        return self.df
    
    def vector_row_2(self, row_name):
        '''Получим токены текстового поля'''
        self.new_name = row_name + '_vec'
        self.df[self.new_name] = self.df.apply\
            (lambda row: tokenizer.tokenize\
            (row[row_name].lower()), axis = 1)
        return self.df
    
    def vector_row_3(self, row_name):
        '''Лемматизация, получим нормальную (начальную) форму слова 
        (именительный падеж)'''
        self.df[self.new_name] = self.df[self.new_name].apply(self.lemmatize)
        return self.df
    
    def vector_row_4(self, row_name):
        '''Убираем стоп-слова'''
        self.df[self.new_name] = self.df.apply(lambda row: \
            [word for word in row[self.new_name] if word \
            not in stopWords_ru], axis = 1)
        return self.df

'''В приведенных ниже примерах комментарии отсутствуют, т.к. наименование переменных достаточно понятное'''
import pandas as pd
df = pd.read_csv('music_log_upd.csv')
print(df.columns)
pop_music = df[df['genre_name'] == 'pop']
pop_music = pop_music[pop_music['total_play_seconds'] > 0]
print(pop_music)
pop_music_max_total_play = pop_music['total_play_seconds'].max()
print(pop_music_max_total_play)
pop_music_max_info = pop_music[pop_music['total_play_seconds'] == pop_music_max_total_play]
print(pop_music_max_info )
pop_music_min_total_play = pop_music['total_play_seconds'].min()
print(pop_music_min_total_play)
pop_music_min_info  = pop_music[pop_music['total_play_seconds'] == pop_music_min_total_play]
print(pop_music_min_info)
pop_music_median = pop_music['total_play_seconds'].median()
print(pop_music_median)
pop_music_mean = pop_music['total_play_seconds'].mean()
print(pop_music_mean )
