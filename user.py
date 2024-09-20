from flask import Blueprint, request

user_blueprint = Blueprint("user", __name__)

@user_blueprint.route('/', methods=['GET'])
def get_user():
    user_id = request.args.get("id")
    # todo Получение пользователя по id из БД
    # todo Вернуть данные о пользователе
    return user_id or "Icnorrect user id"

@user_blueprint.route('/', methods=['POST'])
def register_user():
    pass