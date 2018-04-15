from flask import jsonify, Flask, request
import sqlite3
app = Flask(__name__)

languages = [{'name': 'JS'}, {'name': 'Python'}, {'name': 'Python'}]
rooms = [{"id":1, "name":"First room"}, {"id":2, "name":"Second room"}]
users = [{"name":"Vitya", "SurName":"Shpigunov", "NumberOfRooms":5}, {"name":"Nick", "SurName":"Vinok", "NumberOfRooms":1}]

@app.route('/room/<int:id>', methods = ["GET"])
def getRoomItems(id):
    roos = [room for room in rooms if room["id"]]
    return jsonify({"room":roos[0]})

@app.route('/user/<string:login>', methods = ["GET"])
def getUsersData(login):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute('SELECT * from User Where login = ?', (login, ))
    data = [row for row in cur]
    return jsonify({"User": data[0]})

@app.route('/user/id', methods = ["POST"])
def test(id):
    conn = sqlite3.connect('db.db')
    cur = conn.cursor()
    cur.execute('SELECT UserArt.user_id, UserArt.art_id, UserRoom.user_id, UserRoom.room_id from UserArt, UserRoom where UserRoom.room_id ')
    language = {'name' : request.json['name']}
    languages.append(language)
    return jsonify({'languages':languages})


if __name__ == '__main__':
    app.run(debug=True, port = 8080)