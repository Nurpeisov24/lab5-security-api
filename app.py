import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Временное хранилище в памяти для демонстрации
users = []


@app.route('/api/users', methods=['GET'])
def get_users():
  return jsonify(users), 200


@app.route('/api/users', methods=['POST'])
def create_user():
  data = request.json
  if not data or 'name' not in data:
    return jsonify({'error': 'Invalid data'}), 400

  user = {'id': len(users) + 1, 'name': data['name']}
  users.append(user)
  return jsonify(user), 201


@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  global users
  user_exists = any(u['id'] == user_id for u in users)
  if not user_exists:
    return jsonify({'error': 'User not found'}), 404

  users = [u for u in users if u['id'] != user_id]
  return jsonify({'message': 'User deleted successfully'}), 200


if __name__ == '__main__':
  # Безопасный запуск без жесткого включения debug=True
  debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
  app.run(debug=debug_mode, host='127.0.0.1', port=5000)
