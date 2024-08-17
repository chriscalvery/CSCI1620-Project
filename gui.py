import tkinter as tk
from tkinter import messagebox
from VotingSystem import Voting_System

class VotingApp:
    def __init__(self, window: tk.Tk, voting_system: Voting_System):
        self.window = window
        self.window.title("Voting System")
        self.voting_system = voting_system

        # Frame for candidate selection
        self.frame_one = tk.Frame(self.window)
        self.label_vote = tk.Label(self.frame_one, text="Vote for your Candidate", font=("Arial", 14))
        self.label_vote.pack(pady=10)
        self.frame_one.pack()

        # Frame for radio buttons
        self.frame_two = tk.Frame(self.window)
        self.radio_selection = tk.IntVar()
        self.radio_selection.set(0)
        self.radio_john = tk.Radiobutton(self.frame_two, text="John", variable=self.radio_selection, value=1, font=("Arial", 12))
        self.radio_jane = tk.Radiobutton(self.frame_two, text="Jane", variable=self.radio_selection, value=2, font=("Arial", 12))
        self.radio_john.pack(anchor="w", pady=2)
        self.radio_jane.pack(anchor="w", pady=2)
        self.frame_two.pack(pady=10)

        # Frame for vote button
        self.frame_three = tk.Frame(self.window)
        self.button_vote = tk.Button(self.frame_three, text="Vote", command=self.submit_vote, font=("Arial", 12))
        self.button_vote.pack(pady=10)
        self.frame_three.pack()

        # Frame for displaying results
        self.frame_four = tk.Frame(self.window)
        self.button_results = tk.Button(self.frame_four, text="Show Results", command=self.show_results, font=("Arial", 12))
        self.button_results.pack(pady=10)
        self.frame_four.pack()

    def submit_vote(self):
        """Handles vote submission."""
        selected_candidate = self.radio_selection.get()

        if selected_candidate == 1:
            self.voting_system.vote("1")
            messagebox.showinfo("Vote", "You voted for John.")
        elif selected_candidate == 2:
            self.voting_system.vote("2")
            messagebox.showinfo("Vote", "You voted for Jane.")
        else:
            messagebox.showerror("Error", "Please select a candidate before voting.")

    def show_results(self):
        """Displays voting results in a message box."""
        total_votes = self.voting_system.candidate1_votes + self.voting_system.candidate2_votes
        results_message = (
            f"John: {self.voting_system.candidate1_votes} votes\n"
            f"Jane: {self.voting_system.candidate2_votes} votes\n"
            f"Total Votes: {total_votes}"
        )
        messagebox.showinfo("Results", results_message)

if __name__ == "__main__":
    root = tk.Tk()
    voting_system = Voting_System()
    app = VotingApp(root, voting_system)
    root.mainloop()
