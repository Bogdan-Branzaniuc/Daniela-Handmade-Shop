
for( let button of document.querySelectorAll('.add-to-bag-btn')){
            button.addEventListener('click', (e) => {
                let productId = button.id.split('-')[4]
                console.log(productId)

                setTimeout(()=>{
                    Unicorn.call('bagstatus', 'add_to_bag', productId)
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

window.onerror = function(message, source, lineno, colno, error) {
  // Handle the error here
  console.log('An error occurred:', message, source, lineno, colno, error);
};