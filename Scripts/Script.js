function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
   $(".data").css("display","block");
   $("#lb_Email").text(profile.getEmail());
   $("#lb_User").text(profile.getName());
   $("#lb_UserID").text(profile.getId());
   $("#ppPic").attr('src',profile.getImageUrl());
   $("#hf_GoogleprofilePic").value(profile.getImageUrl());
   $(".limiter").css("display","none");
   $(".limiter-Signedin").css("display","block");
  //window.location.replace("/Home");
  //console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  //console.log('Name: ' + profile.getName());
  //console.log('Image URL: ' + profile.getImageUrl());
  //console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}
