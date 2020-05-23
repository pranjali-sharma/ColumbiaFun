var displayActivities = function(){
    console.log("inside display activities")
//empty old data
//console.log("data="+data)
$("#add-deck").empty()
if(data.length){

for(i=0; i<data.length; i++){
    console.log(i+":"+data[i].name)
    var id=data[i].id;
    //console.log(id)
    var link=data[i].img; 
    //var new_activity= $("<div>"+datum["name"]+"</div>")
    //console.log("new_Activity="+new_activity)
    var new_card=$("<div class='card' id="+id+">")  
    var card_body=$("<div class='card-body'>")                
    var image=$("<img class='card-img-top' id="+id+" src=" + link +" alt='"+data[i].name+"'>")

    $(image).click(function(){
    var i=$(this).attr('id'); 
    window.location='/view/'+i;  

});
/*if(i%4==0){ 
    console.log("i="+i) 
    $("#add-deck").append("<div class='row'>")
    $("#add-deck").append(new_deck)
}*/

    var name=$("<div class='card-title' id="+id+">") 
    $(name).text(data[i].name);  
      

    $("#add-deck").append(new_card)
    $(new_card).append(card_body)
    
    $(card_body).append(image)
    $(card_body).append(name)

}

}

else{
$("#add-card").append("No results found")
}
}


$(document).ready(function(){
console.log("ready in home.html")
displayActivities();
});