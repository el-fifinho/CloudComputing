<?php

class errorHandler
{
    public static function handleException(Throwable $throwable): void
    {
        http_response_code(500);
        echo json_encode([
            "code" => $throwable->getCode(),
            "message" => $throwable->getMessage(),
            "file" => $throwable->getFile(),
            "line" => $throwable->getLine()
        ]);
    }
}