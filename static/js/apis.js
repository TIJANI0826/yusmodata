var settingsIUC = {
  "url": "https://www.husmodata.com/ajax/validate_iuc?smart_card_number=iuc_number&cablename=cable_company",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Token 8f00fa816b1e3b485baca8f44ae5d361ef803311",
    "Content-Type": "application/json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});


var settingsMeterNumber = {
  "url": "https://www.husmodata.com/ajax/validate_meter_number?meternumber=54140827962&disconame=disco_name&mtype=Prepaid
",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Authorization": "Token 8f00fa816b1e3b485baca8f44ae5d361ef803311",
    "Content-Type": "application/json"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});