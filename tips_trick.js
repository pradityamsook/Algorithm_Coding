// parse string to float
parseFloat(keys.name)
  .toFixed(2)
  .replace(/\d(?=(\d{3})+\.)/g, "$&,");

//function format date
function formatDate(dateString) {
  var allDate = dateString.split(" ");
  var thisDate = allDate[0].split("-");
  thisDate[0] = 543 + parseInt(thisDate[0]);
  var newDate = [thisDate[2], thisDate[1], thisDate[0]].join("-");

  return newDate;
}
