'''В данном примере обработки текстового датафрейма императивный подход заменен на ООП. 
В созданном классе используется 22 отдельных метода с минимальным функционалом'''

# Трансформация данных
class Data_Preprocess:
    '''Класс предобработки данных'''
    def __init__(self, df, text_rows, category_rows, dell_rows):
        self.df = df
        self.text_rows = text_rows
        self.category_rows = category_rows
        self.dell_rows = dell_rows
        self.new_name = None
    
    def lemmatize(self, doc):
        '''Лемматизация, получим нормальную (начальную) форму слова'''
        #doc - это содержимое в каждой ячейке, предложение, которое нужно изменить
        doc = re.sub(patterns, ' ', str(doc)) #?
        tokens = []
        for token in doc.split():
            if token and token not in stopwords_ru:
                token = token.strip()
                token = morph.normal_forms(token)[0]
                tokens.append(token)
        return tokens
    
    def vector_row_1(self, row_name):
        '''Метод получения данных для векторизации текстового поля'''
    
        '''Заполним пустые строки'''
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
    
    def vector_row_5(self, row_name):
        '''Обучение модели'''
        # зададим параметры модели
        w2v_model = Word2Vec(
            min_count=1, # 10 для полного поля, для реальной работы
            window=2,
            size=300,
            negative=10,
            alpha=0.03,
            min_alpha=0.0007,
            sample=6e-5,
            sg=1)

        # получить словарь
        w2v_model.build_vocab(self.df[self.new_name])
        # обучить модель, используя метод train
        w2v_model.train(self.df[self.new_name], total_examples = w2v_model.corpus_count,\
                        epochs=30, report_delay=1)

        '''переводим в общий вектор список обработанных слов в каждой строке'''
        self.df[self.new_name] = \
            [(sum(w2v_model.wv[self.df[self.new_name][i]])\
              /len(self.df[self.new_name][i])) \
             for i in range(0, len(self.df[self.new_name]))]
        return self.df
    
    def vector_row_average(self, row_name, new_name):
        '''Вычисляем среднее значение для вектора'''   
        self.df[self.new_name] = \
            [sum(self.df[self.new_name][i])
             /len(self.df[self.new_name][i])
             for i in range(0, len(self.df[self.new_name]))]
        return self.df

    def text_rows_nlp_vector(self, text_rows):
        '''Метод цикла для обработки текстовых полей - возможно нужно его убрать'''
        for row in text_rows:
            self.vector_row(row)
            self.df.drop(row, axis = 1, inplace = True)
        return self.df
    
    def text_row_nlp_vector(self, text_row):
        '''Метод для обработки текстового поля'''
        self.vector_row(text_row)
        self.df.drop(text_row, axis = 1, inplace = True)
        return self.df

    def row_worker(self, rows_list, worker_funk):
        '''Метод применения метода для перечня полей'''
        for row in rows_list: # цикл для всех полей
            worker_funk(row)
        return
    
    def category_change(self, row):
        '''Метод обработки категориальных данных'''
        # подготовим список категорий
        category_list = list(self.df[row].unique())
        # убираем из списка nan
        category_list = [x for x in category_list if x == x]

        count = 1 #счетчик
        for category in category_list:
            self.df.loc[self.df[row] == category, row] = count
            count += 1
        return

    def date_row(self, row):
        '''Метод работы с датами'''
        self.df[row + '_year'] = pd.DatetimeIndex(self.df[row]).year
        self.df[row + '_month'] = pd.DatetimeIndex(self.df[row]).month
        self.df.drop(row, axis = 1, inplace = True)
        return
    
    def date_mistake(self, row_mistake, rows_correct):
        '''Метод работы с неадекватными датами, замена на среднее значение'''
        for row_cor in rows_correct:
            self.df.loc[self.df[row_mistake] == 1, row_cor] = \
            round(self.df[row_cor].mean())
        return self.df
        # df - датафрейм
        # row_mistake - поле с данными об ошибке
        # rows_correct - список полей, где нужно вносить корректировки
    
    def outlier_row_mean(self, row, value):
        '''Метод отсечения выбросов - выброс больше value усредняется'''
        self.df.loc[self.df[row] > value, row] = round(self.df[row].mean())
        return

    def outlier_row_zero(self, row, value):
        '''Метод отсечения выбросов - выброс больше value = 0'''
        self.df.loc[self.df[row] > value, row] = 0
        return
    
    def dummy_ft(self, row):
        '''Метод дамми f = 0 t = 1'''
        self.df.loc[self.df[row] == 'f', row] = 0
        self.df.loc[self.df[row] == 't', row] = 1
        return
    
    def outlier_row_zero_less(self, row, value):
        '''Метод отсечения выбросов - выброс меньше value = 0'''
        self.df.loc[self.df[row] < value, row] = 0
        return

    def nan_value(self, row, value):
        '''метод присвоения nan заданного значения'''
        self.df.loc[self.df[row].isna(), row] = value
        return
    
    def drop_row(self, dell_rows):
        '''Удаление полей из df_train'''
        self.df.drop(columns = dell_rows, axis = 1, inplace = True)
        return self.df
    
    
    def transform_vector(self):
        '''Метод предобработки датафрейма'''
    
        '''Использование метода vector_row '''       
        self.df = self.text_rows_nlp_vector(self.text_rows)
        
        return self.df
    
    def transform_athers(self):
        
        '''Использование метода category_change'''
        self.row_worker(self.category_rows, self.category_change)
        
        '''Использование метода date_row'''
        date_rows = ['date_creation', 'date_posted']
        self.row_worker(date_rows, self.date_row)
        
        '''Использование метода date_mistake'''
            # для поля date_creation_mistake
        row_mistake = 'date_creation_mistake'
        rows_correct = ['date_creation_year', 'date_creation_month']
        self.df.loc[self.df['date_creation_mistake'] == 1, row_cor] = \
            round(self.df['date_creation_year'].mean())

            # для поля date_posted_mistake     
        row_mistake = 'date_posted_mistake'
        rows_correct = ['date_posted_year', 'date_posted_month']
        self.date_mistake(row_mistake, rows_correct)
        
        '''Использование метода outlier_row_mean'''
        self.outlier_row_mean('experience_requirements', 20)
        
        '''Использование метода outlier_row_zero'''
        self.outlier_row_zero('federal_district', 10)
        
        '''Использование метода category_change через метод работы с полями'''
        rows_list = ['is_uzbekistan_recruitment']
        self.row_worker(rows_list, self.dummy_ft)
        
        '''Корректируем ошибочные данные'''
        # Не может быть премия 10 руб., вероятно это 10 тыс.
        self.df.loc[(self.df['premium_size'] < 1000), 'premium_size'] = \
            self.df['premium_size'] * 1000
        
        '''Переводим тип премии в количество месяцев'''
        self.df.loc[(self.df['premium_type'] == \
                   'Ежемесячная премия'), 'premium_type'] = 1
        self.df.loc[self.df['premium_type'] == \
                  'Ежеквартальная премия', 'premium_type'] = 4
        self.df.loc[self.df['premium_type'] == \
                  'Ежегодная премия', 'premium_type'] = 12
        
        '''Генерим новое поле ежемесячной премии'''
        self.df['premium_size_month'] = \
            self.df['premium_size'] / self.df['premium_type']
        
        '''Использование метода outlier_row_zero_less'''
        self.outlier_row_zero_less('retraining_grant_value', 5000)
        
        '''Заполняем Nan заданными значениями'''
        self.nan_value('work_hours', '«Полный рабочий день»')
        self.nan_value('work_places', 1)
        
        '''Заполняем пустые значения во всём датафрейме'''
        self.df = self.df.fillna(0)
        
        '''Убираем лишние поля'''
        self.df = self.drop_row(self.dell_rows)
        return self.df
