/**
Js file to store functionality for django unicorn product component view
**/
let selectedColorJs
let selectedSizeJs
let componentQuantityJs

function focusProductButtons(buttonId, currentValue){
    if($('#'+buttonId).text() == currentValue) {
        $('#'+buttonId).css('border', 'solid 2px black');
    }
}
function setSelectedSizeColorQty(size, color, qty) {
    selectedColorJs = color;
    selectedSizeJs = size;
    componentQuantityJs = qty
}

function pageReload(){
    location.reload()
}

function updateBagstatus(){
    setTimeout(()=>{
        Unicorn.call('bagstatus', 'update')
    },300)
}