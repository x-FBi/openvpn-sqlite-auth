<?php
session_start();
include("db.php");
?>
<?php
$saltysalt = hash('sha512',"t0p$eCRT"); # EDIT ME
$msg = "";
if(isset($_POST['submitBtnLogin'])) {
        $username = trim($_POST['username']);
        $password = trim($_POST['password']);
        $newpassword = trim($_POST['newpassword']);
        $verifypassword = trim($_POST['verifypassword']);
        if($username != "" && $password != "" && $newpassword != "" && $verifypassword != "") {
                if($newpassword != $verifypassword) {
                        $msg = "Your new password doesn't match.";
                }elseif($password == $verifypassword) {
                        $msg = "Your New Password is the same as your old password <br> Kindly Retry With a New Password.";
                }else {
                $password = hash('sha512', $password.$saltysalt); // Add Salt, if need be.
                try {
                        $query = "SELECT COUNT(*) as count FROM users WHERE username = :username AND password = :password";
                        $stmt = $db->prepare($query);
                        $stmt->bindParam(':username', $username, PDO::PARAM_STR);
                        $stmt->bindParam(':password', $password, PDO::PARAM_STR);
                        $stmt->execute();
                        $row = $stmt->fetch(PDO::FETCH_ASSOC);
                        $count = $row['count'];
                        if($count > 0 && !empty($row)) {
                                $query = "UPDATE users SET password=:password WHERE username=:username";
                                $stmt = $db->prepare($query);
                                $verifypassword = hash('sha512', $verifypassword.$saltysalt); // New Password Hashed -- Add Salt, if need be
                                $stmt->bindParam(':username', $username, PDO::PARAM_STR);
                                $stmt->bindParam(':password', $verifypassword, PDO::PARAM_STR);
                                $stmt->execute();
                                /******************** Your code ***********************
                                header('location:home.php');
                                */
                                $msg = "Password for $username has been updated. \n <br><br> <a href=https://do.uwantmy.info/romania.ovpn>OpenVPN Config File</a herf> \n";
                        } else {
                                $msg = "Invalid username and password!";
                        }
                }

                catch (PDOException $e) {
                        echo "Error : ".$e->getMessage();
                }
        }
        } else {
                $msg = "Please fill in all fields.";
        }
}
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
<title>OpenVPN Password Update Tool</title>
<style>
.clearfix { clear:both; }
span { clear:both; display:block; margin-bottom:30px; }
span a { font-weight:bold; color:#0099FF; }
label { margin-top:20px; margin-bottom:3px; font-weight:bold;}
.loginTable {
        text-align: center; /* Adding to all */
        margin: auto;
        position:absolute;
        left:0;
        top:0;
        right:0;
        bottom:0;
        width:400px;
        height:200px;
        border:2px solid #0099FF;
        padding:10px;
}
.loginTable label {
        text-align: center; /* Adding to all */
        display:block;
        margin-bottom:3px;
        color:#0099FF;
        font-weight:bold;
}
.loginTable .firstLabel {
        margin-top:20px;
}

.loginTable th {
        text-align: center; /* Adding to all */
        border-bottom:2px solid #0099FF;
        margin-bottom:10px;
        color:#0099FF;
        text-align: center; /* Adding to all */
}
.loginTable #username, #password,#mname,#verifypassword,#newpassword {
        width:365px;
        margin-bottom:7px;
        padding:3px 10px;
        text-align: center; /* Adding to all */
}
.loginTable #submitBtnLogin {
        padding:5px 20px;
        text-align: center; /* Adding to all */
}
.loginTable .loginMsg {
        color:#FF0000;
        text-align: center;
    padding-top: 5px;
        height:50px; /* Changed from 10px */
        text-align: center; /* Adding to all */
}
</style>

</head>

<body>
        <br><br>
                <form method="post">
                <table class="loginTable">
                  <tr>
                        <th>OpenVPN Password Update Tool</th>
                  </tr>
                  <tr>
                        <td>
                                <label class="firstLabel">Username:</label>
                        <input type="text" name="username" id="username" value="" autocomplete="off" />
                        </td>
                  </tr>
                  <tr>
                        <td><label>Old Password:</label>
                    <input type="password" name="password" id="password" value="" autocomplete="off" /></td>
                  </tr>
                  <tr>
                        <td><label>New Password:</label>
                    <input type="password" name="newpassword" id="newpassword" value="" autocomplete="off" /></td>
                  </tr>
                  <tr>
                        <td><label>Verify New Password:</label>
                    <input type="password" name="verifypassword" id="verifypassword" value="" autocomplete="off" /></td>
                  </tr>
                  <tr>
                        <td><input type="submit" name="submitBtnLogin" id="submitBtnLogin" value="Login" /><span class="loginMsg"><br><?php echo @$msg;?></span></td>
                  </tr>
                </table>
                </form>

</body>
</html>
