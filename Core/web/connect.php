<!-----------------------
-       TTHPieCore
- Main Website
- Copyright2020: 2/9/2021
------------------------------>
<?php
$servername = "151.106.97.0";
$database = "u559891715_Main";
$username = "u559891715_Pie";
$password = "Yards123!";
// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";
mysqli_close($conn);
?>