$(document).ready(function(){
    $("#showvendors").click(function(){
        $('#myTable tbody').empty();
        console.log("Clicked")
        $.getJSON( "http://localhost:8000/data/" + $( "#vendor" ).val(), function( json ) {
          for (i = 0; i < json.length; i++) {
            console.log(json[i].fields.product_description );
            $('#myTable tbody').append(
              '<tr class="child"><td><input type="checkbox" name="product" value="'+json[i].pk+'"></td><td>' + json[i].fields.product_description + '</td><td>' + json[i].fields.product_quantity + '</td><td>' + json[i].fields.unit_cost + '</td><td>' + json[i].fields.final_cost + '</td></tr>'
            );
          }
         });

    });
});
