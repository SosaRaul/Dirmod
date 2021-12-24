const  requestURL = 'https://ruush4tbo8.execute-api.us-east-2.amazonaws.com/v1/?date=2010-12-12&base_currency=USD';
const request = new XMLHttpRequest();


function onRequestHandler() {
  console.log(this.response)
}
request.addEventListener("load",onRequestHandler)
request.open('GET',requestURL)
request.send()
