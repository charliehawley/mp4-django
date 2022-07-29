'''
Python Unittests for models
'''
import unittest
from datetime import date
from models import Prompt


class TestPrompt(unittest.TestCase):
    '''
    Test attributes and methods of the Prompt model
    '''
    def test_prompt(self):
        '''
        Test return prompt
        '''
        today = date.today()
        prompt = Prompt(today, 'How much wood would a woodchuck chuck?')

        self.assertEqual(self.prompt.return_prompt,
                         'How much wood would a woodchuck chuck?')


if __name__ == '__main__':
    unittest.main()
