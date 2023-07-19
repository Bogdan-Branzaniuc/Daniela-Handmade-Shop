
for( let button of document.querySelectorAll('.add-to-bag-btn')){
            button.addEventListener('click', (e) => {
                let productId = button.id.split('-')[4]

                setTimeout(()=>{
                    let size = 'M'
                    let color = 'red'
                    let qty = Number(document.querySelector(`#id_qty_${productId}`).value)

                    Unicorn.call('bagstatus', 'add_to_bag', productId,size, color, qty)
                },300)
            })
        }

for( let button of document.querySelectorAll('.remove-from-bag-btn')){
            button.addEventListener('click', (e) => {
                let productId = button.id.split('-')[4]
                setTimeout(()=>{
                    Unicorn.call('bagstatus', 'remove_from_bag', productId)
                },300)
            })
        }

