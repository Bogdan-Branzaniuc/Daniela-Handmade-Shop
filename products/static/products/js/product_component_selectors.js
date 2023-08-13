/**
Js file to store functionality for django unicorn product component view
**/
let selectedColorJs
let selectedSizeJs

function focusProductButtons(buttonId, currentValue){
    if($('#'+buttonId).attr('data-btn-info') == currentValue) {
        $('#'+buttonId).css('border', 'solid 3px #10122b');
    }
}
function setSelectedSizeColorQty(size, color) {
    selectedColorJs = color;
    selectedSizeJs = size;
}

function pageReload(){
    location.reload()
}

function updateBagstatus(){
    setTimeout(()=>{
        Unicorn.call('bagstatus', 'update')
    },100)
}