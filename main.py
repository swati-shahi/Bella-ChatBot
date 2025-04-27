import tkinter as tk
import random
import webbrowser
import datetime
import os
import platform
import subprocess
import pyautogui
import time
import re
import winsound 
import sys

# Function to get bot response
def get_bot_response(user_input):
    user_input = user_input.lower()

    exit_phrases = ['ok bye', 'see you later', 'talk to you later', 'bye', 'stop', 'now exit']
    if any(phrase in user_input for phrase in exit_phrases):
        print("Ok bye, see you soon!")  # farewell message
        sys.exit()  # Terminate the program



    greetings = ['hello', 'hi', 'hey', 'hola', 'namaste']
    how_are_you = ["how are you", "how are you doing", "how are you doing today"]
    what_are_you_doing = ["what are you doing", "what's up", "what are you up to"]
    english_jokes = [
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my wife she was drawing her eyebrows too high. She looked surprised.",
        "What’s orange and sounds like a parrot? A carrot!",
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "What do you call fake spaghetti? An impasta!",
        "Why can’t you hear a pterodactyl go to the bathroom? Because the 'P' is silent!",
        "I used to play piano by ear, but now I use my hands.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "I told my computer I needed a break, and now it won’t stop sending me beach wallpapers."
    ]
   
    time_questions = ["time", "what time is it", "current time" , "what's time now?" , "what is the time?"]
    day_questions = ["day", "which day is today", "today's day", "what day is it", "what's today" , "what day is today?"]
    date_questions = [
    "date", "what is the date", "current date", "which date is today", 
    "today's date", "what's today's date", "today's date is", 
    "what date is it", "give me the date", "show me the date"
]  # Added for current date logic
    google_search = ["search", "google", "find", "search for", "what is" , "who is" , "when did" , "how is" ]
    open_website = ["open "]
    close_tab = ["close tab", "close browser", "exit tab", "close"]
    arithmetic_operations = ["add", "subtract", "multiply", "divide"]



     # Current Date logic 

    if any(word in user_input for word in date_questions):
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')  # format as YYYY-MM-DD
        return f"Today's date is {current_date}."



    # Day logic 

    elif any(word in user_input for word in day_questions):
        today = datetime.datetime.now().strftime('%A')
        return f"Today is {today}."
    


       # Exit logic 

    exit_phrases = ['ok bye', 'see you later', 'talk to you later', 'bye', 'stop', 'now exit']
    if any(phrase in user_input for phrase in exit_phrases):
        return "Ok bye, see you soon!"
    



    # Greeting logic

    elif any(greeting in user_input for greeting in greetings):
        return random.choice(["Good morning!", "Good afternoon!", "Good evening!", "Hello!", "Hi there!"])



    # How are you logic

    elif any(phrase in user_input for phrase in how_are_you):
        return random.choice([ 
            "I'm just a bunch of code, but I'm doing great!", 
            "Feeling chatty as always!", 
            "Better now that you're here 😊"
        ])



    # What are you doing logic

    elif any(phrase in user_input for phrase in what_are_you_doing):
        return random.choice([ 
            "I'm here waiting to help you!", 
            "Just chilling in your RAM 😎", 
            "Helping amazing humans like you!"
        ])



    # Joke request logic 
    
    elif "joke" in user_input:
        return random.choice(english_jokes)



    # current Time logic

    elif any(word in user_input for word in time_questions):
        current_time = datetime.datetime.now().strftime('%H:%M')
        return f"The current time is {current_time}."



    # google search logic

    elif any(phrase in user_input for phrase in google_search):
        search_query = user_input
        for word in google_search:
            search_query = search_query.replace(word, "")
        search_query = search_query.strip()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            return "Searching on Google..."
        else:
            return "Please tell me what you'd like to search."



    # Open website logic

    elif any(phrase in user_input for phrase in open_website):
        for phrase in open_website:
            if phrase in user_input:
                site = user_input.replace(phrase, "").strip()
                if not site.startswith("http"):
                    if "." not in site:
                        site = "https://www." + site + ".com"
                    else:
                        site = "https://" + site
                try:
                    webbrowser.open(site)
                    return f"Opening {site}..."
                except:
                    return "Couldn't open the website. Please check the URL."



    # Close tab logic

    elif any(phrase in user_input for phrase in close_tab):
        return close_browser_tab()



    # Screenshot request logic

    elif "screenshot" in user_input:
        take_screenshot()
        return "Screenshot taken and saved!"
    

    # Math pattern solving logic

    math_patterns = [
        r'add (\d+) and (\d+)',
        r'subtract (\d+) from (\d+)',
        r'subtract (\d+) and (\d+)',
        r'multiply (\d+) and (\d+)',
        r'solve (.+)',
        r'what is (.+)',
        r'(\d+)\s*[\+\-\*/]\s*(\d+)' 
    ]

    for pattern in math_patterns:
        match = re.search(pattern, user_input)
        if match:
            try:
                if "add" in user_input:
                    num1, num2 = int(match.group(1)), int(match.group(2))
                    return f"The result of addition is: {num1 + num2}"
                elif "subtract" in user_input:
                    if 'from' in user_input:
                        num1, num2 = int(match.group(1)), int(match.group(2))
                        return f"The result of subtraction is: {num2 - num1}"
                    else:
                        num1, num2 = int(match.group(1)), int(match.group(2))
                        return f"The result of subtraction is: {num1 - num2}"
                elif "multiply" in user_input:
                    num1, num2 = int(match.group(1)), int(match.group(2))
                    return f"The result of multiplication is: {num1 * num2}"
                elif "divide" in user_input:
                    num1, num2 = int(match.group(1)), int(match.group(2))
                    if num2 == 0:
                        return "Division by zero is undefined."
                    return f"The result of division is: {num1 / num2}"
                else:
                    expression = match.group(0)
                    result = eval(expression)
                    return f"The answer is: {result}"
            except:
                return "I couldn't solve that. Could you ask again?"

    # Arithmetic operations logic
    if any(word in user_input for word in arithmetic_operations):
        return perform_arithmetic(user_input)

    return "I'm not sure about that. Could you ask something else?"



# arithmetic operations

def perform_arithmetic(user_input):
    try:
        if "add" in user_input:
            numbers = [int(i) for i in user_input.split() if i.isdigit()]
            result = sum(numbers)
            return f"The result of addition is: {result}"
        elif "subtract" in user_input:
            numbers = [int(i) for i in user_input.split() if i.isdigit()]
            result = numbers[0] - numbers[1]
            return f"The result of subtraction is: {result}"
        elif "multiply" in user_input:
            numbers = [int(i) for i in user_input.split() if i.isdigit()]
            result = numbers[0] * numbers[1]
            return f"The result of multiplication is: {result}"
        elif "divide" in user_input:
            numbers = [int(i) for i in user_input.split() if i.isdigit()]
            result = numbers[0] / numbers[1]
            return f"The result of division is: {result}"
        else:
            return "Please provide valid numbers and operation."
    except Exception as e:
        return f"Error in arithmetic operation: {str(e)}"



# take a screenshot

def take_screenshot():
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot = pyautogui.screenshot()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{timestamp}.png"
    screenshot.save(os.path.join(screenshots_dir, filename))

    winsound.Beep(1000, 300)  # Sound after taking screenshot
    print("Screenshot saved successfully!")



# close current Chrome tab

def close_browser_tab():
    os_name = platform.system()
    try:
        if os_name == "Windows":
            time.sleep(1)
            pyautogui.hotkey('alt', 'tab')
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'w')
        else:
            print("Closing tabs is only supported on Windows for now.")
    except Exception as e:
        print(f"Failed to close browser tab: {str(e)}")


# GUI setup

root = tk.Tk()
root.title("Bella - Your Chatbot Companion")
root.state('zoomed')
root.configure(bg="#f7f7f7")

frame = tk.Frame(root, bg="#ffffff", bd=2, relief=tk.GROOVE)
frame.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

chat_box = tk.Text(frame, wrap=tk.WORD, state=tk.DISABLED, bg="#f0f0f0", fg="#333", font=("Segoe UI", 11))
chat_box.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

entry_box = tk.Entry(root, font=("Segoe UI", 14), bd=2)
entry_box.pack(padx=20, pady=10, fill=tk.X)



# send user input and bot response
def send_message(event=None):
    user_input = entry_box.get()
    if user_input != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + user_input + "\n")
        bot_response = get_bot_response(user_input)
        chat_box.insert(tk.END, "Bella: " + bot_response + "\n")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)
        entry_box.delete(0, tk.END)


# Send message on 'Enter' key 
entry_box.bind('<Return>', send_message)

root.mainloop()
