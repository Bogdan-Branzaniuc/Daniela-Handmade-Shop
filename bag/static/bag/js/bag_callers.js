
for( let button of document.querySelectorAll('.add-to-bag-btn')){
    button.addEventListener('click', (e) => {
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            let size = selectedSizeJs
            let color = selectedColorJs
            let qty = Number(document.querySelector(`#id_qty_${productId}`).value)
            Unicorn.call('bagstatus', 'add_to_bag', productId, size, color, qty)
        },300)
    })
}
for(let button of document.querySelectorAll('.remove-from-bag-btn')){
    button.addEventListener('click', (e) => {
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            console.log(productId)
            let size = selectedSizeJs
            let color = selectedColorJs
            Unicorn.call('bagstatus', 'remove_from_bag', productId, size, color)
        },300)
    })
}

for (let button of document.querySelectorAll('.adjust-product-bag-btn')){
    button.addEventListener('click', (e) => {
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            let size = selectedSizeJs
            let color = selectedColorJs
            let qty = Number(document.querySelector(`#id_qty_${productId}`).value)
            console.log('adjust product')
            console.log(qty)
            if(qty > 0){
                Unicorn.call('bagstatus', 'add_to_bag', productId, size, color, qty)
            }else{
                Unicorn.call('bagstatus', 'remove_from_bag', productId, size, color)
            }
        },300)
    })
}

function pageReload(){
    location.reload()
}