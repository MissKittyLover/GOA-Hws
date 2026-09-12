// 2) შექმენი:

// let money = 100;

// წარმოიდგინე, რომ გაქვს 100 ლარი:

// დაამატე 50 ლარი +=
// დახარჯე 30 ლარი -=
// გააორმაგე დარჩენილი თანხა *=
// გაყავი 2-ზე /=
// შემდეგ გამოიყენე ++
// გამოიყენე --

// და საბოლოოდ დაბეჭდე money

let money = 100
money += 50
money -=30
money *= 2
money /= 2
money--

console.log(money)

// 3) კომენტარის სახით ახსენით თუ რა არის es6, და ასევე ახსენით თუ რომელი 2 keyword გამოუშვა es6 მა ცვლადების შესაქმნელად

/* ES6 (ES2015) is a JavaScript standard which adds a few features to JS. Rge 2 main keywords we learned are let and const.
They are both used to create variables. Let is more flexible as it allows you to change the variable later on whenever you wish.
Const on the other hand is less flexible and more fixed. If you want to make sure your variable never gets modified you can use const.

// 4) ახსენით var, let და const თავიანთი მახასიათებლებით

let, var and const are syntaxes used to create variables.
let and var are the same when it comes to flexibility because you are able to change both of their definitions. However, the definitions
are changed differently. With variable you created in var, you can modify that variable and write the same syntax in the front while
that would be a syntax error in let variables. var is function-scoped ( it’s accessible anywhere within the function it’s declared in, 
or globally if declared outside a functionwhile let is block-scoped (it’s only accessible within the {} block where it’s declared. 
This prevents accidental access or modification outside the intended scope.).
I explained const in the previous task. */

// 5) შექმენი:

// let balance = 500;

// შემდეგ გამოიყენე assignment operators:

// დაამატე 200 +=
// გამოაკელი 150 -=
// გაამრავლე 2-ზე *=
// გაყავი 5-ზე /=
// გამოიყენე ++
// გამოიყენე --

// ბოლოს დაბეჭდე balance.

let balance = 500
balance += 200
balance -=150
balance *= 2
balance /= 5
balance++

console.log(balance)