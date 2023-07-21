/**
Js file to store functionality for django unicorn product components
**/
let selectedColorJs
let selectedSizeJs
let componentQuantityJs
function focusProductButtons(buttonId, currentValue){
    if($('#'+buttonId).text() == currentValue) {
        $('#'+buttonId).css('border', 'solid 2px black');
    }
}
function setSelectedColor(value) {
    selectedColorJs = value;
}
function setSelectedSize(value){
    selectedSizeJs = value
}
function setSelectedQuantity(value){
    componentQuantityJs = value
}