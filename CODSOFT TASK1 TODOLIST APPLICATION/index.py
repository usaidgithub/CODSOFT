from flask import Flask, request, jsonify
import pymysql.cursors
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1234',
                             database='todolist',
                             cursorclass=pymysql.cursors.DictCursor
                             )
@app.route('/add_record',methods=['POST'])
def add_record():
    if request.method=='POST':
        try:
            data = request.get_json() 
            records = data['records']
            with connection.cursor() as cursor:
                sql = "INSERT INTO records (records) VALUES (%s)"
                cursor.execute(sql, (records,))
            connection.commit()
            return jsonify({'message': 'Record added successfully'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
@app.route('/get_records',methods=['GET'])
def get_records():
    if request.method=='GET':
        try:
           with connection.cursor() as cursor:
            sql = "SELECT * FROM records"
            cursor.execute(sql)
            result = cursor.fetchall()
            return jsonify(result), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
@app.route('/delete_record/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    if request.method == 'DELETE':
        try:
            with connection.cursor() as cursor:
                sql = "DELETE FROM records WHERE id = %s"
                cursor.execute(sql, (record_id,))
            connection.commit()
            return jsonify({'message': "Record deleted successfully"}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
@app.route('/update_record',methods=['POST'])
def update_record():
    if request.method=='POST':
        id=request.form.get('id')
        print(f"The id is {id}")
        updated_record=request.form.get('update_value')
        print(f"The updated record is {updated_record}")
        try:
            with connection.cursor() as cursor:
                sql = "UPDATE records SET records=%s WHERE id=%s"
                cursor.execute(sql, (updated_record,id,))
            connection.commit()
            return jsonify({'message': "Record updated successfully"}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500





if __name__=='__main__':
    app.run(debug=True)
