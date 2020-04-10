selectedColor = 'gray'

function changeColor(color) {
  selectedColor = color
  element = document.getElementById('card--creator');
  removeLastClass(element);
  addClass(element, "card-" + color);
}

function addClass(element, name) {
  arr = element.className.split(" ");
  if (arr.indexOf(name) == -1) {
    element.className += " " + name;
  }
}

function removeLastClass(element) {
  arr = element.className.split(" ");
  arr.splice(arr.length - 1, 1)
  element.className = arr.join(" ");
}

function addCard()  {
  var date = new Date();
  var timestamp = date.getTime();

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      window.location = "/";
    }
  }
  xhr.open("POST", "/api/dudu", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify([
    document.getElementById('card--from').value,
    document.getElementById('card--to').value,
    document.getElementById('card--message').value,
    selectedColor,
    timestamp
  ]));
}

function getCards()  {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
      refreshCard(xhr.responseText)
    }
  }
  xhr.open("GET", "/api/dudu", true);
  xhr.send();
}

function refreshCard(data) {
  cards = JSON.parse(data)
  element = document.getElementById('board');

  html_cards = ``
  cards.forEach(function(card, index) {
    html_cards += 
    `
    <div class="card card-` + card['color'] + `">
      <div class="card--section"><span>Dari</span><p>` + card['dari'] + `</p></div>
      <div class="card--section"><span>Untuk</span><p>` + card['untuk'] + `</p></div>
      <div class="card--section"><span>Dengan Ucapan</span><p>` + card['dengan_ucapan'] + `</p></div>
    </div>
    `
  });

  element.innerHTML = html_cards;
}

getCards();