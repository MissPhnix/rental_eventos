drop table if exists usuario;
drop table if exists equipamento;
drop table if exists movimentacao;

create table usuario (
    id integer primary key autoincrement,
    nome text not null,
    email text not null unique,
    senha text not null,
    cpf text not null unique.
);

create table equipamento (
    id integer primary key autoincrement,
    marca text not null,
    modelo text not null,
    categoria text not null,
    potencia text,
    material text not null,
    peso integer not null,
    dimensoes text not null,
    cor text not null,
    quantidade integer not null
);

create table movimentacao (
    id integer primary key autoincrement,
    equipamento_id integer not null,
    usuario_id integer not null,
    data_movimento date not null,
    tipo text not null,
    foreign key (equipamento_id) references equipamento(id),
    foreign key (usuario_id) references usuario(id)
);

insert into usuario(nome, data_nascimento, email, senha, cpf) values ('Andressa de Souza', '2009-01-31', 'email@teste.com', 'senha123', '01234567890'), ('Ana Maria', '2008-07-07', 'teste@email.com', 'senha321', '25687412398'), ('Vinicius de Moraes', '1996-05-09', 'email@email.com', '123senha', '14587896532');
insert into equipamento(marca, modelo, categoria, potencia, material, peso, dimensoes, cor, quantidade) values ('Epson', 'Projetor PowerLite X49', 'Eletronico', '3600 Lumens', 'metal', 3, '302mmx87mmx249mm', 'branco', 20), ('Tiffany', 'Cadeira Branca', 'Mobilia', 'cadeira', 'madeira', 3, '87cmx39cmx40cm', 'branca', 17), ('Móveis Britz', 'Mesa Branca', 'Mobília', 'mesa', 'madeira', 5, '73cmx73cmx123cm','branca', 30);
insert into movimentacao(equipamento_id, usuario_id, data_movimento, tipo) values (1, 2, '2026-01-30 10:00:00', 'saída'), (1, 3, '2026-03-04 11:00:00', 'entrada'), (3, 2, '2026-07-08 12:00:00', 'entrada');