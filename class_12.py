
'''В приведенных примерах происходит инициализация переменных в разных частях кода.
См. комментарии #ПРИМЕР: '''

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


adres_train = 'C:/Users/Ник/Desktop/ml/RuCode5_vacancy_salary_pred/train.csv'
df_tr = pd.read_csv(adres_train) #  ПРИМЕР: Переменная инициируется в начале исполнения кода. Далее    происходит её переопределение практически в каждом методе класса

#  ПРИМЕР: Переменная инициируется один раз в начале исполнения кода, применяется сразу и далее остаётся неизменной
text_rows = ['additional_info', 'career_perspective',
         'job_benefits', 'job_benefits_other_benefits', 
         'job_location_address', 'metro_station', 
         'requirements_qualifications', 'requirements_required_certificates', 
         'responsibilities', 'retraining_condition', 
         'social_protecteds_social_protected', 'title']

shot_instance = Data_Preprocess(df_tr, text_rows, category_rows, dell_rows)
df_tr = shot_instance.vector_row_1('additional_info')
df_tr = shot_instance.vector_row_2('additional_info')
df_tr = shot_instance.vector_row_3('additional_info')
df_tr = shot_instance.vector_row_4('additional_info')