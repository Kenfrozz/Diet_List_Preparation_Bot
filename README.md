# Diet List Preparation Bot

This Python program is used by dietitians to prepare special diet lists for their clients. The program finds and creates the most appropriate diet list based on the client's height, weight, age and number of meals and saves it to a file with the specified information.

## Usage

The program uses a user interface. After entering the client's name, number of meals, weight, height and age, the user starts the process by clicking the "Calculate" button.

### Required Libraries

- `tkinter`: To create a user interface.
- `openpyxl`: For manipulating Excel files.
- `random`: To generate random values.
- `os`: For file operations and operating system operations.
- `datetime`: For date and time operations.
- `docx`: For creating and editing Word files.

## How to Use

1. Run the program.
2. Enter the client's name, number of meals, weight, height and age.
3. Click on the "Calculate" button.
4. The program generates the appropriate diet list for the client and saves it to the file.

## Developer Notes

For this program to work, there must be predetermined diet lists. These lists should be divided into folders according to the number of meals and named according to a specific order.

My project includes a Python program that I wrote to make it easier for dietitians to prepare special diet lists for their clients. This program makes fine calculations based on the user's height, weight, age, and number of meals, and selects the most appropriate one among the pre-created diet lists and saves it in the diet file where the client's information is saved.

For the program to work, there must be predetermined weekly diet lists. These lists will be divided into two classes according to the number of meals: 2-meal and 3-meal. Within each class, there will be folders for each for at least 2 months. Each month's folder name will include folders containing BMI classes: 21-25 BMI, 26-29 BMI, 30-33 BMI, 34-37 BMI and above. Within these folders, there will be 4 different weekly diet lists.

For example, the folder sequence will be as follows: DIETS\THREE_MEAL_DIETS\AY2\21_25bmi\1.week.docx or DIETS\TWO_MEAL_DIETS\AY2\26_29bmi\4.week.docx.

After the diet lists are prepared, the program finds the most appropriate diet according to the client information entered, creates and saves the list with the client's information.
