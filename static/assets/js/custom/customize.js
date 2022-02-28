$('#cat2').hide();
$('#lbl_cat1').hide();
let data = [{"id":1,"name":"Infimos","parentid":0, "urgency": "low"},
{"id":2,"name":"Computer servicing","parentid":0, "urgency": "medium"},
{"id":3,"name":"Software installation","parentid":0, "urgency": "urgent"},
{"id":4,"name":"Fix errors","parentid":1, "urgency": "urgent"},
{"id":5,"name":"New feature","parentid":1, "urgency": "medium"},
{"id":6,"name":"Add payee","parentid":1, "urgency": "urgent"},
{"id":7,"name":"Add user","parentid":1, "urgency": "medium"},
{"id":8,"name":"System assistance","parentid":1, "urgency": "urgent"},
{"id":9,"name":"Internet connection problem","parentid":2, "urgency": "medium"},
{"id":10,"name":"Computer malfunction","parentid":2, "urgency": "medium"},
{"id":11,"name":"Printer connection problem","parentid":2, "urgency": "medium"},
{"id":12,"name":"Install microsoft office","parentid":3, "urgency": "low"},
{"id":13,"name":"Printer/scanner Installation","parentid":3, "urgency": "medium"},
{"id":14,"name":"Install other applications","parentid":3, "urgency": "low"},
]

function populateList(list, pid) {
  let l = document.getElementById(list);
  l.innerHTML = "";
  let topItem = document.createElement("option");
  topItem.value = 0;
  topItem.text = "Select";
  l.appendChild(topItem); 
  let items = data.filter(item => item.parentid == pid);
  items.forEach(function(item){
    let newItem = document.createElement("option");
    newItem.value = item.id;
    newItem.text = item.name;
    l.appendChild(newItem);
  });
  if (!items.length) {
    let item = data.filter(item => item.id == pid)[0];
    l.value = item.urgency;
  }
}

function updateList(selList, thisList) {
	$('#cat2').show();
	$('#lbl_cat1').show();
  if (thisList.value != 0) {
    populateList(selList, Number(thisList.value));
  } else {
    let s = document.getElementById(selList);
    s.value = 0;
    triggerEvent(s, "onchange");
    let sCopy = s.cloneNode(false);
    let p = s.parentNode;
    p.replaceChild(sCopy, s);
  }
}
function triggerEvent(e, trigger)
{
    if ((e[trigger] || false) && typeof e[trigger] == 'function')
    {
        e[trigger](e);
    }
}

function loadCat1() {
  populateList("cat1", 0);
}

window.onload = loadCat1;