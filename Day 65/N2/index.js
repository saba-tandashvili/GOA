var num1 = prompt("Enter the first number:");
var num2 = prompt("Enter the second number:");

num1 = parseInt(num1);
num2 = parseInt(num2);

if (num1 > num2) {
    console.log("The first number is greater than the second number.");
    console.log("true");
} else {
    console.log("The first number is not greater than the second number.");
    console.log("false");
}