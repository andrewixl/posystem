$(document).ready(function(){
  // $('#authcode').hide();
  $('.authcoderadio').click(function(){
      if ( $("#authcode").length ){
      }
      else{
        $(".authcode").append('<input type="password" id = "authcode" name="auth_code" placeholder="Please Enter Auth Code." size=30><br>');
      }
  })
  $('.requestradio').click(function(){
    if ( $("#authcode").length ){
      $(".authcode").empty();
    }
  })
});
