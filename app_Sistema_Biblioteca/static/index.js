
/*                    <div class="filtroLivros">
            <label for="filtro">Filtrar por:</label>
            <select id="filtro" onchange="filtrarLivro(parentElement)" class="escolha">
                <option value="titulo">titulo</option>
                <option value="autor">autor</option>
                <option value="gênero">gênero</option>
            </select> <select name="genero" id="generoFiltro" style="display: none;" onchange="filtrarLivro(parentElement)">
                <option value="Ação" {% if livro.genero == 'Ação' %} selected {% endif %}>Ação</option>
                <option value="Aventura" {% if livro.genero == 'Aventura' %} selected {% endif %}>Aventura</option>
                <option value="Comédia" {% if livro.genero == 'Comédia' %} selected {% endif %}>Comédia</option>
                <option value="Drama" {% if livro.genero == 'Drama' %} selected {% endif %}>Drama</option>
                <option value="Ficção Científica" {% if livro.genero == 'Ficção Científica' %} selected {% endif %}>Ficção Científica</option>
                <option value="Romance" {% if livro.genero == 'Romance' %} selected {% endif %}>Romance</option>
                <option value="Terror" {% if livro.genero == 'Terror' %} selected {% endif %}>Terror</option>
            </select>
            <input type="text" id="filtroTexto" onkeyup="filtrarLivro(parentElement)" class="digitado">*/

function filtrarLivro (filtro) {
    livros = document.getElementsByClassName('livro');

    for (i = 0; i < livros.length; i++) {
        livros[i].style.display = "flex";
    }
    
    valor = filtro.getElementsByClassName('escolha')[0].value

    if (valor == 'gênero') { 
        document.getElementById('generoFiltro').style.display      = "inline-block";
        document.getElementsByClassName('digitado')[0].style.display = "none";
        input = document.getElementById('generoFiltro').value.toLowerCase()
    } else {
        document.getElementById('generoFiltro').style.display        = "none";
        document.getElementById('filtroTexto').style.display         = "inline-block";
        input = document.getElementsByClassName('digitado')[0].value.toLowerCase()
    }

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