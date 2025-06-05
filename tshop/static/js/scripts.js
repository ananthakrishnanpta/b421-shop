function updateCart(item, isAdd){
    const quantity_element = document.getElementById(`item-qnty-${item}`);
    const item_element = document.getElementById(`item-${item}`);
    const sub_total  = document.getElementById(`sub-total-${item}`);

    value = parseInt(quantity_element.innerText);
    if (isAdd){
        // alert(`Adding quantity to item ${item}`);
        actionUrl = '';
        quantity_element.innerText = value + 1;
        

    }
    else {
        // alert(`Removing quantity to item ${item}`);
        actionUrl = '';

        if (value <= 1){
            item_element.remove();
        }
        else {
            quantity_element.innerText = value - 1;
        }
      
            
       
        
    }

    
}