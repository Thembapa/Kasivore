function ValidateUser() {
		
		Email =document.getElementById( 'txtUser1' ).value.toString().trim();

		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
		if (xhr.readyState == XMLHttpRequest.DONE) {
			userNames =xhr.responseText;

				if( userNames.indexOf("Error") !== -1)
				{
				    document.getElementById( 'lbErrorMsg' ).innerHTML = userNames.replace('Error: ','');
				    document.getElementById( 'hf_Error' ).value = userNames.replace('Error: ','');
				    document.getElementById("txtUser1").focus();
							
				} else
				{
				    		
				    document.getElementById( 'lbErrorMsg' ).innerHTML = "";
				    document.getElementById( 'hf_Error' ).value ="";
				    if(ValidateEmail(Email))
					{
						document.getElementById( 'lbErrorMsg' ).innerHTML = "";
					}
					else{
						document.getElementById( 'lbErrorMsg' ).innerHTML = "Invalid email!";
						document.getElementById( 'hf_Error' ).value =  "Invalid email!";
						document.getElementById("txtUser1").focus();
					
					}
				    		
				}
				        
			}
		}
		url = '/UserNames/'+ Email
		xhr.open('GET', url, true);
		xhr.send(null);	

		
		
	}
	function Signup_Click() {
	  //document.getElementById("txtUsername").style.backgroundColor = "yellow";

	  document.getElementById('frmResetPass' ).style.display = "none"; 
	  document.getElementById('SiginForm' ).style.display = "none"; 
	  document.getElementById('SigupForm' ).style.display = "block";
	  document.getElementById('footer').style.display = "none";
	  document.getElementById('hf_IsSignup' ).value = "1";
	  document.getElementById('Error').style.display = "block";
	  document.getElementById( 'lbSignin' ).innerHTML = "Sign up";
		  

	  // document.getElementById('ub_SigInGoogle' ).style.display = "none"; 
	  //alert(document.getElementById('hf_IsSignup' ).value);
	}
	function ResetPass()
	{
		document.getElementById('frmResetPass' ).style.display = "block"; 
		document.getElementById('SiginForm' ).style.display = "none"; 
	  	document.getElementById('SigupForm' ).style.display = "none";
	  	document.getElementById('footer').style.display = "none";
	  	document.getElementById('hf_IsSignup' ).value = "1";
	  	document.getElementById('Error').style.display = "block";
	  	document.getElementById( 'lbSignin' ).innerHTML = "Reset password";
	}

	function PageLoad() {
	  //document.getElementById("txtUsername").style.backgroundColor = "yellow";
	   //alert(document.getElementById('hf_IsSignup' ).value);
	  


	  if(document.getElementById('hf_IsSignup' ) != null)
	  {
	  	
	  	 if(document.getElementById('hf_IsSignup' ).value==="")	  
	  	 {
			document.getElementById('SiginForm' ).style.display = "block";
			document.getElementById('footer').style.display = "block"; 
			document.getElementById('SigupForm' ).style.display = "none";
			document.getElementById('Error').style.display = "none";
			document.getElementById( 'lbSignin' ).innerHTML = "Sign in";
			//document.getElementById('LoginDiv').style.display = "block"; 
			//document.getElementById('div_HomePage').style.display = "none"; 
			
		  }
		  else
		  {
		  	document.getElementById( 'lbSignin' ).innerHTML = "Sign up";
			document.getElementById('SiginForm' ).style.display = "none"; 
		  	document.getElementById('SigupForm' ).style.display = "block";
		  	document.getElementById('footer').style.display = "none";
		  	document.getElementById('Error').style.display = "block";
		  	document.getElementById( 'lbSignin' ).innerHTML = "Sign out";
		  }
	  }
	 
	}
	
	function ValidateEmail(mail) 
	{
	 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail))
	  {
		return (true)
	  }
		return (false)
	}
	function passwordMissMatch() 
	{
		var pass1 = document.getElementById("txt_pass1");
		var pass2 = document.getElementById("txt_pass2");
		if (pass1.value.toString() != pass2.value.toString() )
		{
			document.getElementById( 'hf_Error' ).value =  "password mismatch";
		    document.getElementById( 'lbErrorMsg' ).innerHTML = "password mismatch";
		}
		else{
			 document.getElementById( 'hf_Error' ).value =  "";
		     document.getElementById( 'lbErrorMsg' ).innerHTML ="";
		}````
	}
	function onSignIn(googleUser) {
	  var profile = googleUser.getBasicProfile();
	   $(".data").css("display","block");
	  // $("#lb_Email").text(profile.getEmail());
	  // $("#lb_User").text(profile.getName());
	   //$("#lb_UserID").text(profile.getId());
	  
	   //$(".limiter").css("display","none");
	   //$(".limiter-Signedin").css("display","block");
	  //window.location.replace("/Home");
	  //console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
	  //console.log('Name: ' + profile.getName());
	  //console.log('Image URL: ' + profile.getImageUrl());
	  //console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
	   try {
           $("#profilepicture").attr('src',profile.getImageUrl());
        }
        catch(err) {
          
        }
	  Url = '/login/' + profile.getEmail()+'/'+ profile.getName()
	  
	  if(document.getElementById('hf_GoogleprofilePic' ) != null)
	  {
	       window.location.replace(Url);
	  }
	 
	}

	function sinOut() {
	   
	   
	   try {
          var auth2 = gapi.auth2.getAuthInstance();
    	   auth2.signOut().then(function () {
    	   auth2.disconnect();
    	   });
        }
        catch(err) {
          
        }
	   	
	 	window.location.replace('/login');
	}
	function passwordValidation() 
	{
		  var x = document.getElementById("txt_pass1");
		  var error = document.getElementById("lbErrorMsg");
		  var progress = document.getElementById("passwordStregnth");
		  currentpass = x.value.toString();

		  var strength = 0;
		  if (currentpass.match(/[a-z]+/)) {
		    strength += 1;
		  }
		  if (currentpass.match(/[A-Z]+/)) {
		    strength += 1;
		  }
		  if (currentpass.match(/[0-9]+/)) {
		    strength += 1;
		  }
		  if (currentpass.match(/[$@#&!]+/)) {
		    strength += 1;

		  }

		  if (currentpass.length < 6) {
		    document.getElementById( 'hf_Error' ).value = "minimum number of characters is 6";
		    document.getElementById( 'lbErrorMsg' ).innerHTML = "minimum number of characters is 6";
		  }else if (currentpass.length > 12) {

		    document.getElementById( 'hf_Error' ).value =  "maximum number of characters is 12";
		    document.getElementById( 'lbErrorMsg' ).innerHTML = "maximum number of characters is 12";
		 }else
		 {

		    document.getElementById( 'hf_Error' ).value =  "";
		    document.getElementById( 'lbErrorMsg' ).innerHTML ="";
		}

		  switch (strength) {
		    case 0:
		      //strengthbar.value = 0;
		       progress.style.width ="0%";
		       progress.style.backgroundColor ="red";
		      break;

		    case 1:
		      //strengthbar.value = 25;
		       progress.style.width ="25%";
		       progress.style.backgroundColor ="orange";
		      break;

		    case 2:
		      //strengthbar.value = 50;
		      progress.style.width ="50%";
		      progress.style.backgroundColor ="blue";
		      break;

		    case 3:
		      //strengthbar.value = 75;
		       progress.style.width ="75%";
		       progress.style.backgroundColor ="#4ef542";
		      break;

		    case 4:
		      //strengthbar.value = 100;
		      progress.style.width ="100%";
		      progress.style.backgroundColor ="green";
		      break;
		  }
  }