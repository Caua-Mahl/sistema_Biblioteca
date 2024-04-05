function filtrarLivro (filtro) {
    livros = document.getElementsByClassName('livro');

    for (i = 0; i < livros.length; i++) {
        livros[i].style.display = "flex";
    }
    
    valor = filtro.getElementsByClassName('escolha')[0].value

    input = filtro.getElementsByClassName('digitado')[0].value.toLowerCase()

    switch (valor) {
        case 'titulo':
            for (i = 0; i < livros.length; i++) {
                if (livros[i].getElementsByClassName(valor)[0].innerHTML.toLowerCase().indexOf(input) == -1) {
                    livros[i].style.display = "none";
                }
            }
            break;
        
        case 'autor':
            for (i = 0; i < livros.length; i++) {
                if (livros[i].getElementsByClassName(valor)[0].innerHTML.toLowerCase().slice(8).indexOf(input) == -1) {
                    livros[i].style.display = "none";
                }
            }
            break;

        case 'gênero':
            for (i = 0; i < livros.length; i++) {
                if (livros[i].getElementsByClassName(valor)[0].innerHTML.toLowerCase().slice(8).indexOf(input) == -1) {
                    livros[i].style.display = "none";
                }
            }
            break;
    }
}

function ordenarLivro() {
    ordem    = document.getElementById('ordem').value
    ordenado = document.getElementById('ordenado').value
    livros   = document.getElementsByClassName('livro');

    switch (ordenado) {
        case '0':
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('titulo')[0].innerHTML.toLowerCase() > livros[j + 1].getElementsByClassName('titulo')[0].innerHTML.toLowerCase()) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('titulo')[0].innerHTML.toLowerCase() < livros[j + 1].getElementsByClassName('titulo')[0].innerHTML.toLowerCase()) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;

        case '1':
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('autor')[0].innerHTML.toLowerCase().slice(8) > livros[j + 1].getElementsByClassName('autor')[0].innerHTML.toLowerCase().slice(8)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('autor')[0].innerHTML.toLowerCase().slice(8) < livros[j + 1].getElementsByClassName('autor')[0].innerHTML.toLowerCase().slice(8)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;

        case '2':
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('gênero')[0].innerHTML.toLowerCase().slice(8) > livros[j + 1].getElementsByClassName('gênero')[0].innerHTML.toLowerCase().slice(8)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('gênero')[0].innerHTML.toLowerCase().slice(8) < livros[j + 1].getElementsByClassName('gênero')[0].innerHTML.toLowerCase().slice(8)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;
    }
}

/*  
{% extends "layouts/base.html" %}
{% block title %}Resenhar Livro{% endblock %}
{% block content %}
    <h1>{{ livro.titulo }}</h1>
    {% if erro %}
        <p class="aviso">{{ erro }}</p>
    {% endif %}
    {% if sucesso %} 
        <p class="aviso">{{ sucesso }}</p>
    {% endif %}
    <div class="livroOpcoes">
        <form action="{% url 'resenha' %}" method="post">
            {% csrf_token %}
            <input type="hidden" name="livro" value="{{ livro.id }}">
            <input type="hidden" name="id" value="{{ resenha.id }}">
            <textarea type="text"   name="resenha" id="resenha" placeholder="Resenha" required>
                {% if resenha %}
                    {{ resenha.resenha }}
                {% endif %}
            </textarea>
            <input type="submit" value="Resenhar" class="botao">
        </form>

        <form action="{% url 'avaliarLivro' %}" method="post" class="livrosNota">
            {% csrf_token %}
            <input type="hidden" name="livro" value="{{ livro.id }}">
            {% if avaliacao %}
                <input type="hidden" name="id" value="{{ avaliacao.id }}">
                <label for="nota">Nota:</label>
                <select name="nota" id="nota" required>
                    <option value="0" {% if avaliacao.nota == 0 %}selected{% endif %}>0</option>
                    <option value="1" {% if avaliacao.nota == 1 %}selected{% endif %}>1</option>
                    <option value="2" {% if avaliacao.nota == 2 %}selected{% endif %}>2</option>
                    <option value="3" {% if avaliacao.nota == 3 %}selected{% endif %}>3</option>
                    <option value="4" {% if avaliacao.nota == 4 %}selected{% endif %}>4</option>
                    <option value="5" {% if avaliacao.nota == 5 %}selected{% endif %}>5</option>
                </select>
            {% else %}
                <label for="nota">Nota:</label>
                <select name="nota" id="nota" required>
                    <option value="0">0</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            {% endif %}
            <input type="submit" value="Avaliar" class="botao">
        </form>
    </div>

    <div class="filtroAluno">
        <label for="filtro">Filtrar Aluno:</label>
        <input type="text" id="filtroTexto" onkeyup="filtrarAluno()" class="digitado">
        <div>
            <label for="">Esconder Não Resenhados:</label>
            <input type="checkbox" id="esconder" onclick="esconderNaoResenhados()">
        </div>
        <div>
            <label for="">Esconder Não Avaliados:</label>
            <input type="checkbox" id="esconderAvaliacao" onclick="esconderNaoAvaliados()">
        </div>

    </div>
    <div class="ordenacao">
        <label for="ordenado">Ordenar por:</label>
        <select id="ordenado" onchange="ordenar()">
            <option value="0">Aluno</option>
            <option value="1">Nota</option>
        </select>

        <label for="ordem">Ordem:</label>
        <select id="ordem" onchange="ordenar()">
            <option value="0">Crescente</option>
            <option value="1">Decrescente</option>
        </select>
    </div>

    <div class="livroTodas">
        {% for usuario in usuarios %}
            {% if usuario.resenha != None  or usuario.nota != None %}
                <div class="livroTodasUsuario">
                    <h2 class="aluno">{{ usuario.nome }}</h2>
                    <div class="livroTodasUsuarioResenha">
                        <p>Resenha: </p>
                        {% if usuario.resenha %}
                            <div name="resenha" id="resenha" contenteditable="false" readonly >{{ usuario.resenha }}</div>
                        {% else %}
                            <div name="resenha" id="resenha" contenteditable="false" readonly style="background-color: red; text-align: center;" class="semResenha">Ainda não resenhou, apenas avaliou!</div>
                        {% endif %}
                    </div>
                    <div class="livroTodasUsuarioNota">
                        <p>Nota:</p>
                        {% if usuario.nota != None %}
                            <p>{{ usuario.nota }}</p>
                        {% else %}
                            <p class="semNota"> N/A</p>
                        {% endif %}
                    </div>
                </div>
            {% endif %}
        {% endfor %}
    </div>
{% endblock %}





*/

function filtrarAluno() {
    alunos = document.getElementsByClassName('livroTodasUsuario');

    for (i = 0; i < alunos.length; i++) {
        alunos[i].style.display = "flex";
    }

    input = document.getElementById('filtroTexto').value.toLowerCase()

    for (i = 0; i < alunos.length; i++) {
        if (alunos[i].getElementsByClassName('aluno')[0].innerHTML.toLowerCase().indexOf(input) == -1) {
            alunos[i].style.display = "none";
        }
    }
}

function esconderNaoResenhados() {
    alunos = document.getElementsByClassName('livroTodasUsuario');

    if (document.getElementById('esconder').checked) {
        for (i = 0; i < alunos.length; i++) {
            if (alunos[i].getElementsByClassName('semResenha').length != 0) {
                alunos[i].style.display = "none";
            }
        }
    } else {
        for (i = 0; i < alunos.length; i++) {
            if (alunos[i].getElementsByClassName('semResenha').length != 0) {
                alunos[i].style.display = "flex";
            }
        }
    }
}

function esconderNaoAvaliados() {
    alunos = document.getElementsByClassName('livroTodasUsuario');

    if (document.getElementById('esconderAvaliacao').checked) {
        for (i = 0; i < alunos.length; i++) {
            if (alunos[i].getElementsByClassName('semNota').length != 0) {
                alunos[i].style.display = "none";
            }
        }
    } else {
        for (i = 0; i < alunos.length; i++) {
            if (alunos[i].getElementsByClassName('semNota').length != 0) {
                alunos[i].style.display = "flex";
            }
        }
    }
}

function ordenar() {
    ordem    = document.getElementById('ordem').value
    ordenado = document.getElementById('ordenado').value
    alunos   = document.getElementsByClassName('livroTodasUsuario');

    switch (ordenado) {
        case '0':
            if (ordem == '0') {
                for (i = 0; i < alunos.length; i++) {
                    for (j = 0; j < alunos.length - 1; j++) {
                        if (alunos[j].getElementsByClassName('aluno')[0].innerHTML.toLowerCase() > alunos[j + 1].getElementsByClassName('aluno')[0].innerHTML.toLowerCase()) {
                            alunos[j].parentNode.insertBefore(alunos[j + 1], alunos[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < alunos.length; i++) {
                    for (j = 0; j < alunos.length - 1; j++) {
                        if (alunos[j].getElementsByClassName('aluno')[0].innerHTML.toLowerCase() < alunos[j + 1].getElementsByClassName('aluno')[0].innerHTML.toLowerCase()) {
                            alunos[j].parentNode.insertBefore(alunos[j + 1], alunos[j]);
                        }
                    }
                }
            }
            break;

        case '1':
            if (ordem == '0') {
                for (i = 0; i < alunos.length; i++) {
                    for (j = 0; j < alunos.length - 1; j++) {
                        if (alunos[j].getElementsByClassName('livroTodasUsuarioNota')[0].innerHTML.toLowerCase() > alunos[j + 1].getElementsByClassName('livroTodasUsuarioNota')[0].innerHTML.toLowerCase()) {
                            alunos[j].parentNode.insertBefore(alunos[j + 1], alunos[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < alunos.length; i++) {
                    for (j = 0; j < alunos.length - 1; j++) {
                        if (alunos[j].getElementsByClassName('livroTodasUsuarioNota')[0].innerHTML.toLowerCase() < alunos[j + 1].getElementsByClassName('livroTodasUsuarioNota')[0].innerHTML.toLowerCase()) {
                            alunos[j].parentNode.insertBefore(alunos[j + 1], alunos[j]);
                        }
                    }
                }
            }
            break;
    }
}