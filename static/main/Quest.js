// const products = [
//     { day:"21 June",
//     name:"Bahar kampaniyası",
//     title:"Müştərilərimizə arzularını rahatlıqla gerçəkləşdirmək üçün nağd pul krediti üzrə 'Bahar kampaniyası' təklif edirik. 🌸",
//     category: 'Loans',
//     Image:"static/img/campaniya1.webp"
// },
//     { day:"16 Octobers",
//     name:"Bahar kampaniyası",
//     title:"Müştərilərimizə arzularını rahatlıqla gerçəkləşdirmək üçün nağd pul krediti üzrə 'Bahar kampaniyası' təklif edirik. 🌸",
//     category: 'Loans',
//     Image:"static/img/campaniya2.webp" 
// },
//     { day:"25 June",
//     name:"Bahar kampaniyası",
//     title:"Müştərilərimizə arzularını rahatlıqla gerçəkləşdirmək üçün nağd pul krediti üzrə 'Bahar kampaniyası' təklif edirik. 🌸",
//     category: 'Deposits',
//     Image:"static/img/campaniya3.webp" 
// }
// ];

// function filterProducts(category) {
//     const buttons = document.querySelectorAll('.category-btn');
//     buttons.forEach(btn => {
//         if (btn.getAttribute("data-category") === category) {
//             btn.classList.add('active');
//         } else {
//             btn.classList.remove('active');
//         }
//     });


//     const filteredProducts = category === 'all' ? products : products.filter(product => product.category === category);
    
//     displayProducts(filteredProducts);
// }

// function displayProducts(products) {
//     const productList = document.querySelector('.productList');
//     productList.innerHTML = '';
    
//     products.forEach(product => {
//         const li = document.createElement('li');
        
//         const link = document.createElement('a')
//         link.classList.add("productList__Item")
//         link.href = "./CampaignsItem.html"
//         const left = document.createElement('div')
//         left.classList.add('productList__Item--left')
//         const span_date = document.createElement('span')
//         span_date.textContent = product.day
//         const name_product = document.createElement('h3')
//         name_product.textContent = product.name
//         const title = document.createElement("p")
//         title.textContent = product.title
//         left.appendChild(span_date)
//         left.appendChild(name_product)
//         left.appendChild(title)
//         link.appendChild(left)
//         // start right
//         const right = document.createElement('div')
//         right.classList.add('productList__Item--right')
//         const photo = document.createElement('img')
//         photo.src = product.Image
//         right.appendChild(photo)
//         link.appendChild(right)
//         li.appendChild(link)
//         productList.appendChild(li);
//     });
// }

// const buttons = document.querySelectorAll('.category-btn');
// buttons.forEach(item=>{
//     item.addEventListener('click',()=>{
//         filterProducts(item.getAttribute("data-category"))
//     })
// })
// filterProducts("all")

let currentNumber = generateRandomFiveDigitNumber();

function generateRandomFiveDigitNumber() {
    return Math.floor(10000 + Math.random() * 90000);
}

const input = document.querySelector('.SubmiteForm input')
function getNextNumber() {
    alert(currentNumber++); 
}
input.addEventListener('click',getNextNumber)