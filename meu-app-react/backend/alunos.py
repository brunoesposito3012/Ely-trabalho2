import pymysql
from db_config import connect_db
from flask import jsonify, request, Blueprint

alunos_bp = Blueprint("aluno", __name__)

@alunos_bp.route('/alunos', methods=['GET'])
def listar_alunos():
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aluno")
        rows = cursor.fetchall()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@alunos_bp.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    try:
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM aluno WHERE idaluno = %s", (id,))
        row = cursor.fetchone()
        if row:
            return jsonify(row), 200
        else:
            return jsonify({'message': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@alunos_bp.route('/alunos', methods=['POST'])
def inserir_aluno():
    try:
        aluno = request.json
        conn = connect_db()
        cursor = conn.cursor()
        sql = "INSERT INTO aluno (nome, idade, curso, matricula, email) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (aluno['nome'], aluno['idade'], aluno['curso'], aluno['matricula'], aluno['email']))
        conn.commit()
        return jsonify({'message': 'Aluno cadastrado com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@alunos_bp.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    try:
        aluno = request.json
        conn = connect_db()
        cursor = conn.cursor()
        sql = "UPDATE aluno SET nome = %s, idade = %s, curso = %s, matricula = %s, email = %s WHERE idaluno = %s"
        cursor.execute(sql, (aluno['nome'], aluno['idade'], aluno['curso'], aluno['matricula'], aluno['email'], id))
        conn.commit()
        return jsonify({'message': 'Aluno atualizado com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()

@alunos_bp.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM aluno WHERE idaluno = %s", (id,))
        conn.commit()
        return jsonify({'message': 'Aluno excluído com sucesso'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        conn.close()
