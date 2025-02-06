//  fetch('https://jsonplaceholder.typicode.com/users', {
//      method: 'POST',
//      headers: {'Content-type': 'application/json'},
//      body: JSON.stringify()
//  })
//    .then(res => res.json()) 
// 	.then(data => console.log(data))

// function getUserUrl(id) {
//   const userURL = `https://jsonplaceholder.typicode.com/user/${id}` // bu url 
//   axios.get(userURL)
//     .then(res => console.log(res.data))
//     .catch(err => console.error(err))
// }
// getUserUrl(1)

// Task 01
// Rəqəmlər massivini parametr kimi qəbul edən və 
// əgər həmin massivdə mənfi ədədlər varsa onları massiv şəklində geri qaytaran,
//  yoxdursa uyğun mesajı geri qaytaran funksiya yazın.

const global = [12,-231, 3121, -443]

if(true){
    var local = global.map(item =>item <= 0 ? item: false)
    console.log(local, 'if scope');

    
}

console.log(global, 'log');
console.log(local, 'log')




// Task 02
// Adlar massivi verilib. 
// Bir funksiya yazın, hansı ki parametr olaraq massiv qəbul edir.
//  Həmin massivdə "A" hərfi ilə başlayan elementlərdən ibarət yeni massiv yaradıb, 
// elə bir dəyər tapılmasa uyğun mesajı geri qaytarmalıdır.
let namesArray = [
"Alice",
"Bob",
"Catherine",
"David",
"Eva",
"Andrew",
"Frank",
"Anna",
"item",
"Alex",
];


item.index


// Task 03
// ƏDV xaric qiymətlər saxlayan massivini qəbul edən və 
// ƏDV daxil olmaqla olan qiymətlərdən ibarət yeni massiv qaytaran funksiya yazın.
// addTax() funksiyası yaradın.
//  Verilmiş ƏDV-siz qiymətlərlə olan price massivini ona ötürün. 
// addTax() funksiyasının köməyi ilə 
// ƏDV ilə qiymətlərin daxil olduğu massiv yaratın və funksiya həmin massivi geri qaytarsın. 
// ƏDV 20% təşkil edir.
// Input: const pricesArray = [12.99, 24.95, 9.99, 34.50, 19.99, 42.75, 8.49, 15.00, 28.75, 10.99];