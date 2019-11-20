<?php
	if($_POST['key'])
	{
		$myfile=fopen("key_db.txt","a");
		fwrite($myfile,$_SERVER['REMOTE_ADDR'] . " " . $_POST['key'] . "\n");
		fclose($myfile);
		echo "True";
	}
?>
