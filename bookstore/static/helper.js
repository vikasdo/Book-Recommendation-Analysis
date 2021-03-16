
// for ajax calls 
        $(document).ready(function(){
            var fetch_rating=0;

            $('input:radio').click(()=>{
                
                fetch_rating= $('input[type=radio][name=rate]:checked').attr('value')
                console.log(fetch_rating)


                let book_id = window.location.href.split('/').splice(-1)[0]

                let user_id = $('#session-data').attr('data-session')

                data_to_send = {
                    user_id:user_id,
                    user_rating:fetch_rating,
                    book_id:book_id
                }
                console.log(data_to_send);


                $.ajax({
                    url:window.location.href,
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
},1000)

// for add to cart

$(document).ready(function(){
    $('#wishlist').text(localStorage.length)

    $('#add-to-cart').click( ()=>{
        
        let product_id = window.location.href.split('/').splice(-1)[0]

        let sx=product_id.length

        if(product_id[sx-1]=='!' && product_id[sx-2]=='#')
            product_id=product_id.substr(0,sx-2)

        console.log(product_id)

        let price = $('#item-price').text()
        let item_count = $('#item-value').val()

        console.log(product_id,price,item_count)

        let fe = localStorage.getItem(product_id)

        if(fe!=null){
            localStorage.removeItem(product_id)
        }
        
        let sa = new Array( parseInt(price),parseInt(item_count))
        console.log(sa)

            // add this to localStorage
            localStorage.setItem(product_id,JSON.stringify(sa))

            console.log(localStorage.getItem(product_id))
            $('#wishlist').text(localStorage.length)
            $('#add-to-cart').text("Added to cart")

    })
    $('#logout-user').click(()=>{
        localStorage.clear();
        console.log("Session Data Cleared..")
    })



    $('#basket').click(()=>{

        $('#main-cart-content').empty()
        
        let total_price = 0;

        if(localStorage.length>0){
            $('#empty_cart_img').hide();

                        $('#main-cart-content').append(`<table class="table table-bordered" id="cart-table">
          <tr>
          <th>Product Name</th>
          <th>Quantity</th>
          <th>Price</th>
          <th>Total</th>
          </tr>
            </table>`)

        for(let i=0;i<localStorage.length;i++){
            let product_name=localStorage.key(i);
            
            let price = JSON.parse(localStorage.getItem(product_name))[0]
            
            let quantity = JSON.parse(localStorage.getItem(product_name))[1]


            let html_content =`<tr>
                                <td>${product_name}</td>
                                <td>${quantity}</td>
                                <td>${price}</td>
                                <td>${price*quantity}</td>
                                </tr>`

            $('#cart-table').append(html_content)
            total_price+=(price*quantity)
        }


        // set discounted price

        const user_id = $('#session-data').attr('data-session')


        $.get('/getDiscountedUsers',(data,status)=>{
            
            const user_discount=data;

            for(var x in user_discount){
                
                const re=parseInt(x)

                if(re==user_id){
                    console.log("User will get Discount")
                    $('#discount-message').text(`Hurrah !! You Get a Discount of ${user_discount[x]}% :)`)
                    total_price-=((total_price*parseInt(user_discount[x])/100))
                    break;
                }
            }
            console.log(user_id)
            console.log("Total Price :" + total_price)

            $('#total-item-price').text(`Total Price : ${total_price}`)
            $('#total_price').text(total_price)
        })
        }

    })




    $('#checkout').click(()=>{

            $('#main-cart-content').empty()
            $('#total-item-price').empty()
            $('#discount-message').empty()
            if(localStorage.length>0){

            $('#empty_cart_img').hide();

            data_to_send = {
                "order":JSON.stringify(localStorage),
                "total-price":$('#total_price').text()
            }

            $('#total-item-price').text("Please Wait...")

            setTimeout(()=>{
                $('#order-success').show()

                $('#total-item-price').text("Success, Payment Completed...")                

                $('#checkout').removeAttr('disabled')

            },3000)

            setTimeout(()=>{

                    $('#order-success').hide();
                    $('#empty_cart_img').show();

                    $('#total-item-price').text("Your Cart is Empty..")                

            },4000)

            $.ajax({
                    url:window.location.origin+"/transaction",
                    type:"post",
                    data:data_to_send,
                    success: function(){
                        console.log("Data Sent for checkout...")
                    },
                    error: function(){
                        console.log("Data Error during checkout...")
                    }

                })

            $('#checkout').attr('disabled',true)

            localStorage.clear()    
            $('#wishlist').text(0)
        }
        else{
            $('#total-item-price').text("Your Cart is Empty Add something to checkout")
        }
    })

    $('#empty_cart').click(()=>{
        console.log("Clicked")
            $('#main-cart-content').empty()
            $('#total-item-price').empty()
            $('#discount-message').empty()
            $('#total-item-price').text('Your Cart is Empty')
            $('#empty_cart_img').show();
            $('#wishlist').text(0)
            localStorage.clear();
    })




})


// analysis part



var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
            label: '# of Votes',
            data: [12, 19, 3, 5, 2, 3],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});
