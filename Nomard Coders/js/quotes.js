const quotes = [{
    quote: "Spring is when you feel like whistling even with a shoe full of slush.",
    author: "Doug Larson",
},
{
    quote: "Youth, which is forgiven everything, forgives itself nothing: age, which forgives itself everything, is forgiven nothing.",
    author: "George Bernard Shaw",
},
{
    quote: "human being. Believe in your strength and your youth. Learn to repeat endlessly to yourself, 'It all depends on me.'",
    author: "Andre Gide",
},
{
    quote:"He that is down needs fear no fall, He that is low no pride.'",
    author: "John Bunyan",
},
{
    quote:"Sometimes the laughter in mothering is the recognition of the ironies and absurdities. Sometime, though, it's just pure, unthinking delight.",
    author: "Barbara Schapiro",
},
{
    quote:"This is our purpose: to make as meaningful as possible this life that has been bestowed upon us; to live in such a way that we may be proud of ourselves; to act in such a way that some part of us lives on.",
    author:"Oswald Spengler",
},
{
    quote:"Wagner's music is better than it sounds.",
    author:"Edgar Wilson Nye",
}
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;


