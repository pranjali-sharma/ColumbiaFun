  
        $(document).ready(function(){
            $(".warnings").hide();            
            $("#name").focus();

    $('#submit-btn').click(function(){submit_pressed()});
});

function submit_pressed(){ 
    console.log("inside submit_pressed")  
    name_txt= $.trim($("#name").val());
    //console.log(name_txt);
    name_len=name_txt.length;
    //console.log(name_len);
    
    image_txt= $.trim($("#image").val());
    //console.log(image_txt);
    image_len=image_txt.length;
    //console.log(image_len);

    text_txt= $.trim($("#text").val());
    //console.log(text_txt);
    text_len=text_txt.length;
    //console.log(text_len);

    rating_txt= $.trim($("#rating").val());
    //console.log(rating_txt);
    rating_len=rating_txt.length;
    if($.isNumeric(rating_txt) && rating_len && rating_txt<=5){
        var rating_ok=1;
    }
    else{
        console.log("rating warning")
        $(".rating.warnings").show();
    }
    //console.log(rating_len);

    alums_txt= $.trim($("#alums").val());
    //console.log(alums_txt);
    alums_len=alums_txt.length;
    //console.log(alums_len);

    if(name_len && image_len && text_len && rating_ok && alums_len){
       console.log("all g");
      $(".warnings").hide(); 
           
      alums_li=alums_txt.split(",")
      console.log(alums_li)
      var alums_true=[]
      for(var i=0; i<alums_li.length; i++){
        alums_true[i]=true
      }
      activity={id:null, name:name_txt, img:image_txt, text:text_txt, rating:rating_txt, alums:[alums_true,alums_li]} ;
      createActivity(activity);
    }      
    else{
        if(name_len==0){
            $(".name.warnings").show();
            console.log("name is empty")
        }
        if(image_len==0){
            $(".image.warnings").show();
            console.log("image is empty")
        }
        if(alums_len==0){
            $(".alums.warnings").show();
            console.log("alums is empty")
        }
        if(text_len==0){
            $(".text.warnings").show();
            console.log("text is empty")
        }
    }
}

function createActivity(activity){
        console.log("reached create activity")
        console.log(activity)
        //ajax
        var data_to_save = {"new_activity": activity} 
        console.log(data_to_save)
        $.ajax({
        type: "POST",
        url: "createActivity",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
           // console.log(JSON.stringify(data_to_save))
            var link = result["data"]
            console.log("data="+link)
            displayLink(link)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    }

function displayLink(link){
    
    $("#feedback").append("New item successfully created.")
    console.log("reached displayLink")
    console.log("link="+link)
    var printLink=$("<a href="+link+">")
    $(printLink).text("See it here")
    $("#link").append(printLink);

    $("#name").val("");
    $("#image").val("");
    $("#text").val("");
    $("#rating").val("");
    $("#alums").val("");
    
    $("#name").focus();


}


