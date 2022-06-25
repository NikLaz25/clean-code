'''В представленных ниже 12 методах, в соответствии с первым пунктом задания, 
изменены имена функций на более понятные, и убраны соответствующие комментарии'''

class Data_Preprocess:
    '''Класс предобработки данных'''
    def __init__(self, df, text_rows, category_rows, dell_rows):
        self.df = df
        self.text_rows = text_rows
        self.category_rows = category_rows
        self.dell_rows = dell_rows
        self.new_name = None
    
    def get_word_formal_form(self, doc):
        doc = re.sub(patterns, ' ', str(doc)) 
        tokens = []
        for token in doc.split():
            if token and token not in stopwords_ru:
                token = token.strip()
                token = morph.normal_forms(token)[0]
                tokens.append(token)
        return tokens
    
    def fill_empty_lines(self, row_name):
        self.df[row_name] = self.df[row_name].fillna('пусто')
        return self.df
    
    def get_tokens_of_text_field(self, row_name):
        self.new_name = row_name + '_vec'
        self.df[self.new_name] = self.df.apply\
            (lambda row: tokenizer.tokenize\
            (row[row_name].lower()), axis = 1)
        return self.df
    
    def get_row_formal_form(self, row_name):
        self.df[self.new_name] = self.df[self.new_name].apply(self.lemmatize)
        return self.df
    
    def remov_stop_words(self, row_name):
        self.df[self.new_name] = self.df.apply(lambda row: \
            [word for word in row[self.new_name] if word \
            not in stopWords_ru], axis = 1)
        return self.df
    
    def model_training(self, row_name):

        # зададаём параметры модели
        w2v_model = Word2Vec(
            min_count=1, # 10 для полного поля, для реальной работы
            window=2,
            size=300,
            negative=10,
            alpha=0.03,
            min_alpha=0.0007,
            sample=6e-5,
            sg=1)

        # получаем словарь
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
    
    def calculate_vector_average_value(self, row_name, new_name):
        self.df[self.new_name] = \
            [sum(self.df[self.new_name][i])
             /len(self.df[self.new_name][i])
             for i in range(0, len(self.df[self.new_name]))]
        return self.df

    def cycle_for_text_fields(self, text_rows):
        for row in text_rows:
            self.vector_row(row)
            self.df.drop(row, axis = 1, inplace = True)
        return self.df
    
    def text_field_processing(self, text_row):
        self.vector_row(text_row)
        self.df.drop(text_row, axis = 1, inplace = True)
        return self.df

    def applying_def_for_fields_list(self, rows_list, worker_funk):
        for row in rows_list: # цикл для всех полей
            worker_funk(row)
        return
    
    def processing_categorical_row(self, row):

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
        self.df[row + '_year'] = pd.DatetimeIndex(self.df[row]).year
        self.df[row + '_month'] = pd.DatetimeIndex(self.df[row]).month
        self.df.drop(row, axis = 1, inplace = True)
        return
    
    def replacing_outlier_to_average_value(self, row_mistake, rows_correct):
        for row_cor in rows_correct:
            self.df.loc[self.df[row_mistake] == 1, row_cor] = \
            round(self.df[row_cor].mean())
        return self.df
        # df - датафрейм
        # row_mistake - поле с данными об ошибке
        # rows_correct - список полей, где нужно вносить корректировки
