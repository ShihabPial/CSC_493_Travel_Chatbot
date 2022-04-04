from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        # Check if statement is travel related question
        if statement.text.startswith('Can i go to'):
            return True
        return False

    def process(self, input_statement, additional_response_selection_parameters):
        import random
        # Isolate the country name
            # todo
        
        # Use Best Match logic adapter to search for country name
            #todo

        # Set confidence interval to 1 if a response is returned
        confidence = random.uniform(0, 1)
        # If no response is returned return "Country information not found"
            #todo
        selected_statement = input_statement
        selected_statement.confidence = confidence

        return selected_statement
