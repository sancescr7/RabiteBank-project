const search_button = document.querySelector('.header__search--button')
const search_input = document.querySelector('.header__search--input')
const headerDowloud = document.querySelector(".headerDowloud")
const dowloudOpen = document.querySelector('.dowloud-open')
const ofervlow = document.querySelector('.ofervlow ')

function togleSearch() {
    search_input.classList.toggle("search-active")
    search_button.classList.toggle('search-border')
}
search_button.addEventListener("click",togleSearch)

function openMenu() {
    ofervlow.classList.toggle('hidden')
    headerDowloud.classList.toggle('hidden')
}
ofervlow.addEventListener("click",()=>{
    ofervlow.classList.add("hidden")
    headerDowloud.classList.add('hidden')
})
dowloudOpen.addEventListener("click",openMenu)






const sticky = document.querySelector(".sticky");

function Scrool() {
    const verticalScroll = window.scrollY;
    if (verticalScroll > 30) {
        sticky.classList.add("is-sticky")
    }
    else{
        sticky.classList.remove("is-sticky")
    }
}
window.addEventListener('scroll',Scrool)


