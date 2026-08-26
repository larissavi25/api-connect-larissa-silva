from flask import request, jsonify

from data.connect_data import usuarios, gerar_id


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Os dados do usuário são obrigatórios."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    if not nome:
        return jsonify({
            "error": "O campo nome é obrigatório."
        }), 400

    if not email:
        return jsonify({
            "error": "O campo email é obrigatório."
        }), 400

    usuario = {
        "id": gerar_id(),
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)

    return jsonify({
        "data": usuario
    }), 201


def listar_usuarios():
    return jsonify(usuarios), 200


def buscar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    return jsonify({
        "data": usuario
    }), 200


def atualizar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Os dados para atualização são obrigatórios."
        }), 400

    if "nome" in dados:
        usuario["nome"] = dados["nome"]

    if "email" in dados:
        usuario["email"] = dados["email"]

    return jsonify({
        "data": usuario
    }), 200


def remover_usuario(id):
    indice = next(
        (i for i, usuario in enumerate(usuarios) if usuario["id"] == id),
        None
    )

    if indice is None:
        return jsonify({
            "error": "Usuário não encontrado."
        }), 404

    usuarios.pop(indice)

    return "", 204
