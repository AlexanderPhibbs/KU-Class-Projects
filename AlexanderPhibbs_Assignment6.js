//Alexander Phibbs
//EECS 468 Assignment 6
//4-11-24
//Description: This code creates a server using node js and java script, this server can handle different requests such as
//GET,PUT,DELETE,MKCOL, and error handling, this will have output specific to the console terminal for each of the methods depending
//on the specific input used, there will be a PDF Attached that will document the test cases and what exactly the steps and reasoning where to
//get here.

//Import necessary modules for the HTTP server, file system, and URL parsing
const http = require('http');        //HTTP module to handle requests and responses
const fs = require('fs');            //File System module to interact with files and directories
const path = require('path');        //Path module for managing and resolving file paths
const url = require('url');          //URL module to parse incoming URLs

//Defines the port number where the server will listen
const port = 3000;

//Creates an HTTP server that listens for requests
const server = http.createServer((req, res) => {
    //Parses the URL from the request to extract the file path
    const reqUrl = url.parse(req.url, true);  //Parses the URL and allow query string parsing
    const filePath = path.join(__dirname, reqUrl.pathname);  //Creates an absolute file path from the URL
    const method = req.method;  //Gets the HTTP method (GET, PUT, DELETE, MKCOL)

    //Sets common headers for the response
    res.setHeader('Content-Type', 'text/plain');  //Responses will be plain text
    res.setHeader('Access-Control-Allow-Origin', '*'); //Enables CORS for all origins

    //Checks the HTTP method and handle the request accordingly

    if (method === 'GET') {
        //Handles GET requests (reads a file from the server)
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                //If the file doesn't exist, respond with a 404 error
                if (err.code === 'ENOENT') {
                    res.statusCode = 404;  //The status code reads Not Found
                    res.end('File not found');  //Send's file not found message
                } else {
                    //If there is a server error, respond with a 500 error
                    res.statusCode = 500;  //The status code reads Internal Server Error
                    res.end('Error reading file');  //Send's error message
                }
            } else {
                //If the file is read successfully, sends the content with a 200 OK response
                res.statusCode = 200;  //The status code reads OK
                res.end(data);  //Sends the file contents as the response body
            }
        });

    } else if (method === 'PUT') {
        //Handles PUT requests (writes data to a file)
        let body = '';  //Initializes a variable to collect the incoming data from the request body
        
        //Collects the incoming data chunks
        req.on('data', chunk => {
            body += chunk;  //Appends each chunk of data to the body variable
        });

        //If all data is collected, write it to the file
        req.on('end', () => {
            //Writes the data to the specified file path
            fs.writeFile(filePath, body, 'utf8', (err) => {
                if (err) {
                    //If there's an error writing to the file, respond with a 500 error
                    res.statusCode = 500;  //The status code reads Internal Server Error
                    res.end('Error writing file');  //Sends an error message
                } else {
                    //If the file is successfully written, respond with a 201 status code
                    res.statusCode = 201;  //The status code reads Created
                    res.end('File created or updated');  //Sends a success message
                }
            });
        });

    } else if (method === 'DELETE') {
        //Handles DELETE requests (deletes a file)
        fs.unlink(filePath, (err) => {
            if (err) {
                //If the file doesn't exist or there's an error, respond with a 404 error
                if (err.code === 'ENOENT') {
                    res.statusCode = 404;  //The status code reads Not Found
                    res.end('File not found');  //Sends a file not found message
                } else {
                    //If there is a server error, respond with a 500 error
                    res.statusCode = 500;  //The status code reads Internal Server Error
                    res.end('Error deleting file');  //Sends an error message
                }
            } else {
                //If the file is deleted successfully, respond with a 200 status code
                res.statusCode = 200;  //The status code reads OK
                res.end('File deleted');  //Sends a success message
            }
        });

    } else if (method === 'MKCOL') {
        //Handles MKCOL requests (create a directory, WebDAV standard)
        fs.mkdir(filePath, { recursive: true }, (err) => {
            if (err) {
                //If there is an error creating the directory, respond with a 500 error
                res.statusCode = 500;  //The status code reads Internal Server Error
                res.end('Error creating directory');  //Sends an error message
            } else {
                //If the directory is created successfully, respond with a 201 status code
                res.statusCode = 201;  //The status code reads Created
                res.end('Directory created');  //Sends a success message
            }
        });

    } else {
        //Handles unsupported HTTP methods by returning a 405 Method Not Allowed error
        res.statusCode = 405;  //The status code reads Method Not Allowed
        res.end(`The method ${method} is not supported.`);  //Sends message indicating the unsupported method
    }
});

//Starts the server and listen for incoming requests on port 3000
server.listen(port, () => {
    console.log(`Server listening on port ${port}`);  //Log to the console when the server starts
});
