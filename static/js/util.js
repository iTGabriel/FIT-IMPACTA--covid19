// Callback para controlar o botão de atalho para o fim da página ou para o topo
document.getElementById('scroll').addEventListener('click', function scroll_move() {
    let scroll = document.getElementById('scroll');
    let scroll_href = scroll.children[0].getAttribute('href');

    if (scroll_href != '#endtable') {
        scroll.children[0].setAttribute('href', '#endtable');
        scroll.classList.add('scroll_up');
        scroll.classList.remove('scroll_down');
    } else {
        scroll.children[0].setAttribute('href', '#bkns');
        scroll.classList.add('scroll_down');
        scroll.classList.remove('scroll_up');
    };
});

// Callback para verificar se o THEAD esta no topo da página e então prover atalho 
// var header = document.getElementById('scroll_tr');
// var sticky = header.offsetTop;

// if (window.pageYOffset > sticky) {
//     scroll_up.removeAttribute('style');
//     scroll_down.setAttribute('style', 'display:none');
// } else {
//     scroll_up.setAttribute('style', 'display:none');
//     scroll_down.setAttribute('style', 'display:block');
// }