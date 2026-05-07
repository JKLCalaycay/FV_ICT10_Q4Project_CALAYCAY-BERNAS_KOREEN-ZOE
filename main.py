from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt
a
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"<strong>{self.name}</strong> from {self.section} loves <em>{self.favorite_subject}</em>!"

classmates_list = [
    Classmate("Ebtisam", "10-RUBY", "ICT"),
    Classmate("Aeiou", "10-RUBY", "PE"),
    Classmate("Ethan", "10-RUBY", "TLE")
]

def display_all_classmates(e=None):
    output_div = document.getElementById("output_area")
    if output_div:
        output_div.innerHTML = "" 
        for person in classmates_list:
            div = document.createElement("div")
            div.className = "border-bottom py-2"
            div.innerHTML = person.introduce()
            output_div.appendChild(div)

def add_new_classmate(e):
    name_in = document.getElementById("input_name").value
    subject_in = document.getElementById("input_subject").value
    if name_in and subject_in:
        new_person = Classmate(name_in, "10-RUBY", subject_in)
        classmates_list.append(new_person)
        document.getElementById("input_name").value = ""
        document.getElementById("input_subject").value = ""
        display_all_classmates()

absence_data = np.array([0, 0, 0, 0, 0])
days_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

def generate_graph():
    target_div = document.getElementById('graph-inner')
    if target_div:
        target_div.innerHTML = ""
        fig, ax = plt.subplots(figsize=(7, 4))
        ax.plot(days_labels, absence_data, marker='o', color='#F7A5A5', linewidth=3)
        ax.set_title("Weekly Class Absences")
        ax.set_ylim(0, max(max(absence_data) + 2, 5))
        display(fig, target='graph-inner')

def update_attendance(e):
    day_idx = int(document.getElementById('day-select').value)
    count_val = document.getElementById('absence-count').value
    if count_val.isdigit():
        absence_data[day_idx] = int(count_val)
        generate_graph()

display_all_classmates()
generate_graph()