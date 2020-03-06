<!DOCTYPE html>
<html lang="en">
<head>
	<title>Kasivore</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta name="google-signin-client_id" content="">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="images/icons/favicon.ico"/>
<!--===============================CSS================================================================-->
	<link rel="stylesheet" type="text/css" href="css/util.css">
	<link rel="stylesheet" type="text/css" href="css/main.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
<!--===================================Javascript============================================================-->
<script src="https://apis.google.com/js/platform.js" async defer></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script type="text/javascript">
	function ValidateUser() {
	  //document.getElementById("txtUsername").style.backgroundColor = "yellow";
		userNames= "{{ userNames}}";
		Email =document.getElementById( 'txtUsername' ).value.toString().trim();
		userNames = userNames.replace(/&quot;/g, '"').toUpperCase();
		if(userNames.indexOf(Email.toUpperCase()) !== -1 && document.getElementById('hf_IsSignup' ).value.toString()=="1") {
			document.getElementById( 'lbErrorMsg' ).innerHTML = "Username already in use: " + document.getElementById( 'txtUsername' ).value;
		}else{
			if(ValidateEmail(Email))
			{
				document.getElementById( 'lbErrorMsg' ).innerHTML = "";
			}
			else{
				document.getElementById( 'lbErrorMsg' ).innerHTML = "You have entered an invalid email address!";
			
			}
			
		}
		
	}
	function Signup_Click() {
	  //document.getElementById("txtUsername").style.backgroundColor = "yellow";
	  document.getElementById('txt_pass2' ).style.display = "block"; 
	  document.getElementById('ub_Create' ).style.display = "block";
	  document.getElementById('ub_LogIn' ).style.display = "none";
	  document.getElementById('ub_Signup' ).style.display = "none"; 
	  document.getElementById('hf_IsSignup' ).value = "1";
	  document.getElementById('txtUsername' ).value = "";
	  document.getElementById('lbForget' ).style.display = "none"; 
	   document.getElementById('ub_SigInGoogle' ).style.display = "none"; 
	  //alert(document.getElementById('hf_IsSignup' ).value);
	}
	function PageLoad() {
	  //document.getElementById("txtUsername").style.backgroundColor = "yellow";
	   //alert(document.getElementById('hf_IsSignup' ).value);
	  if(document.getElementById('hf_IsSignup' ).value==="")
	  {
		document.getElementById('txt_pass2' ).style.display = "none"; 
		document.getElementById('ub_Create' ).style.display = "none"; 
		document.getElementById('ub_LogIn' ).style.display = "block"; 
		document.getElementById('ub_Signup' ).style.display = "block"; 
		document.getElementById('lbForget' ).style.display = "block"; 
		document.getElementById('LoginDiv').style.display = "block"; 
		document.getElementById('div_HomePage').style.display = "none"; 
		
	  }
	  else
	  {
		document.getElementById('LoginDiv').style.display = "none"; 
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
 </script>
 <script src="Scripts/Script.js"></script>
 <style>

 </style>
</head>
<body onload="PageLoad()">

	<div   class="limiter" >
		<div class="container-login100" style="background-image: url('images/img-01.jpg');">
			<div class="wrap-login100" id="LoginDiv" style="display:none;" 	>
				<form class="login100-form validate-form">
					<div class="login100-form-avatar">
						<img src="images/logo.gif" alt="AVATAR">
					</div>
					<div class="WelcomeNote">
						
						<label id="lb_Welcome" > Welcome!</label>
					</div>
					<div class="ErrorMsg">
						<label id = "lbErrorMsg" > </label>
					</div>
					
					<div class="wrap-input100 validate-input m-b-10" data-validate = "Username is required">
						<input id="txtUsername" class="input100" type="text" name="username" placeholder="Username" onblur="ValidateUser()">
						<span class="focus-input100"></span>
						<span class="symbol-input100">
						</span>
					</div>

					<div class="wrap-input100 validate-input m-b-10" data-validate = "Password is required">
						
						<input class="input100" type="password" name="pass" placeholder="Password" id="txt_pass1">
						<span class="focus-input100"></span>
						<span class="symbol-input100">
						</span>
						
						<br>
						<input class="input100" type="password" name="pass" placeholder="Confirm Password" id="txt_pass2" style= "display: none" >
					</div>
					
					<div class="text-center w-full">
						<a href="#" class="txt1">							
							<label id="lbForget" >Forgot Username / Password?</label>
						</a>
					</div>

					<div class="container-login100-form-btn p-t-10">
						<button class="login100-form-btn"  id="ub_Create" style= "display: none" > 
							Create Account
						</button>
						<button class="login100-form-btn"  id="ub_LogIn" >
							Login
						</button>
					</div>
					
					<div class="container-login100-form-btn p-t-10" id="ub_Signup">
						<button class="login100-form-btn" onclick="Signup_Click(); return false;">
							Signup
						</button>
					</div>
					<div class="container-login100-form-btn p-t-10" id="ub_SigInGoogle">
						<div class="g-signin2" data-onsuccess="onSignIn" style="float:left"  ></div> 
						
						
					</div>
					<div class="container-login100-form-btn p-t-10">
						
					</div>
					
				</form>
			</div>
			
		</div>
	</div>
	
	<div id="div_HomePage" class="limiter-Signedin"  >
		<div class="container-login100" style="background-image: url('images/img-01.jpg');">
		<div class="wrap-login100-Signedin">
			<div class="login100-form-avatar">
						<img id="ppPic" >
			</div>
			<div class="WelcomeNote">
				<label id="lb_User" ></label>
			</div>
			<div class="WelcomeNote">
				<label id="lb_Email" ></label>
			</div>
			<div class="WelcomeNote">
				<label id="lb_UserID" ></label>
			</div>
		</div>
			
			
		</div>
	</div>
	<!--===================================Hidden fields============================================================-->
	<input type="hidden" id="hf_IsSignup"  >
	
	

</body>
</html>