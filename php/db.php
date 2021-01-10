<?php
try {
        $db = new PDO('sqlite:database.name');
        $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        $db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
} catch (PDOException $e) {
        echo "Connection failed : ". $e->getMessage();
}
?>
