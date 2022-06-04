import review.choice as ch

class Question:

    choices = {}

    def __init__(self, json_data, num):
        self.num = num
        self.text = json_data['text']
        ques_choices = []
        for i in range (1, len(json_data)):
            choice = ch.Choice(json_data[str(i)], i)
            ques_choices.append(choice)
        self.choices[str(self.num)] = ques_choices
            

    def __str__(self):
        return str(self.num) + ") " + self.text


    def start(self):
        for choice in self.choices[str(self.num)]:
            print(choice)