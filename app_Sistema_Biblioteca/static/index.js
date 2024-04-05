function filtrarLivro (filtro) {
    livros = document.getElementsByClassName('livro');

    for (i = 0; i < livros.length; i++) {
        livros[i].style.display = "flex";
    }
    
    valor = filtro.getElementsByTagName('select')[0].value


    input = filtro.getElementsByTagName('input')[0].value.toLowerCase()

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
            /*
        case '3':
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('lancamento')[0].innerHTML.toLowerCase().slice(12) > livros[j + 1].getElementsByClassName('lancamento')[0].innerHTML.toLowerCase().slice(12)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('lancamento')[0].innerHTML.toLowerCase().slice(12) < livros[j + 1].getElementsByClassName('lancamento')[0].innerHTML.toLowerCase().slice(12)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;

        case '4':
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('notaMedia')[0].innerHTML.toLowerCase().slice(12) > livros[j + 1].getElementsByClassName('notaMedia')[0].innerHTML.toLowerCase().slice(12)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('notaMedia')[0].innerHTML.toLowerCase().slice(12) < livros[j + 1].getElementsByClassName('notaMedia')[0].innerHTML.toLowerCase().slice(12)) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;
            */

        case 3:
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('lancamento')[0].innerHTML > livros[j + 1].getElementsByClassName('lancamento')[0].innerHTML) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (livros[j].getElementsByClassName('lancamento')[0].innerHTML < livros[j + 1].getElementsByClassName('lancamento')[0].innerHTML) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;

        case 4:
            if (ordem == '0') {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (parseFloat(livros[j].getElementsByClassName('notaMedia')[0].innerHTML.slice(12)) > parseFloat(livros[j + 1].getElementsByClassName('notaMedia')[0].innerHTML.slice(12))) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            } else {
                for (i = 0; i < livros.length; i++) {
                    for (j = 0; j < livros.length - 1; j++) {
                        if (parseFloat(livros[j].getElementsByClassName('notaMedia')[0].innerHTML.slice(12)) < parseFloat(livros[j + 1].getElementsByClassName('notaMedia')[0].innerHTML.slice(12))) {
                            livros[j].parentNode.insertBefore(livros[j + 1], livros[j]);
                        }
                    }
                }
            }
            break;

    }
}
