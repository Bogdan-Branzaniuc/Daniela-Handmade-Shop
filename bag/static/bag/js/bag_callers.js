
for( let button of document.querySelectorAll('.add-to-bag-btn')){
    button.addEventListener('click', (e) => {
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            let size = selectedSizeJs
            let color = selectedColorJs
            let qty = Number(document.querySelector(`#id_qty_${productId}`).value)
            Unicorn.call('bagstatus', 'add_to_bag', productId,size, color, qty)
        },300)

    })
}
for(let button of document.querySelectorAll('.remove-from-bag-btn')){
    button.addEventListener('click', (e) => {
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            let size = selectedSizeJs
            let color = selectedColorJs
            Unicorn.call('bagstatus', 'remove_from_bag', productId, size, color)
        },300)
    })
}

for(let button of document.querySelectorAll('.adjust-the-bag-btn')){
    button.addEventListener('click', (e)=>{
        setTimeout(()=>{
            let productId = button.id.split('-')[4]
            let size = selectedSizeJs
            let color = selectedColorJs
            console.log('called bagstatus with',selectedSizeJs, selectedColorJs)
        }, 300)
    })
}

