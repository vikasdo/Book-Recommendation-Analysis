
$(document).ready(()=>{

	data_recieved = $.get("localhost:5000/get_data",(data,status)=>{
		console.log(data)
	})



})