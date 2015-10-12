"use strict";
// version: 2015-05

var currentLocation = window.location.host;
/*
Libs pour l'envoie et la réception de json entre le client et le serveur ElipssWebSocket

-- Instancie l'objet ElipssWebSocket avec en paramètre:
	-la callback (le message que l'on va recevoir)
	-le port (ex 8080,8081)
	-la room (par défaut l'url actuel)

Function disponible :
	-sendMessage --> prend en paramètre le message crée au dessus et l'envoie au serveur ARG: message

EX : 

var callback = function(evt){jQuery.parseJSON(console.log(evt.data))};
var socketA = new Zephclient();
socketA.send("echo",{toto:toto});
*/
function Zephclient(session, url, room, messageCallback){
	var self = this;
	room = typeof room !== 'undefined' ? room : window.location.href;
	url = typeof url !== 'undefined' ? url : 'ws://' + currentLocation + "/ws" ;
	self.webSocket = new WebSocket(url);
	self.room = room;
	self.callbackTable = {};

	setInterval(function(){ self.send('TaskPing',{}) }, 45000);
	self.init = function()
	{
		var session_id = session
		this.webSocket.onopen = function (event) 
		{
			//send the url to identify in which room the user is when the connection open.
			this.send(JSON.stringify({ session_id: session_id,room : self.room })); 
			
		};
		if (messageCallback !== undefined && messageCallback !== null)
		{
			self.webSocket.onmessage = messageCallback;
		}
		else
		{
			self.webSocket.onmessage = self.defaultCallBack
		}
	}

	//default callback if the user do not overide the main callback
	self.defaultCallBack = function(event)
	{
		data = JSON.parse(event.data);
		if(self.callbackTable[data.task] != undefined)
		{
			for(var i = 0; i < self.callbackTable[data.task].length; i++)
			{
				if(self.callbackTable[data.task][i] != undefined)
				{
					self.callbackTable[data.task][i](data);
				}
			}
		}

	};

	/**
	* suscribe to a task if the default callback is not overriden
	* task : the name of the task you are waiting
	* callback : the callback to call when this task speaks
	*/
	self.suscribe = function(task, callback)
	{
		if(self.callbackTable[task] != undefined)
		{
			self.callbackTable[task].push(callback);
		}
		else
		{
			self.callbackTable[task] = [];
			self.callbackTable[task].push(callback);
		}
	};

	/**
	* unsuscribe from a task if the default callback is not overriden
	* task : the name of the task
	* callback : the callback to remove 
	*/
	self.unsuscribe = function(task, callback)
	{
		if(self.callbackTable[task] != undefined)
		{
			for(var i = 0; i < self.callbackTable[task]; i++)
			{
				if(self.callbackTable[task][i] == callback)
				{
					delete self.callbackTable[task][i];
					break;
				}
			}
		}
	}

	/**
	* private
	*/
	self.sendMessage = function(message){ 
		if (self.webSocket.readyState === 1) 
		{
			self.webSocket.send(JSON.stringify(message));
			return;
		}
		else
		{
			setTimeout(function(){self.sendMessage(message)},10);
		}
	};

	/**
	* send data to the task via the websocket
	*/
	self.send = function(task, data){ 
		var message = { 
				task: task,
				data: data,
				room : self.room,
				session_id: session,
				date: Date.now()
			};
		console.log(message);
		self.sendMessage(message);
	};
	
	self.init();
}
