from urllib import response
from chatterbot.logic import LogicAdapter
import yaml



class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
        

    def can_process(self, statement):
        # Check if statement is travel related question
        # input_file = 'Data/testdata.yml'

        data_yml = open('testdata.yml', encoding="utf-8")
        parsed_file = yaml.load(data_yml, Loader=yaml.FullLoader)
        countries = (parsed_file["conversations"])
        for country in countries:
            if country[0] in statement.text:
                return True
        return False

    def process(self, input_statement, additional_response_selection_parameters=None):
        import random

        # Isolate the country name
        data_yml = open('testdata.yml', encoding="utf-8")
        parsed_file = yaml.load(data_yml, Loader=yaml.FullLoader)
        countries = (parsed_file["conversations"])
        for country in countries:
            if country[0] in input_statement.text:
                response1 = country[1]
        # Set confidence interval to 1 if a response is returned
        if response1:
            confidence =1
        else:
            confidence = 0
        selected_statement = input_statement
        selected_statement.text = response1
        selected_statement.confidence = confidence

        return selected_statement
