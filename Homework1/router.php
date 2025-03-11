<?php

spl_autoload_register(function ($class) {
    require __DIR__ . "/$class.php";
});

set_exception_handler("errorHandler::handleException");

header("Content-type: application/json; charset=UTF-8");

if ($_SERVER['CONTENT_TYPE'] !== 'application/json') {
    http_response_code(400);
    echo json_encode(["error" => "Invalid Content-Type. Must be application/json."]);
    exit;
}

$uri = explode("/", $_SERVER['REQUEST_URI']);

$database = new database();

$service = new service($database);

switch(count($uri))
{
    case 4:
        $service->processRequest1($_SERVER['REQUEST_METHOD'],$uri[3]);
        break;
    case 5:
        $service->processRequest2($_SERVER['REQUEST_METHOD'],$uri[3],$uri[4]);
        break;
    case 6:
        $service->processRequest3($_SERVER['REQUEST_METHOD'],$uri[3],$uri[4],$uri[5]);
        break;
    case 7:
        $service->processRequest4($_SERVER['REQUEST_METHOD'],$uri[3],$uri[4],$uri[5],$uri[6]);
        break;
    default:
        http_response_code(404);
        echo json_encode("Not good URL.");
        exit;
}