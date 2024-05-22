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

let currentNumber = generateRandomFiveDigitNumber();

function generateRandomFiveDigitNumber() {
    return Math.floor(10000 + Math.random() * 90000);
}

const input = document.querySelector('.SubmiteForm input')
function getNextNumber() {
    alert(currentNumber++); 
}
input.addEventListener('click',getNextNumber)


// getText("https://www.cbar.az/currencies/13.07.2023.xml");

// async function getText(file) {
//   let x = await fetch(file);
//   console.log(x);;
 
// }

