class Voting_System:
    def __init__(self):
        self.candidate1_votes = 0
        self.candidate2_votes = 0

    def vote_menu(self) -> str:
        """Displays the voting menu and returns the user's choice."""
        print('-' * 34)
        print('VOTE MENU')
        print('-' * 34)
        print('v: Vote')
        print('x: Exit')
        choice = input('Option: ').lower().strip()
        while choice not in ['v', 'x']:
            choice = input('Invalid (v/x): ').lower().strip()
        return choice

    def candidate_menu(self) -> str:
        """Displays the candidate menu and returns the user's vote."""
        print('-' * 34)
        print('CANDIDATE MENU')
        print('-' * 34)
        print('1: John')
        print('2: Jane')
        vote = input('Candidate: ').strip()
        while vote not in ['1', '2']:
            vote = input('Invalid (1/2): ').strip()
        return vote

    def vote(self, candidate: str) -> None:
        """Increments the vote count for the selected candidate."""
        if candidate == '1':
            print('Voted John')
            self.candidate1_votes += 1
        elif candidate == '2':
            print('Voted Jane')
            self.candidate2_votes += 1

    def display_results(self) -> None:
        """Displays the current vote totals for each candidate."""
        total_votes = self.candidate1_votes + self.candidate2_votes
        print('-' * 34)
        print(f'John - {self.candidate1_votes}, Jane - {self.candidate2_votes}, Total - {total_votes}')
        print('-' * 34)

    def run(self) -> None:
        """Runs the main voting loop."""
        while True:
            menu_choice = self.vote_menu()
            if menu_choice == 'v':
                vote_choice = self.candidate_menu()
                self.vote(vote_choice)
            elif menu_choice == 'x':
                self.display_results()
                break
