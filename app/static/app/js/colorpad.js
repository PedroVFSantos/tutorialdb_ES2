var elem = document.getElementsByName("colorpad");

for (var item of elem) {
  item.style.backgroundColor = randomColor({luminosity: 'light'});
}
