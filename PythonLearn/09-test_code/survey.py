"""调查问卷"""
class AnonymousSurvey:
    """收集匿名调查问卷"""

    def __init__(self, question):
        """storage a question and prepare to store a response"""
        self.question = question
        self.response = []
    
    def show_question(self):
        """show question"""
        print(self.question)
    
    def store_responce(self, new_responce):
        """store single survey"""
        self.response.append(new_responce)

    def show_results(self):
        """show all responces"""
        print("Survey results: ")
        for res in self.response:
            print(f' - {res}')



