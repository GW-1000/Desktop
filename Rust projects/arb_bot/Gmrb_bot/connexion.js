const WebSocket = require('ws');
const websocketUrl = 'wss://wss.betphoenix.info/ws/'; 
//create a new websocket connexion
const socket = new WebSocket(websocketUrl);
function tournamentRequest(trnm, onMessageCallback){
    //when the web connexion opens
    socket.on ('open', function() {
        console.log('web connexion established');

        //First send the authentication request with the locale and language set to haitian creole
        const authRequest = {
            "key": "demo",     
            "token": "demo",
            "partnerId": "paryajpam",
            "lang": "HT",         
            "ln": "ht",          
            "tree": false,        
            "hot": false          
        };

        socket.send(JSON.stringify(authRequest));
        console.log('authentication request sent');

        // Wait for a brief moment before sending the next request
        setTimeout(() => {

                // Second: Send the request to fetch event data, including necessary filters
                const eventRequest = {
                    "action": "events",      // Action to fetch events
                    "level": 3,              // Level (use 3 as per your data)
                    "trnm": trnm,  // Tournament ID (replace if needed)
                    "mcount": 2,             // Market count (2 as per your data)
                    "filter": {
                        "notempty": true     // Filter to get only non-empty results
                    },
                    "marker": "sport",       // Marker (use sport as per your data)
                    "config": {              // Config object to replicate the website's settings
                        "url": "dict/ht.json", // Locale file for Creole
                        "method": "get",      // HTTP method to use for this
                        "headers": {
                            "Accept": "application/json, text/plain, */*" // Set headers for content type
                        },
                        "transformRequest": [null],
                        "transformResponse": [null],
                        "timeout": 0,         // No timeout
                        "xsrfCookieName": "XSRF-TOKEN",
                        "xsrfHeaderName": "X-XSRF-TOKEN",
                        "maxContentLength": -1,
                        "maxBodyLength": -1,
                        "transitional": {
                            "silentJSONParsing": true,
                            "forcedJSONParsing": true,
                            "clarifyTimeoutError": false
                        }
                    }
                };

                // Send the event request after the authentication
                socket.send(JSON.stringify(eventRequest));
                console.log('Event request sent');

                
            }, 1000); 
            
    })
    //handle incoming messages 
    socket.on('message', (data) => {
        const message = JSON.parse(data);

        //filter messages: only handle "events" messages
        if (message.action === "events" && message.result === true) {
            onMessageCallback(message.data);// process event data to get gameIds 
        }else{
            console.log('Non event message received, ignoring.')
        }
        
    }); 

    

    //handle websocket error 
    socket.on('error', (error) => {
        console.error('WebSocket error:', error);
    });

    return socket;

}



module.exports = { tournamentRequest };
