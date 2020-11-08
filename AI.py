import speech_recognition as sr 
import pyttsx3
import webbrowser
import tkinter as tk
import wikipedia
engine=pyttsx3.init()


#predefined chats
greetings={"hello":"Hey my name is Jif How are you!","hi":"Hey my name is Joey How are you!","hey":"Hey my name is Joey How are you!"}
wish={"morning": "Good morning","night":"Good Night","care":"You too","bye":"Please don't go"}
silly={"marry":"No i don't think so right now","love":"I love myself too","hate":"You sure about that","children":"Yeah Children are cute"}

#pre defining the function
def check():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)
		order = r.recognize_google(audio,language="en-in")
	#this is used to fill the box l2 or display what the user said
	e2.insert(tk.END,order)
	x=order.split(" ")

	for word in x:
		if word in greetings:
			answer=greetings[word]
			engine.say(answer)
			engine.runAndWait()
			e1.insert(tk.END,answer)
		elif word in wish:
			#extracting the reply from the dictionary it self
			answer=wish[word]
			engine.say(answer)
			engine.runAndWait()
			e1.insert(tk.END,answer)
		elif "play" in x:
			webbrowser.open_new(f'https://www.youtube.com/results?search_query={x[1]}')
			answer = "Command Accepted"
			engine.say(answer)
			engine.runAndWait()
			break
		elif "search" in x:
			webbrowser.open_new(f'https://www.bing.com/search?q={x[1]}')
			answer = "The Search Results are"
			engine.say(answer)
			engine.runAndWait()
			break
		elif word in silly:
			answer=silly[word]
			engine.say(answer)
			engine.runAndWait()
			e1.insert(tk.END,answer)
		elif "what" in x or "who" in x:
			try:
				order=order.replace("who","")
			except:
				order=order.replace("what","")
			answer=wikipedia.summary(order,sentences=1)
			engine.say(answer)
			engine.runAndWait()
			e1.insert(tk.END,answer)
			break

		elif "exit" in x:
			root.destroy()

#gui
root=tk.Tk()
root.geometry("350x500")
root.title("Ai")
root.configure(bg="light blue")
e1 =tk.Text(root)
e1.place(x=10,y=35,height=75,width=330)
l1=tk.Label(root,text="Output")
l1.place(x=10,y=10)
e2=tk.Text(root)
e2.place(x=10,y=150,height=80,width=330)
l2=tk.Label(root,text="You Said :")
l2.place(x=10,y=120)
b=tk.Button(root,text="Speak",bg="yellow",fg="black",command=check)
b.place(x=100,y=300,height=75,width=150)

root.mainloop()