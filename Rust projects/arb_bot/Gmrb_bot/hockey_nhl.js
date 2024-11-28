const { request } = require('http');
const { tournamentRequest} = require('./connexion');
const fs = require('fs');
let allGameIds = [];
collectedGameData = [];
requestSent = 0;
const sportID1 = 7;
const sportID = "b3e0478a25a84d51955627231947e2be";
const tournamentID = "cbdd0859b503408cbf1cf910c32b1db0";

function handleMessage (data){
    const games = data[sportID1][sportID][tournamentID]
    if (!games){
        console.log('No games found for this tournament');
    }
    let gameIds = Object.keys(games);
    allGameIds.push(...gameIds)

   // console.log(`The game Ids are ${allGameIds}`)
    return allGameIds
}

function requestGameDataForAllGames(socket){
    allGameIds.forEach((gameId) => {
        const gameRequest = {
            "action": "events",
            "level": 2,
            "id": gameId,
            "filter": {
                "notempty": true
            },
            "marker": "event"
        };

        socket.send(JSON.stringify(gameRequest));
        console.log('game data request sent for:', gameId);
        requestSent++
    });
    socket.on('message', (data) => {
        const message = JSON.parse(data);
        if(message.action === "events" && message.result === true && message.data){
            gameData = message.data;
            console.log('Game data received');
            collectedGameData.push(gameData);
            saveGameDataToFile();
    }});
}



function saveGameDataToFile(){
    const jsonFilePath = './game_data3.json'
    try{
        fs.writeFileSync(jsonFilePath, JSON.stringify(collectedGameData, null, 2), 'utf-8');
        console.log(`Game data saved to ${jsonFilePath}`);
    } catch (error) {
        console.error('Error saving game data to file:', error);
    }
    

}



const socket = tournamentRequest(tournamentID, (data) => {
   const gameIds = handleMessage(data);
   console.log('the game Ids are :', gameIds)
   requestGameDataForAllGames(socket);
  
});


