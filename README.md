# Banking Application

This Banking Application is a graphical user interface (GUI) implemented in Python using the Tkinter library. It provides basic banking functionalities such as checking balance, transferring funds, viewing transaction history, and creating new user accounts.

## Features

- Login System: Users are required to enter their username and password to access the application. Only users with valid credentials stored in the users.txt file can log in successfully.

- Main Window: After successful login, users are presented with a main window where they can perform various banking operations.

- Check Balance: Users can check their account balance by entering their user ID.

- Transfer Funds: Users can transfer funds to another user by specifying the recipient's user ID and the amount to transfer. It includes error handling for insufficient funds.

- Transaction History: Users can view their transaction history by entering their user ID.

- Create User (Admin): An admin user (username: "Admin") has the ability to create new user accounts with a specified initial balance.

## File Structure

- final_code.py: Contains the main Python script implementing the GUI application.

- assets/: Directory containing images used for buttons in the application.

- users.txt: Text file storing user data in the format user_id,username,password,balance.

- transactions.txt: Text file storing transaction history in the format sender_id,recipient_id,amount.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### Prerequisites

- Python 3.10.0
- Tkinter (usually included with Python installation)
- Pillow = pip install pillow
- Customtkinter = pip install customtkinter

#### Installation

1. Clone the repository:
https://github.com/tthompson0820/4999-Financial-Application.git

2. Navigate to the project directory:
cd 4999-Financial-Application

3. Run the application:
python final_code.py

## Usage

1. Login: Upon running the script, the login window will appear. Enter your username and password to log in.

2. Main Window: After successful login, you'll be presented with the main window of the banking application.

3. Perform Banking Operations:

- Check Balance: Click on the "Check Balance" button and enter your user ID to view your account balance.
- Transfer Funds: Click on the "Transfer Funds" button to transfer funds to another user. Enter the recipient's user ID and the amount to transfer.
- Transaction History: Click on the "Transaction History" button to view your transaction history. Enter your user ID.
- Create User (Admin): If logged in as an admin user (username: "Admin"), you'll have access to the "Create User" button. Click on it to create a new user account with a specified initial balance.

4. Log Out: To exit the application, simply close the main window.

