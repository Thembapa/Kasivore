
 var _validFileExtensions = [".jpg", ".jpeg", ".bmp", ".gif", ".png"]; //Image Types

 /* 
 	Date picker
 */
//


//Select option
function selectElement(id, valueToSelect) {    
    let element = document.getElementById(id);
    element.value = valueToSelect;
}
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
	function ProfileSlides(CurrentSection)
	{
		document.getElementById('AccountForm' ).style.display = "none";
		document.getElementById('Bioform' ).style.display = "none";
		document.getElementById('Addressform' ).style.display = "none";
		document.getElementById('Businessform' ).style.display = "none";
		document.getElementById('BusinessAddressform' ).style.display = "none";
		document.getElementById('showcaseForm' ).style.display = "none";
		document.getElementById('WelcomeForm' ).style.display = "none";
		document.getElementById(CurrentSection).style.display = "block";
		document.getElementById('Accountlabel' ).innerHTML = CurrentSection.replace('form','').replace('Form','')
		
		if(CurrentSection == 'BusinessAddressform' || CurrentSection =='showcaseForm')
		{
			CurrentSection = 'Businessform';
		}

		var radioButtons1 = 'radio' +CurrentSection + '1';
		var radioButtons2 = 'radio' +CurrentSection + '2';
		
		document.getElementById(radioButtons1 ).checked = true;
		document.getElementById(radioButtons2 ).checked = true;
	}
	//Change Account Type
	function ChangeAccountType(){
		document.getElementById("AccountForm").submit();
	           
	}


	function IndexPage()
	{
		window.location.replace("/index");
	}
	function UpLoadProfilePic(input) {
        if (ValidateImage(input)) {
            var reader = new FileReader();
            str = input.value;
            //#Newpp.url = input;
            var FileName = str.substring(str.indexOf('fakepath'), str.length); 
            document.getElementById( 'lbFileName' ).innerHTML = FileName.replace('fakepath\\','');
            
		    reader.onload = function (e) {
                $('#Newpp')
                    .attr('src', e.target.result)
                    ;
            };
            reader.readAsDataURL(input.files[0]);

            //Save image to server 
            document.getElementById("hf_ppUpload").value ="1";
            document.getElementById("AccountForm").submit();
	           
	    }
	}
	function SelectThumbnail(imageid){
		document.getElementById("hf_imageID").value = imageid;
        document.getElementById("showcaseForm").submit();
	}
	function UpLoadWorkDone(input) {
        if (ValidateImage(input)) {
            var reader = new FileReader();
            str = input.value;
            //#Newpp.url = input;
            var FileName = str.substring(str.indexOf('fakepath'), str.length); 
            document.getElementById( 'lbImageName' ).innerHTML = FileName.replace('fakepath\\','');

            //Save image to server 
            document.getElementById("hf_ImageUpload").value ="1";
            document.getElementById("showcaseForm").submit();
	           
	    }
	}


	function ValidateImage(oInput) {
		str = oInput.value;
		var FileName = str.substring(str.indexOf('fakepath'), str.length); 
        FileName = FileName.replace('fakepath\\','');
		 if (oInput.type == "file") {
		        var sFileName = oInput.value;
		         if (sFileName.length > 0) {
		            var blnValid = false;
		            for (var j = 0; j < _validFileExtensions.length; j++) {
		                var sCurExtension = _validFileExtensions[j];
		                if (sFileName.substr(sFileName.length - sCurExtension.length, sCurExtension.length).toLowerCase() == sCurExtension.toLowerCase()) {
		                    blnValid = true;
		                    break;
		                }
		            }
		             
		            if (!blnValid) {
		                alert("Sorry, " + FileName + " is invalid, allowed extensions are: " + _validFileExtensions.join(", "));
		                oInput.value = "";
		                return false;
		            }
		        }
		    }
		    return true;
	}
	function validateID() {
		var ex = /^(((\d{2}((0[13578]|1[02])(0[1-9]|[12]\d|3[01])|(0[13456789]|1[012])(0[1-9]|[12]\d|30)|02(0[1-9]|1\d|2[0-8])))|([02468][048]|[13579][26])0229))(( |-)(\d{4})( |-)(\d{3})|(\d{7}))/;
			  
		var theIDnumber = document.getElementById('txtIDNO' );
		if (ex.test(theIDnumber.value) == false) {
		  // alert code goes here
		  alert('Please supply a valid ID number');		  
		}
		
	  }
	  function changeFunc($i) {
		if($i !='South Africa')
		{
			document.getElementById('passportdiv' ).style.display = 'Block';
			document.getElementById('SAiddiv' ).style.display = 'none';			
			document.getElementById('txtIDNO' ).required;
		}
		else
		{
			document.getElementById('passportdiv' ).style.display = 'none';
			document.getElementById('SAiddiv' ).style.display = 'Block';
			document.getElementById('txtPassport' ).required;
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
	//Drop Down Select
	function myFunction() {
		document.getElementById("myDropdown").classList.toggle("show");
		
	  }
	  
	  function filterFunction() {
		var input, filter, ul, li, a, i;
		input = document.getElementById("myInput");
		filter = input.value.toUpperCase();
		div = document.getElementById("myDropdown");
		a = div.getElementsByTagName("a");
		for (i = 0; i < a.length; i++) {
		  txtValue = a[i].textContent || a[i].innerText;
		  if (txtValue.toUpperCase().indexOf(filter) > -1) {
			a[i].style.display = "";
		  } else {
			a[i].style.display = "none";
		  }
		}
	  }
	  function CategorySelect(SeletedCategory,Categoryvalue, collapse) {
		
		document.getElementById( 'hf_Category' ).value = SeletedCategory;
		document.getElementById( 'btCategory' ).innerHTML = Categoryvalue;
		document.getElementById( 'hf_CategoryName' ).value = Categoryvalue;
		if(collapse == 1)
		{
			myFunction();
		}
		
		
	}
	function passwordMissMatch(txt1, txt2) 
	{
		var pass1 = document.getElementById(txt1);
		var pass2 = document.getElementById(txt2);
		if (pass1.value.toString() != pass2.value.toString() )
		{
			document.getElementById( 'hf_Error' ).value =  "password mismatch";
		    document.getElementById( 'lbErrorMsg' ).innerHTML = "password mismatch";
		}
		else{
			 document.getElementById( 'hf_Error' ).value =  "";
		     document.getElementById( 'lbErrorMsg' ).innerHTML ="";
		}
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
			document.getElementById('hf_GoogleprofilePic').value =  profile.getImageUrl();
			document.getElementById('hf_Email').value =  profile.getEmail();
			document.getElementById('hf_GmailName').value = profile.getName();
		 }
		 catch(err) {
		   
		 }
		document.getElementById("frmGoogleSignIn").submit();
	 
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
	function passwordValidation(textboxName) 
	{
		  var x = document.getElementById(textboxName);
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

  