
// for ajax calls 
        $(document).ready(function(){
            var fetch_rating=0;

            $('input:radio').click(()=>{
                
                fetch_rating= $('input[type=radio][name=rate]:checked').attr('value')
                console.log(fetch_rating)

                data_to_send = {
                    user_id:"BX1023",
                    user_rating:fetch_rating,
                }
                console.log(data_to_send);
                    
                $.ajax({
                    url:"/single_product",
                    type:"post",
                    data:data_to_send,
                    success: function(){
                        console.log("Data Sent...")
                    },
                    error: function(){
                        console.log("Data Error...")
                    }

                })
            })
        })

// for spinner

document.querySelector('.container').style.display='none';
document.querySelector('.loader').classList.add('spinner-1');
setTimeout(()=>{
      document.querySelector('.loader').classList.remove('spinner-1')
      document.querySelector('.container').style.display = 'block';
},2000)

// for add to cart

$(document).ready(function(){
    $('#wishlist').text(localStorage.length)

    $('#add-to-cart').click( ()=>{
        
        let product = $('#item-name').text()
        let price = $('#item-price').text()
        let item_count = $('#item-value').val()

        console.log(product,price,item_count)

        let fe = localStorage.getItem(product)

        let sa = new Array( parseInt(price),parseInt(item_count))
        console.log(sa)



        if(fe==null){
            // add this to localStorage
            localStorage.setItem(product,JSON.stringify(sa))

            console.log(localStorage.getItem(product))
            $('#wishlist').text(localStorage.length)
            $('#add-to-cart').text("Added to cart")
        }
    })
    $('#logout-user').click(()=>{
        localStorage.clear();
        console.log("Session Data Cleared..")
    })


})


