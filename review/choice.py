class Choice:

    actions_data = {}

    def __init__(self, json_data, num):
        self.num = num
        self.text = json_data['text']
        self.actions_data = json_data


    def __str__(self):
        return str(self.num) + ") " + self.text

    def make_choice(self, tarrifs):
        for key in self.actions_data:
            if key != 'text':
                for tarr_num in self.actions_data[key]:
                    tarrifs[key][tarr_num] += 1