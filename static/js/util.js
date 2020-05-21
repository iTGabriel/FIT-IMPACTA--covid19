// Callback para controlar o botão de atalho para o fim da página ou para o topo com base em click
var scroll = document.getElementById('scroll_trigger');
document.getElementById('scroll_trigger').addEventListener('click', () => {
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

// Callback para controlar o botão de atalho para o fim da página ou para o topo com base no scroll
window.addEventListener('scroll', () => {
    if(document.body.scrollTop > 200){
        scroll.children[0].setAttribute('href', '#endtable');
        scroll.classList.add('scroll_up');
        scroll.classList.remove('scroll_down');
    }else{
        
        scroll.children[0].setAttribute('href', '#bkns');
        scroll.classList.add('scroll_down');
        scroll.classList.remove('scroll_up');
    }
});