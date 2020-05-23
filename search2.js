var displayActivities = function(){
    console.log("inside display activities")
//empty old data
//console.log("data="+data)
$("#add-card").empty()
console.log(data)
var val= data[data.length-1]
console.log(val)

if(data.length-1){
    var num_results= data.length-1
$(".results_count").text("There are "+ num_results +" results for \""+val+"\".")
for(i=0; i<data.length-1; i++){
    var dataname=data[i].name
    console.log(i+":"+dataname)
    var id=data[i].id;
    //console.log(id)
    var link=data[i].img; 
    //var new_activity= $("<div>"+datum["name"]+"</div>")
    //console.log("new_Activity="+new_activity)
    var new_card=$("<div class='card' id="+id+">")  
    var card_body=$("<div class='card-body'>")                
    var image=$("<img class='card-img-top' id="+id+" src=" + link +"  alt='" + dataname + "' >")

    $(image).click(function(){
    var i=$(this).attr('id'); 
    console.log("clicked:"+i)
    window.location='/view/'+i;  

});
    
    var name=$("<div class='card-title' id="+id+" >") 
    //comparing  highlightig searched word
    var lowerVal= val.toLowerCase()
    var lowerName=dataname.toLowerCase()
    console.log("val="+lowerVal)
    console.log("name="+lowerName)
    var index=lowerName.indexOf(lowerVal)
    console.log(val+"@"+index)
    if (index>=0){
        console.log("val in name")
        dataname=dataname.substring(0,index)+"<span class='highlight'>" + dataname.substring(index, index+val.length)+"</span>" + dataname.substring(index+val.length)
        console.log(dataname)
    }

    $(name).append(dataname);  
      
    $("#add-card").append(new_card)
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
console.log("ready in search.html")
displayActivities();
});