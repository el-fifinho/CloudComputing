<?php

class service
{
    private $database;
    public function __construct(database $database)
    {
        $this->database = $database;
    }

    public function processRequest1($method,$collection): void
    {
        if(!in_array($collection,["teams","players","tournaments"]))
        {
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        switch($method)
        {
            case "GET":
                $sql_stmt = "SELECT info FROM `$collection`";
                $this->getAll_1($sql_stmt);
                break;
            case "POST":
                $data = file_get_contents("php://input");
                $sql_stmt = "INSERT INTO `$collection` (`id`, `info`) VALUES (NULL, '$data')";
                $this->post_1($sql_stmt);
                break;
            default:
                http_response_code(403);
                echo json_encode("Method not supported.");
                break;
        }
    }

    public function processRequest2($method,$collection,$id): void
    {
        if(!in_array($collection,["teams","players","tournaments"]))
        {
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        switch($method)
        {
            case "GET":
                $sql_stmt = "SELECT info FROM `$collection` WHERE id = $id";
                $this->get_2($sql_stmt);
                break;
            case "PUT":
                $data = file_get_contents('php://input');
                $validate = json_decode($data, true);
                if (json_last_error() !== JSON_ERROR_NONE) {
                   http_response_code(400);
                    echo json_encode(["error" => "Malformed JSON payload."]);
                    return;
                }
                $this->put_2($collection, $id, $data);
                break;
            case "DELETE":
                $sql_stmt = "DELETE FROM `$collection` WHERE `$collection`.`id` = $id";
                $this->delete_2($sql_stmt);
                break;
            default:
                http_response_code(403);
                echo json_encode("Method not supported.");
                break;
        } 
    }

    public function processRequest3($method,$collection1,$id,$collection2): void
    {
        if(!in_array($collection1,["teams","tournaments"]) || !in_array($collection2,["teams","players","matches"]))
        {
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        switch($method)
        {
            case "GET":
                switch($collection1)
                {
                    case "teams":
                        $this->get_teams_3($id,$collection2);
                        break;
                    case "tournaments":
                        $this->get_tournaments_3($id,$collection2);
                        break;
                    default:
                        break;
                }
                break;
            case "POST":
                $data = file_get_contents('php://input');
                $validate = json_decode($data, true);
                if (json_last_error() !== JSON_ERROR_NONE) {
                   http_response_code(400);
                    echo json_encode(["error" => "Malformed JSON payload."]);
                    return;
                }
                switch($collection1)
                {
                    case "teams":
                        $this->post_teams_3($id,$collection2,$data);
                        break;
                    case "tournaments":
                        $this->post_tournaments_3($id,$collection2, $data);
                        break;
                    default:
                        break;
                }
                break;
            default:
                http_response_code(403);
                echo json_encode("Method not supported.");
                break;
        }
    }

    public function processRequest4($method,$collection1,$id1,$collection2,$id2): void
    {
        if(!in_array($collection1,["teams","tournaments"]) || !in_array($collection2,["teams","players"]))
        {
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        if($method != "DELETE"){
            http_response_code(403);
            echo json_encode("Method not supported.");
            return;
        }

        $this->delete_4($collection1,$id1,$collection2,$id2);
    }

    private function getAll_1($stmt): void
    {
        $sql_response = $this->database->execute_query($stmt);
        $data = array();
        while($row = $sql_response->fetch_column())
        {
            $data[] = json_decode(json: $row);
        }
        $response = [];
        foreach($data as $tournament)
        {
            $decoded_json = (array)$tournament;
            $response[] = $decoded_json['name'];
        }
        http_response_code(200);
        echo json_encode($response);
    }

    private function post_1($stmt): void
    {
        $sql_response = $this->database->execute_query($stmt);
        if($sql_response)
        {
            http_response_code(201);
            echo json_encode("Resource created successfuly.");
        }
        else
        {
            http_response_code(500);
            echo json_encode("Something went wrong");
        }
    }

    private function get_2($stmt): void
    {
        $sql_response = $this->database->execute_query($stmt);
        $data = array();
        while($row = $sql_response->fetch_column())
        {
            $data = $row;
        }

        if(empty($data))
        {
            http_response_code(204);
            echo json_encode("No content.");
        }else{
            http_response_code(200);
            echo $data;
        }
    }
    private function put_2($collection, $id, $input):void
    {
        $sql_stmt = "SELECT info FROM `$collection` WHERE id = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        $original_data = array();
        while($row = $sql_response->fetch_column())
        {
            $original_data[] = $row;
        }
        if(count($original_data) == 0)
        {
            http_response_code(204);
            echo json_encode("Resourse not found.");
            return;
        }

        $inputData = json_decode($input,true);
        $data = json_decode($original_data[0],true);

        $updatedData = array_merge( $data,$inputData);
        $JSON_updatedData = json_encode($updatedData);

        $sql_stmt = "UPDATE `$collection` SET `info` = '$JSON_updatedData' WHERE `$collection`.`id` = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        if ($sql_response) {
            http_response_code(200);
            echo json_encode(["message" => "Resource updated successfully."]);
        } else {
            http_response_code(500);
            echo json_encode(["error" => "Failed to update resource."]);
        }
    }
    private function delete_2($stmt): void
    {
        $sql_response = $this->database->execute_query($stmt);
        if($sql_response)
        {
            http_response_code(201);
            echo json_encode("Resource deleted successfuly.");
        }
        else
        {
            http_response_code(500);
            echo json_encode("Something went wrong");
        }
    }

    private function get_teams_3($id,$collection): void
    {
        if($collection != "players"){
            http_response_code(404);
            echo json_encode("No such URL");
            return;
        }
        $sql_stmt = "SELECT info FROM `teams` WHERE id = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        $team = $sql_response->fetch_column();
        if(!$team){
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        $teamInfo = json_decode($team,true);
        $playersIds = $teamInfo['players'];

        $players = array();
        foreach($playersIds as $playerId)
        {
            $stmt = "SELECT info FROM `players` WHERE id = $playerId";
            $playerResult = $this->database->execute_query($stmt);
            $player = json_decode($playerResult->fetch_column(),true);
            if ($player){
                $players[] = $player['name'];
            }
        }

        http_response_code(200);
        echo json_encode($players);
    }

    private function get_tournaments_3($id,$collection): void
    {
        $sql_stmt = "SELECT info FROM `tournaments` WHERE id = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        $tournament = $sql_response->fetch_column();
        if(!$tournament){
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        $tournamentInfo = json_decode($tournament, true);
        
        if($collection == "teams"){
            $teamsIDs = $tournamentInfo['teams'];

            $teams = array();
            foreach($teamsIDs as $teamId)
            {
                $stmt = "SELECT info FROM `teams` WHERE id = $teamId";
                $teamResult = $this->database->execute_query($stmt);
                $team = json_decode($teamResult->fetch_column(),true);
                if ($team){
                    $teams[] = $team['name'];
                }
            }

            http_response_code(200);
            echo json_encode($teams);
        }else{
            http_response_code(200);
            echo json_encode($tournamentInfo['matches']);
        }
    }

    private function post_teams_3($id,$collection,$input): void
    {
        if($collection != "players"){
            http_response_code(404);
            echo json_encode("No such URL");
            return;
        }
        $sql_stmt = "SELECT info FROM `teams` WHERE id = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        $team = $sql_response->fetch_column();
        if(!$team){
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        $teamInfo = json_decode($team,true);
        $playersIds = $teamInfo['players'];

        if(in_array($input,$playersIds)){
            http_response_code(409);
            echo json_encode("Player allready in team");
            return;
        }

        array_push($teamInfo['players'],(int)$input);
        $team = json_encode($teamInfo);

        $sql_stmt = "UPDATE `teams` SET `info` = '$team' WHERE `teams`.`id` = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        if ($sql_response) {
            http_response_code(200);
            echo json_encode(["message" => "Resource updated successfully."]);
        } else {
            http_response_code(500);
            echo json_encode(["error" => "Failed to update resource."]);
        }
    }

    private function post_tournaments_3($id,$collection,$input): void
    {
        $sql_stmt = "SELECT info FROM `tournaments` WHERE id = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        $tournament = $sql_response->fetch_column();
        if(!$tournament){
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        $tournamentInfo = json_decode($tournament, true);

        if($collection == "teams"){
            if(in_array((int)$input,$tournamentInfo[$collection])){
                http_response_code(409);
                echo json_encode("Resource allready in collection.");
                return;
            }
            array_push($tournamentInfo[$collection],(int)$input);
        }else{
            array_push($tournamentInfo[$collection],$input);
        }

        $tournament = json_encode($tournamentInfo);

        $sql_stmt = "UPDATE `tournaments` SET `info` = '$tournament' WHERE `tournaments`.`id` = $id";
        $sql_response = $this->database->execute_query($sql_stmt);
        if ($sql_response) {
            http_response_code(200);
            echo json_encode(["message" => "Resource updated successfully."]);
        } else {
            http_response_code(500);
            echo json_encode(["error" => "Failed to update resource."]);
        }
    }

    private function delete_4($collection1,$id1,$collection2,$id2): void
    {
        $sql_stmt = "SELECT info FROM `$collection1` WHERE id = $id1";
        $sql_response = $this->database->execute_query($sql_stmt);
        $data = json_decode($sql_response->fetch_column(),true);
        if(!$data){
            http_response_code(404);
            echo json_encode("Not found.");
            return;
        }
        #array_diff($data[$collection2],[(int)$id2]);
        $result = array_filter($data[$collection2], function($value) use ($id2) {
            return $value !== (int)$id2;
        });
        
        $data[$collection2] = array_values($result);

        $updatedData = json_encode($data);
        $sql_stmt = "UPDATE `$collection1` SET `info` = '$updatedData' WHERE `$collection1`.`id` = $id1";
        $sql_response = $this->database->execute_query($sql_stmt);
        if ($sql_response) {
            http_response_code(200);
            echo json_encode(["message" => "Resource updated successfully."]);
        } else {
            http_response_code(500);
            echo json_encode(["error" => "Failed to update resource."]);
        }
    }
}