data = [
  {
    "DiscoID": 1,
    "DiscoName": "Ikeja Electric"
  },
  {
    "DiscoID": 2,
    "DiscoName": "Eko Electric"
  },
  {
    "DiscoID": 3,
    "DiscoName": "Abuja Electric"
  },
  {
    "DiscoID": 4,
    "DiscoName": "Kano Electric"
  },
  {
    "DiscoID": 5,
    "DiscoName": "Enugu Electric"
  },
  {
    "DiscoID": 6,
    "DiscoName": "Port Harcourt Electric"
  },
  {
    "DiscoID": 7,
    "DiscoName": "Ibadan Electric"
  },
  {
    "DiscoID": 8,
    "DiscoName": "Kaduna Electric"
  },
  {
    "DiscoID": 9,
    "DiscoName": "Jos Electric"
  },
  {
    "DiscoID": 11,
    "DiscoName": "Yola Electric"
  },
  {
    "DiscoID": 10,
    "DiscoName": "Benin Electric"
  }
]

$(document).ready(function () {
  $('#discoSelect').focus(function(){

    $(this).html(function() {
      var options = `<option value=''>select plan id</option>`
      data.forEach((element, index, array) => {
        options +=`<option value='${element.DiscoID}'>${element.DiscoName}</option>`
      });
      return options
    });
  });
});

