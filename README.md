# Virtual-Assistant
A virtual assistant just like Siri, Google assistant etc. which will execute your verbal commands. It requires stable Internet Connection for proper functioning. The given source code is written in python 3.6.

# Modules Required
Note: Some modules required for this program to run needs to be installed by using pip install <module name> in the terminal.
  
  1.**pyttsx3** : Pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3.
              Included TTS engines:
                   1.  sapi5
                   2.  nsss
                   3.  Espeak
Instead of pyttsx3 module, you can also use gTTS module too.
  
  2.**SpeechRecognition** : Library for performing speech recognition, with support for several engines and APIs, online and offline.
     **Requirements for functionality of the library:**
      - **Pyaudio** PyAudio is required if you want to use microphone input (Microphone). PyAudio version 0.2.11+ is required, as earlier   versions have known memory management bugs when recording from microphones in certain situations.
      - **Google API Client Library for Python** required only if you need to use the Google Clouds Speech API      
      
  3.**Wikipedia** : Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia. Type following command for installation
                    > pip install wikipedia
          
  4. **Webbroswer** : Webbrowser module provides a high-level interface which allows displaying Web-based documents to users.
  
  5. **OS and Datetime** : Both are inbuilt python library. Os is used for opening certain apps present in your PC. Datetime library is used to greet the user and tell the current time to user.
  
# Limitation and Solution

If a command different from the mentioned command is given no output is obtained. For example if you ask it "How you doing?" instead of "How are you?", it will not respond. But this minor problem can be eradicated by writing another else if condition or mending the previous condition by using "or" operator if the output is same just like in above case. 


