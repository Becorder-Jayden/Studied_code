// Function
// - fundamental building block in the program
//  - subprogram can be used multiple times
//  - performs a task or calcuates a value

// 1. Fucntion declaration
// function name(param1, param2) { body... return; }
// one function === on thing
// naming: doSomething, command, verb
// e.g. createCardAndPoint -> createCared, reatePoint
// function is object in JS
function printHello() {
  console.log('Hello');
}
printHello();

function log(message) {
  console.log(message);
}
log('Hello@');
log(1234);

// 2. Parameters
// permitive parameters: passed by value
// object parameters: passed by reference
function changeName(obj) {
  obj.name = 'coder';
}
const ellie = { name: 'ellie' };
changeName(ellie);
console.log(ellie);

// 3. Default prameters (added in ES6)
function showMessage(message, from = 'unknown') {
  console.log(`${message} by ${from}`);
}
showMessage('Hi!');

// 4. Rest parameters (added in ES6)
function printAll(...args) {
  for (let i = 0; i < args.lenth; i++) {
    console.log(args[i]);
  }

  for (const arg of args) {
    console.log(arg);
  }

  args.forEach(arg => console.log(arg));
}
printAll('ream', 'coding', 'ellie');

// 5. Local scope
//  밖에서는 안이 보이지 않고 안에서만 밖을 볼 수 있다
let globalMessage = 'global'; // global variable
function printMessage() {
  let message = 'hello';
  console.log(message); // local variable
  console.log(globallMessage);
  function printAnother() {
    console.log(message);
    let childMessage = 'hello';
  }
  console.log(childMessage); // error
}

// 6. Return a skill__value
function sum(a, b) {
  return a + b;
}
const result = sum(1, 2); // 3
console.log(`sum: ${sum(1, 2)}`);

// 7. Early return, early exit
// bad
function upgradeUser(user) {
  if (user.point > 10) {
    // long upgrade logic...
  }
}

// good
function upgradeUser(user) {
  if (user.point <= 10) {
    return;
  }

  // long upgrade logic...
}

// Fist-class function
// functions are treated like any other variable
// can be assigned as a value to variable
// can ba passed as an argument to other functions
// can be returned by another function

// 1. Function expression
// a function declaration can be called earlier than it is defined. (hoisted)
// a function expression is created when the execution reaches it.
const print = function () {
  console.log('print');
};
print();
const printAgain = print;
printAgain();
const sumAgain = sum;
console.log(sumAgain(1, 3));

// 2. Callback function using fuction expression
function randomQuiz(answer, printYes, printNo) {
  if (answer === 'love you') {
    printYes();
  } else {
    printNo();
  }
}

// anonymous function
const printYes = function () {
  console.log('yes!');
};

// named function
// better debugging in debugger's stack traces
// recursions
const printNo = function print() {
  console.log('no!');
  // print();
};
randomQuiz('wrong', printYes, printNo);
randomQuiz('love you', printYes, printNo);

// Arrow function
// always anonymous
const simplePrint = function () {
  console.log('simplePrint!');
};

const simplePrint = () => console.log('simplePrint!');
const add = (a, b) => {
  a + b;
};
const simpleMultiply = (a, b) => {
  // do something more
  return a * b;
};

// IIFE: immedately Invoked Function Expression
(function hello() {
  console.log('IIFE');
})();

// Fun quiz time
// function calculate(command, a, b)
// command: add, substract, divide, multiply, remainder

function calculate(command, a, b) {
  switch (command) {
    case 'add':
      return a + b;
    case 'substract':
      return a - b;
    case 'divide':
      return a / b;
    case 'multiply':
      return a * b;
    case 'remainder':
      return a % b;
    default:
      throw Error('unknown command');
  }
}
onmouseleave.log(calcuate('add', 2, 3));
