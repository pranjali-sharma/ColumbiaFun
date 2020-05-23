
    
    var id;
    $(document).ready(function(){
       
        $("#warning").hide();

        $("#name").append(data[0].name);

        id=data[0].id
        console.log(id)
/*
        var link="http://127.0.0.1:5000/edit/"+id
        var printLink=$("<a href="+link+">")
        $(printLink).text("edit")
        $("#link").append(printLink);
        */
       
        $("#text").append(data[0].text);
        $("#rating").append(data[0].rating);
        printList(data[0].alums);
        var link=data[0].img;
        var image=$("<img src=" + link + ' class="center" alt="This is the image of the activity">')
        console.log(image)
        $("#image").append(image)

        $("#edit_text").click(function(){  
            //put text in box
            $("#edit_text").hide();
            var box=$('<textarea id="text_editable" rows="4" cols="100" autofocus>')
            $(box).val(data[0].text);
            //buttons
            var submit_text=$('<button/>', {
                text: "Submit",
                id: 'submit',
                class: 'btn btn-primary'
            });
            $(submit_text).click(function(){
                var text= $(box).val()
                console.log("submit clicked")
                submitText(text, id);
            });

            var discard_text=$('<button/>', {
                text: "Discard",
                id: 'discard',
                class: 'btn btn-warning'
            });
            $(discard_text).click(function(){
                console.log("discard clicked")           
                    window.location='/view/'+id;
            });

            $("#text").empty()
            $("#text").append(box)
            $("#text").append(submit_text)
            $("#text").append(discard_text)

            console.log("edit text")

        });
        

        $("#edit_rating").click(function(){  

            console.log("edit rating")
            //add text box
            //add buttons
            //put text in box
            $("#edit_rating").hide();
            var box=$('<textarea id="rating_editable" rows="1" cols="2" autofocus>')
            $(box).val(data[0].rating);
            //buttons
            var submit_rating=$('<button/>', {
                text: "Submit",
                id: 'submit',
                class: 'btn btn-primary'
            });
            $(submit_rating).click(function(){                    
                console.log("submit clicked")
                var rating= $(box).val()
                if($.isNumeric(rating) && rating<=5){
                    console.log(rating)
                    submitRating(rating, id);
                }
                else{
                    $("#warning").show();
                    console.log("warnign")
                }
            });

            var discard_rating=$('<button/>', {
                text: "Discard",
                id: 'discard',
                class: 'btn btn-warning'
            });
            $(discard_rating).click(function(){
                console.log("discard clicked")           
                    window.location='/view/'+id;
            });

            $("#rating").empty()
            $("#rating").append(box)
            $("#rating").append(submit_rating)
            $("#rating").append(discard_rating)

            
            
        });

        
    });

   

    
    function submitRating(edit, id){
        console.log("reached submit rating")
        var data_to_save = {"edits": edit} 
        console.log(data_to_save)
        $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/submit_rating/"+id,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
           // console.log(JSON.stringify(data_to_save))
           console.log("success");
           var data=result["data"]
           console.log(data)
           var id=data.id
           console.log(id)
           window.location='/view/'+id;
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    }



    
    function submitText(edit, id){
        console.log("reached submit rating")
        var data_to_save = {"edits": edit} 
        console.log(data_to_save)
        $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/submit_text/"+id,                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
           // console.log(JSON.stringify(data_to_save))
           console.log("success");
           var data=result["data"]
           console.log(data)
           var id=data.id
           console.log(id)
           window.location='/view/'+id;
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
    }
    function printList(alums){
        console.log("print list")
        console.log(alums)
        var show=[];
        show=alums[0]

        var names=[];
        names=alums[1]
        console.log(names)

        for(index=0; index<names.length; index++){
            console.log(show[index])
            
            var value=names[index]
            console.log(value)
            if(show[index]){
            var alum_row=$('<div class="row" id='+ index +'>')
            var alum_text=$('<div class="col-4">')
            $(alum_text).text(value)


            var del=$('<button/>', {
                text: "X", 
                id: index,
                class: 'btn-xs btn-danger h-10'
            });

    $(del).click(function(){
        console.log("clikccccccc")
        
        var ind=$(this).attr('id');
        console.log(ind+"=deleted")
        $("#"+ind).empty();
        var undo_del=$('<button/>', {
            text: "Undo Delete", 
            id: ind,
            class: 'btn btn-secondary h-10'
        });

        $(undo_del).click(function(){
            console.log("clikced undo")
            undo_delete(ind, id);
        });

        $("#"+ind).append(undo_del);  
          
    delete_alum(ind, id);
    });
    
    $('#alums').append(alum_row);
    $(alum_row).append(del);
    $(alum_row).append(alum_text)

}

    }
  }

  var delete_alum = function(index, id){ 
    console.log("reached delete_activity")
    console.log(index)
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/delete_alum/"+id,  
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(index),        
        success: function(data){
            console.log("in successs")
            var all_activities = data["activities"]
            activities=all_activities
            var all_data=data["data"]
            data=all_data
            console.log("activities: "+activities.length)
            console.log("data="+data.length)
            //window.location='/view/'+id;

        },
        error: function(request, status, error){
            
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
} 
var undo_delete= function(index, id){ 
    console.log("reached delete_activity")
    console.log(index)
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/undo_delete_alum/"+id,  
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(index),        
        success: function(data){
            console.log("in successs")
            var all_activities = data["activities"]
            activities=all_activities
            var all_data=data["data"]
            data=all_data
            console.log("activities: "+activities.length)
            console.log("data="+data.length)
            window.location='/view/'+id;

        },
        error: function(request, status, error){
            
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
} 