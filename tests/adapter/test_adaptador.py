# from app.infraestructura.adaptador.inmemory_vote_repository import (
#     InMemoryVoteRepository,
# )

from app.infraestructura.adaptador.mysql.adaptador_mysql import AdaptadorMysql
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto

# from app.dominio.modelo.vote import Vote


def test_vote_save():
    # vote = Vote()
    # vote_repository = InMemoryVoteRepository()
    adaptador = AdaptadorMysql()
    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)
    assert isinstance(adaptador, AdaptadorMysql)


#     assert vote.save(vote_repository).vote_id == vote.vote_id


# def test_vote_repository_all():
#     vote_repository = InMemoryVoteRepository()
#     vote1 = Vote().save(vote_repository)
#     vote2 = Vote().save(vote_repository)

#     assert set(vote_repository.all()) == {vote1, vote2}


# def test_vote_repository_total():
#     vote_repository = InMemoryVoteRepository()
#     Vote().save(vote_repository)
#     Vote().save(vote_repository)

#     assert vote_repository.total() == 2
