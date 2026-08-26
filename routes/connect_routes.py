from flask import Blueprint

from controllers.connect_controller import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario,
    atualizar_usuario,
    remover_usuario
)


connect_routes = Blueprint("connect", __name__)


connect_routes.route(
    "/usuarios",
    methods=["POST"]
)(cadastrar_usuario)


connect_routes.route(
    "/usuarios",
    methods=["GET"]
)(listar_usuarios)


connect_routes.route(
    "/usuarios/<int:id>",
    methods=["GET"]
)(buscar_usuario)


connect_routes.route(
    "/usuarios/<int:id>",
    methods=["PUT"]
)(atualizar_usuario)


connect_routes.route(
    "/usuarios/<int:id>",
    methods=["DELETE"]
)(remover_usuario)
