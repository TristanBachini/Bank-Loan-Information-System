let percentage = document.getElementById("percentage");
let amount = document.getElementById("amount");
let sellingprice = document.getElementById("sellingprice");

percentage.oninput = function(){
    if(sellingprice.value.length!=0){
        amount.value = (sellingprice.value/100)*percentage.value;
    } 
    
}

amount.oninput = function(){
    if(sellingprice.value.length!=0){
        percentage.value = (amount.value/sellingprice.value)*100;
        percent = percentage.value
        percentage.value = percent.toFixed(1)
    } 
}


