from datetime import date, datetime


class StepCounter:
    def __init__(self):
        self.date = date.today()
        self.steps = 0

    def add_steps(self, amount):
        self.steps += amount

    def total_steps(self):
        now = datetime.now()
        return f'{now.strftime("%H:%M:%S")} - {self.date.strftime("%d.%m.%Y")}: {self.steps} Steps taken'

    def save_data(self, file_path='stepcounterdata.txt'):
        with open(file_path, 'a') as file:
            now = datetime.now()
            file.write(f'{now.strftime("%H:%M:%S")} - {self.date.strftime("%d.%m.%Y")}: {self.steps}\n')

    @classmethod
    def load_data_from_file(cls, file_path='stepcounterdata.txt'):
        step_counter_list = []
        with open(file_path, 'r') as file:
            for line in file:
                time_str, rest = line.strip().split(' - ')
                date_str, steps_text = rest.strip().split(': ')
                date = datetime.strptime(date_str, "%d.%m.%Y").date()
                steps = int(steps_text.split()[0])
                step_counter = cls()
                step_counter.date = date
                step_counter.steps = steps
                step_counter_list.append(step_counter)
        return step_counter_list


# User input for the number of steps walked
def user_input_steps():
    while True:
        try:
            steps = int(input("Enter the number of steps walked: "))
            return steps
        except ValueError:
            print("Please enter a valid integer.")


# Function for user input whether to end the program
def user_input_exit_program():
    response = input("Do you want to end the program? (yes/no): ").lower()
    return response == "yes"


# Example of Usage
if __name__ == "__main__":
    step_counter1 = StepCounter()
    exit_program = False

    while not exit_program:
        # User input for the number of steps walked
        new_steps = user_input_steps()

        # Add steps
        step_counter1.add_steps(new_steps)

        # Display total number of steps walked for the day
        print(step_counter1.total_steps())

        # Save data to the file
        step_counter1.save_data()

        # User input whether to end the program
        exit_program = user_input_exit_program()
