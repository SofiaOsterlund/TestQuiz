import random
import tkinter as tk
from tkinter import ttk

#var
Coms = []

#main
def main():
    init()

#class
class Command:
    def __init__(self, com, meaning, chapter):
        self.com = com
        self.meaning = meaning
        self.chapter = chapter


#Methods
def init():
    with open("LinuxComs.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Hoppa över tomma rader och kommentarer
            if not line or line.startswith("#"):
                continue

            # Dela raden i tre delar
            com, meaning, chapter = line.split(",")

            # Ta bort extra mellanslag
            com = com.strip()
            meaning = meaning.strip()
            chapter = chapter.strip()

            # Skapa objektet
            command = Command(com, meaning, chapter)
            Coms.append(command)
            

def makeQuestion():

    selection = random.randrange(len(Coms))

    question = Coms[selection].meaning
    answer = Coms[selection].com

    questionLabel.config(text=question)
    answerEntry.delete(0, tk.END)


main()
window = tk.Tk()
window.title("Learn Linux")
window.geometry("600x600")

# Skapa tab-kontrollen
notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

# Skapa två tabs
tabExam = ttk.Frame(notebook)
tabReadCommands = ttk.Frame(notebook)

# Lägg till tabs i Notebook
notebook.add(tabExam, text="Test yourself")
notebook.add(tabReadCommands, text="Commands Red Hat")

# TAB Do the test
#-------------------------------------------------------------------------------
ttk.Label(tabExam, text="Testa dig själv").pack(pady=20)
questionLabel = ttk.Label(tabExam, text="")
questionLabel.pack(pady=20)

answerEntry = ttk.Entry(tabExam)
answerEntry.pack(pady=20)

ttk.Button(tabExam, text="Start Test", command=makeQuestion).pack()

# TAB Read commands
#-------------------------------------------------------------------------
ttk.Label(tabReadCommands, text="Text").pack(pady=20)

# Läs in filen
with open("LinuxComs.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Textfält
comText = tk.Text(tabReadCommands)
comText.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(tabReadCommands, command=comText.yview)
scrollbar.pack(side="right", fill="y")

# Koppla scrollbar till textfältet
comText.config(yscrollcommand=scrollbar.set)

# Lägg in filens innehåll
comText.insert("1.0", content)

window.mainloop()


