<?php

class database{
    private $db_handle;
    private $host = "localhost";
    private $db = "cloudcomputinghmwrk";
    private $user = "root";
    private $password = '';

    public function __construct() {
        $this->db_handle = mysqli_connect($this->host,$this->user,$this->password); //connect to mysql
        if(!$this->db_handle) die('Unable to connect to MYSQL'.mysqli_error($this->db_handle));
        if(!mysqli_select_db($this->db_handle, $this->db)) die('Unable to select database'.mysqli_error($this->db_handle));
    }

    public function execute_query($sql_stmt) {
        $result = mysqli_query($this->db_handle,$sql_stmt);
        if (!$result) die('Database access failed: '.mysqli_error($this->db_handle));
        
        return $result;
    }

    public function __destruct() {
        mysqli_close($this->db_handle);
    }

}