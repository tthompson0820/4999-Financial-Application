#start here

from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="Senior",
    password="your_password",
    database="your_database"
)

cursor = db.cursor()

# Initialize the users table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                  id INT AUTO_INCREMENT PRIMARY KEY,
                  username VARCHAR(255) UNIQUE,
                  password VARCHAR(255),
                  balance FLOAT DEFAULT 0)''')
db.commit()

# Endpoints
# Account Balance Inquiry
@app.route('/balance/<int:user_id>', methods=['GET'])
def get_balance(user_id):
    cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify({'balance': user[3]})
    else:
        return jsonify({'error': 'User not found'}), 404

# Transaction History View
@app.route('/transactions/<int:user_id>', methods=['GET'])
def get_transactions(user_id):
    cursor.execute('SELECT * FROM users WHERE id=%s', (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify({'transactions': []})  # Placeholder for transaction history
    else:
        return jsonify({'error': 'User not found'}), 404

# Funds Transfer
@app.route('/transfer', methods=['POST'])
def transfer_funds():
    data = request.get_json()
    sender_id = data.get('sender_id')
    recipient_id = data.get('recipient_id')
    amount = data.get('amount')

    cursor.execute('SELECT * FROM users WHERE id=%s', (sender_id,))
    sender = cursor.fetchone()
    cursor.execute('SELECT * FROM users WHERE id=%s', (recipient_id,))
    recipient = cursor.fetchone()

    if sender and recipient:
        if sender[3] >= amount:
            # Update sender's balance
            cursor.execute('UPDATE users SET balance=%s WHERE id=%s', (sender[3] - amount, sender_id))
            # Update recipient's balance
            cursor.execute('UPDATE users SET balance=%s WHERE id=%s', (recipient[3] + amount, recipient_id))
            # Commit changes to the database
            db.commit()
            return jsonify({'message': 'Transfer successful'}), 200
        else:
            return jsonify({'error': 'Insufficient funds'}), 400
    else:
        return jsonify({'error': 'Sender or recipient not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
