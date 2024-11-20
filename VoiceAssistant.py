import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
from tkinter import *
import threading
import queue
import pyautogui
import time
import os


class assistance_gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.root.geometry('600x600')
        self.running = False
        self.command_queue = queue.Queue()

        # Initialize incrementable_counter here
        self.incrementable_counter = 0  # Initialize the instance variable

        # ====start button
        start = Button(self.root, text='START', font=("times new roman", 14), command=self.start_option)
        start.place(x=150, y=520)

        # ====close button
        close = Button(self.root, text='CLOSE', font=("times new roman", 14), command=self.close_window)
        close.place(x=350, y=520)

        # ====allow user to close when prompt isnt being executed
        self.root.bind('<Escape>', lambda event: self.close_window())

        # Register Chrome as the browser
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        

        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def start_option(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.voice_recognition_thread, daemon=True).start()
            self.root.after(100, self.process_commands)
            self.speak('Aight Go')

    def voice_recognition_thread(self):
        while self.running:
            try:
                with sr.Microphone() as data_taker:
                    print("Say Something")
                    voice = self.listener.listen(data_taker, timeout=5, phrase_time_limit=5)
                    instruction = self.listener.recognize_google(voice).lower()
                    self.command_queue.put(instruction)
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except Exception as e:
                print(f"An error occurred: {e}")

    def process_commands(self):
        try:
            while not self.command_queue.empty():
                instruction = self.command_queue.get_nowait()
                self.execute_command(instruction)
        finally:
            if self.running:
                self.root.after(100, self.process_commands)

    def close_chrome_tab(self):
        # Find Chrome windows
        chrome_windows = pyautogui.getWindowsWithTitle('Chrome')
        
        if chrome_windows:
            chrome_window = chrome_windows[0]  # Get the first Chrome window
            chrome_window.activate()  # Bring Chrome to the foreground
            
            time.sleep(0.2)  # Wait for the window to be active
            
            # Use the keyboard shortcut to close the current tab
            pyautogui.hotkey('ctrl', 'w')
            print("Chrome tab closed")
        else:
            print("No Chrome window found")
    
    def open_chrome_tab(self):
        # Find Chrome windows
        chrome_windows = pyautogui.getWindowsWithTitle('Chrome')
        
        if chrome_windows:
            chrome_window = chrome_windows[0]  # Get the first Chrome window
            chrome_window.activate()  # Bring Chrome to the foreground
            
            time.sleep(0.2)  # Wait for the window to be active
            
            # Use the keyboard shortcut to close the current tab
            pyautogui.hotkey('ctrl', 't')
            print("Chrome tab closed")
        else:
            print("No Chrome window found")

    def type_what_i_say(self):
        # Initialize the recognizer
        recognizer = sr.Recognizer()

        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            self.speak("Ready to type.")
            
            # Adjust for ambient noise and listen for input
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")

            # Give a short pause before typing
            time.sleep(0.2)

            # Type out the recognized text
            pyautogui.write(text)
            self.speak("Finished typing.")

        except sr.UnknownValueError:
            self.speak("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            self.speak(f"Could not request results from Google Speech Recognition service.")
        except Exception as e:
            self.speak(f"An error occurred while typing.")
    
    def open_spotify(self):
        # Press the Windows key
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        # Type "Spotify"
        pyautogui.write('Spotify')
        time.sleep(0.1)  # Wait for the search results

        # Press Enter to open Spotify
        pyautogui.press('enter')

    def open_discord(self):
        # Press the Windows key
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        # Type "Discord"
        pyautogui.write('Discord')
        time.sleep(0.1)  # Wait for the search results

        # Press Enter to open discord
        pyautogui.press('enter')

    def open_notepad(self):
        # Press the Windows key
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        # Type "notepad"
        pyautogui.write('notepad')
        time.sleep(0.1)  # Wait for the search results

        # Press Enter to open notepad
        pyautogui.press('enter')
    
    def open_steam(self):
        # Press the Windows key
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        # Type "steam"
        pyautogui.write('steam')
        time.sleep(0.1)  # Wait for the search results

        # Press Enter to open steam
        pyautogui.press('enter')
    
    def open_runescape(self):
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        pyautogui.write('jagex launcher')
        time.sleep(0.1)  # Wait for the search results

        pyautogui.press('enter')

    def open_unity(self):
        pyautogui.press('win')
        time.sleep(0.1)  # Wait for the start menu to open

        pyautogui.write('unity hub')
        time.sleep(0.1)  # Wait for the search results

        pyautogui.press('enter')

    def resetIncrementableValue(self):
        self.incrementable_counter = 0  # Reset the instance variable

    def incrementTheIncrementableValue(self):
        self.incrementable_counter += 1  # Increment the instance variable

    def returnIncrementableValue(self):
        self.speak(f' {self.incrementable_counter}')  # Access the instance variable

    def execute_command(self, instruction):
        print(instruction)
        if 'who are you' in instruction:
            self.speak('nobody special')
        elif 'wake up' in instruction:
            self.speak('ok im here chill')
        elif 'increment counter' in instruction or 'add to counter' in instruction:
            self.speak('ok im incrementing the counter')
            self.incrementTheIncrementableValue()
        elif 'reset counter' in instruction or 'reset the counter' in instruction:
            self.speak('ok im resetting the counter')
            self.resetIncrementableValue()
        elif 'counter value' in instruction or 'what is the counter value' in instruction or 'what is the counter' in instruction:
            self.speak('ok the counter value is ')
            self.returnIncrementableValue()
        elif 'open unity' in instruction:
            self.speak('opening unity')
            self.open_unity()
        elif 'open spotify' in instruction:
            self.speak('opening spotify')
            self.open_spotify()
        elif 'open discord' in instruction:
            self.speak('opening discord')
            self.open_discord()
        elif 'open notepad' in instruction:
            self.speak('opening notepad')
            self.open_notepad()
        elif 'open steam' in instruction:
            self.speak('opening steam')
            self.open_steam()
        elif 'open runescape' in instruction:
            self.speak('opening runescape')
            self.open_runescape()
        elif 'current time' in instruction or 'what time is it' in instruction:
            time = datetime.datetime.now().strftime('%I: %M')
            self.speak('current time is' + time)
        elif 'open google' in instruction:
            self.speak('Opening Google')
            webbrowser.get('chrome').open('google.com')
        elif 'open youtube' in instruction:
            self.speak('Opening Youtube')
            webbrowser.get('chrome').open('https://www.youtube.com')
        elif 'open linkedin' in instruction:
            self.speak('Opening Linkedin')
            webbrowser.get('chrome').open('linkedin.com')
        elif 'open gmail' in instruction:
            self.speak('Opening Gmail')
            webbrowser.get('chrome').open('gmail.com')
        elif 'open my portfolio' in instruction or 'open portfolio' in instruction:
            self.speak('Opening your portfolio')
            webbrowser.get('chrome').open('https://michaelsn22.github.io/')
        elif 'close chrome window' in instruction or 'close chrome tab' in instruction or 'close tab' in instruction:
            self.speak('closing chrome tab')
            self.close_chrome_tab()
        elif 'open new tab' in instruction or 'open new chrome tab' in instruction or 'open tab' in instruction or 'open chrome tab' in instruction:
            self.speak('opening new tab')
            self.open_chrome_tab()
        elif 'open yahoo' in instruction or 'open yahoo mail' in instruction or 'open my email' in instruction:
            self.speak('Got it, opening your yahoo email')
            webbrowser.get('chrome').open('https://mail.yahoo.com/')
        elif 'type something for me' in instruction:
            self.speak("Sure, one sec")
            self.type_what_i_say()
        elif 'shutdown' in instruction or 'shut down' in instruction or 'exit' in instruction or 'close' in instruction or 'pound salt' in instruction:
            self.speak('Got it, shutting down!')
            self.close_window()
        else:
            self.speak('What lol')

    def close_window(self):
        self.running = False
        self.root.destroy()

root = Tk()
obj = assistance_gui(root)
root.mainloop()
