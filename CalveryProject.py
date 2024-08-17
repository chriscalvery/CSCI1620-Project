from VotingSystem import Voting_System
from gui import VotingApp
import tkinter as tk

def main():
    # Initialize the main Tkinter window
    root = tk.Tk()

    # Create an instance of the Voting_System
    voting_system = Voting_System()  # Use correct class name

    # Create an instance of the VotingApp GUI and pass the Voting_System instance to it
    app = VotingApp(root, voting_system)  # Ensure variable names match

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
