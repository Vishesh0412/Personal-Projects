import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Vishesh Srivastava")
    while True:
        x = input("Enter what you want me to speak: ")
        if x == "q":
            os.system(f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('Bye Bye friend')")
            break
        command = f"Powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)