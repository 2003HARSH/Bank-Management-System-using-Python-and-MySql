# Bank Management System

This is a Bank Management System project using Python and Tkinter for the GUI and MySQL as the database. This application allows users to open accounts, check balances, deposit and withdraw money, and close accounts. Additionally, it provides an admin interface for viewing all account details.

## Preview
![](https://github.com/2003HARSH/Bank-Management-System-using-Python-and-MySql/blob/main/docs/static/1.jpg)
![](https://github.com/2003HARSH/Bank-Management-System-using-Python-and-MySql/blob/main/docs/static/2.jpg)
![](https://github.com/2003HARSH/Bank-Management-System-using-Python-and-MySql/blob/main/docs/static/3.jpg)
![](https://github.com/2003HARSH/Bank-Management-System-using-Python-and-MySql/blob/main/docs/static/4.jpg)

## Features

- **User Login**:
  - Open a new account
  - Deposit money
  - Withdraw money
  - Check balance
  - Close account

- **Admin Login**:
  - View all account details

## Prerequisites

- Python 3.x
- MySQL Server
- Tkinter library for Python
- MySQL Connector for Python

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
   cd bank-management-system
   ```

2. **Install the required libraries**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Create the database**:
   - Open MySQL command line or any MySQL client.
   - Create a database named `bank`:
     ```sql
     CREATE DATABASE bank;
     ```
   - Create the necessary tables:
     ```sql
     USE bank;
     CREATE TABLE ACCOUNT (
       ACNO INT PRIMARY KEY,
       NAME VARCHAR(100),
       DOB DATE,
       PHONE_NO VARCHAR(15),
       ADDRESS VARCHAR(255),
       OPENING_BALANCE INT
     );

     CREATE TABLE SECURED (
       ACNO INT PRIMARY KEY,
       PASSWORD VARCHAR(255)
     );
     ```

4. **Run the application**:
   ```bash
   python main.py
   ```
   OR
   ```bash
   python BANK MANAGEMENT.py
   ```

## Usage

### User Interface

1. **Open Account**:
   - Fill in the required details: Name, Account Number, Date of Birth, Phone Number, Opening Balance, Password, Address.
   - Click the "Submit" button to open the account.

2. **Deposit Amount**:
   - Enter the account number and amount to deposit.
   - Click the "Submit" button to deposit the amount.

3. **Withdraw Amount**:
   - Enter the account number, amount to withdraw, and password.
   - Click the "Submit" button to withdraw the amount.

4. **Check Balance**:
   - Enter the account number and password.
   - Click the "Submit" button to check the balance.

5. **Close Account**:
   - Enter the account number and password.
   - Click the "Submit" button to close the account.

### Admin Interface

1. **Admin Login**:
   - Enter the admin password.
   - If authenticated, click the "Show Data" button to view all account details.

## Code Explanation

The main functions are:

- `openAcc()`: Opens a new account.
- `checkBal()`: Checks the balance of an account.
- `closeAcc()`: Closes an account.
- `depoAmo()`: Deposits an amount into an account.
- `withAmo()`: Withdraws an amount from an account.
- `user_options()`: Provides user options.
- `admin_options()`: Provides admin options.
- `main()`: Main function to run the application.

Each function creates a new window using Tkinter's `Toplevel` widget and interacts with the MySQL database using `mysql.connector`.

## License

This project is licensed under the MIT License.

