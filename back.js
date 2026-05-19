// server.js

const express = require("express");
const http = require("http");
const { Server } = require("socket.io");

const app = express();

const server = http.createServer(app);

const io = new Server(server, {
  cors:{
    origin:"*"
  }
});

const players = {};

io.on("connection", (socket)=>{

  console.log("Player connected:", socket.id);

  players[socket.id] = {
    x:0,
    y:1,
    z:0
  };

  socket.on("playerMove", (data)=>{

    players[socket.id] = data;

    io.emit("playersUpdate", players);
  });

  socket.on("disconnect", ()=>{

    delete players[socket.id];

    io.emit(
      "playerDisconnected",
      socket.id
    );

    console.log(
      "Player disconnected:",
      socket.id
    );
  });
});

server.listen(3000, ()=>{

  console.log(
    "Server running on port 3000"
  );
});