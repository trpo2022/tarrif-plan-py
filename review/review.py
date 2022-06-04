import review.question as q

class Review:
    
    questions = []
    tarrifs = {}
    json_data = {}

    def __init__(self, json_data):#parse json
        
        self.json_data = json_data
        q_json = json_data['questions']
        t_json = json_data['operators']

        for i in range(1, len(q_json) + 1):
            #create new question
            ques = q.Question(q_json[str(i)], i)
            self.questions.append(ques)
        
        for operator in t_json:
            tarrifs_count = len(t_json[operator])
            self.tarrifs[operator] = [0] * tarrifs_count

    def try_input(self, num, min_inc, max_inc):
        try:
            num = int(num)
            if num >= min_inc and num <= max_inc:
                return True
            else:
                return False
        except:
            return False

    def start(self):
        for ques in self.questions:
            #print question 
            print('\n')
            print(ques)
            print('\n')
            ques.start()
            #wait input
            inp = 0
            while True:
                inp = input('\nEnter number: ')

                if self.try_input(inp, 1, len(ques.choices[str(ques.num)])):
                    break
                else:
                    print('\nEnter valid number!\n')

            #here we have right choice
            choice = ques.choices[str(ques.num)][int(inp) - 1]
            choice.make_choice(self.tarrifs)
        
        for tarrif in self.tarrifs:
            print('Recomendations per operator: ')
            print('\n')
            print(tarrif.upper())
            print('\n')
            tarrif_max = max(self.tarrifs[tarrif])
            tarrif_ind = self.tarrifs[tarrif].index(tarrif_max)
            print(self.json_data['operators'][tarrif][str(tarrif_ind)])    
            
            