from flask import Blueprint, request

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route('/', methods=['GET'])
def get_user():
    user_id = request.args.get("id")
    # todo Получение пользователя по id из БД
    # todo Вернуть данные о пользователе
    return user_id or "Incorrect user id"

@user_blueprint.route('/', methods=['DELETE'])
def delete_user():
    pass

@user_blueprint.route('/', methods=['POST'])
def register_user():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        # todo Запись данных в БД
        return "Success"
    return 'Content-Type not supported!'