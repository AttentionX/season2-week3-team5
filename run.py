import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')


import pyautogui
import time

os_type = 'win' # 'mac'

def openApp(app):
    if os_type == 'win':
        pyautogui.press('win')
    else:
        pyautogui.hotkey('command', 'space')
    time.sleep(1)
    
    pyautogui.typewrite(app)
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(1)

def calculate(equation):
    pyautogui.typewrite(equation)
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(1)
 
    pyautogui.hotkey('ctrl', 'c')

def searchGoogle(searchKeyword):
    pyautogui.typewrite(searchKeyword)
    time.sleep(1)
    
    pyautogui.press('enter')
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    
    
def writeMemo():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
def complete():
    exit()
 
def main():
    calculate('9+1')
    writeMemo()
    searchGoogle('llava2')
    writeMemo()
    
initial_prompt = '''
You are the Agent that determines the next action to achieve the final object.
There are three movements that you can perform. Determine the next action considering the current screen condition.

def openApp(app)
- OpenApp function lets you open the app by inserting the app name.
- You can enter only three types of app name: 'calculator', 'chrome', and 'memo'.

def calculate(equation)
- Calculate function performs calculations when you insert an equation and copies the calculation results to the clipboard.

def searchGoogle(searchKeyword)
- The searchGoogle function enters the searchKeyword into the Google search box and copies the entire search result to the clipboard.

def writeMemo()
- writeMemo function opens and pastes what is copied to the clipboard.

def complete()
- The complete function is invoked when all operations are complete and causes the process to terminate.


Sample Output 1:
Input:
Current screen status: Desktop is displayed
Final object: add 2 to 8 and find out what the value minus 3 is and paste it into Notepad

Output:
openApp('calculator')
calculate('8+2-3')
openApp('memo')
writeMemo()
complete()

Sample Output 2:
Input:
Current screen status: Calculator is on the screen
Final object: add 2 to 8 and find out what the value minus 3 is and paste it into Notepad

Output:
calculate('8+2-3')
openApp('memo')
writeMemo()
complete()

---------

'''
    
if __name__=='__main__':
    
    status = input('current status: ')
    objective = input('final objective: ')
    
    current_prompt = f' \
    Input:                      \
    Current screen status: {status}   \
    Final objective:  {objective}          \
    Output:                     \
    '
    prompt = initial_prompt + current_prompt
    completion = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    )
    
    output = str(completion.choices[0].message.content)
    commands = output.split('\n')
    for command in commands:
        print(command)
        eval(command)
 
