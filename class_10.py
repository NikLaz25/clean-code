	- Переменная инициализирована непосредственно перед циклом
	my_sum = 0	
	   for i in my_line:
	        If my_dict.get(i) is not None:
	             my_sum += my_dict.get(i)
	         else:
	             my_sum += 23
	    return my_sum
	- Переменные инициализированы непосредственно перед циклом
	   modul_of_difference = ''
	    less_than_zero = 0
	#     основной цикл
	    for i in range(len(a1)):
	        try:
	            if less_than_zero == 0 and (int(a1[i]) - int(a2[i])) < 0:
	                difference = 10 + int(a1[i]) - int(a2[i])
	                less_than_zero = 1
	
	            elif less_than_zero == 0 and (int(a1[i]) - int(a2[i])) >= 0:
	                difference = int(a1[i]) - int(a2[i])
	                less_than_zero = 0
	
	
	            elif less_than_zero == 1 and (int(a1[i]) - 1 - int(a2[i])) < 0:
	                difference = int(10 + a1[i])- 1 - int(a2[i])
	                less_than_zero = 1
	
	            elif less_than_zero == 1 and (int(a1[i]) - 1 - int(a2[i])) >= 0:
	                difference = int(a1[i]) - 1 - int(a2[i])
	                less_than_zero = 0
	
	            modul_of_difference += str(difference)
	- Переменные инициализированы непосредственно перед циклом    
	    number = modul_of_difference[::-1]
	    less_than_zero = 0
	    number_to_answer = ''
	    for i in number:
	        if i == '0' and less_than_zero == 0:
	            pass
	        else:
	            less_than_zero = 1
	            number_to_answer += i
	    return number_to_answer
	-  Переменная инициализирована непосредственно перед циклом
	    Votes_max = 0
	    for i in range(N):
	        if Votes[i] > Votes_max:
	            Votes_max = Votes[i]
	- Переменные инициализированы непосредственно перед циклом  
	def UFO(N, data, octal):
	    if octal == False:
	        system = 16
	
	    else:
	        system = 8
	    new_data = []
	    
	    for i in range(N):
	        new_data += [int(str(data[i]), system)]
	- Переменные инициализированы непосредственно перед циклом
	time = 0 #время в пути
	travel = 0 #пройденный путь
	    while travel < L:
	        if travel not in way_traffick_light:
	            travel +=1
	            time += 1
	- Переменная инициализирована непосредственно перед циклом
	    # расчет максимального времени,если все светофоры будут красными максимально долго
	    time_max = L
	    for i in range(N):
	        time_max += track[i][2]
	- Переменная инициализирована непосредственно перед циклом
	    work_light = [[] for x in range(N)]
	    for number_light in range(N):
	        cycle = track[number_light][1] + track[number_light][2]
	        step = 0
	        while len(work_light[number_light]) < (time_max):
	            for x in range(cycle):
	                if x <= (track[number_light][1] - 1) and step <= (time_max - 1):
	                    work_light[number_light].append(0)
	                    step += 1
	                elif x > (track[number_light][1] -1) and step <= (time_max - 1):
	                    work_light[number_light].append(1)
	                    step += 1
	                else:
	                    step += 1
	- Переменные инициализированы непосредственно перед циклом
	    general_match = 0
	    removed_lines_matrix1 = []
	    for i2, line_2 in enumerate(S2_split): # проходим матрицу 2
	        local_match = 0
	        for i1, line_1 in enumerate(S1_split): # проходим матрицу 1
	            # убираем из цикла строки, где уже были совпадения
	            if i1 in removed_lines_matrix1:
	                pass
	            else:
	                # цикл поиска line_2 в line_1
	                if line_2 in line_1: # если нашли 
	                    general_match += 1
	                    local_match += 1
	                    removed_lines_matrix1.append(i1)
	                    break
	                else:  # если не нашли
	                    pass
	- Переменная инициализирована непосредственно перед циклом
	    # разбиваем строку
	    line_split = line.split('*')
	      
	    # проверяем равенство символов
	    for i in range(len(line_split) - 1):
	        if line_split[i] == line_split[i + 1]:
	            result = True
	        else:
	            result = False
	            return result
            break