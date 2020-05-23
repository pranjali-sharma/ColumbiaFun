var displayActivities = function(){
    console.log("inside display activities")
//empty old data
//console.log("data="+data)
$("#updates").empty()
console.log(data)
var val= data[data.length-1]
console.log(val)

if(data.length-1){
    var num_results= data.length-1
$(".results_count").text("There are "+ num_results +" results for \""+val+"\".")
for(i=0; i<data.length-1; i++){
    //console.log(i+":"+data[i].name)
    var id=data[i].id;
    //console.log(id)
    var link=data[i].img; 
    //var new_activity= $("<div>"+datum["name"]+"</div>")
    //console.log("new_Activity="+new_activity)
    var new_card=$("<div class='card' id="+id+">")  
    var card_body=$("<div class='card-body row'>")                
    var image=$("<img class='col-3 card-img-left' id="+id+" src=" + link +"  alt="+data[i].name+" >")

    $(image).click(function(){
    var i=$(this).attr('id'); 
    console.log("clicked:"+i)
    window.location='/view/'+i;  

});
    
    var name=$("<div class='col-7 card-title' id="+id+" >") 
    var lowerVal= val.toLowerCase()
    var dataname=data[i].name
    var lowerName=dataname.toLowerCase()
    lowerName=" "+lowerName+" "
    console.log("val="+lowerVal)
    console.log("name="+lowerName)
    var index=lowerName.indexOf(lowerVal)
    console.log(val+"@"+index)
    if (index>=0){
        console.log("val in name")
        dataname=dataname.substring(0,index)+"<span class='highlight'>" + dataname.substring(index, index+val.length-1)+"</span>" + dataname.substring(index+val.length-1)
        console.log(dataname)
    }

    $(name).append(dataname);  
      
    $("#updates").append(new_card)
    $(new_card).append(card_body)
    
    $(card_body).append(image)
    $(card_body).append(name)

}
}

else{
$("#updates").append("No results found")
}
}


$(document).ready(function(){
console.log("ready in search.html")
displayActivities();
});