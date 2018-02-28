var playerId;
var gameStatus = {};
var placementStatus = {};
var hits = 0;

function setStatusMessage(message) {
	$('#status-message').text(message);
}

function placeShip(e) {
	var currentX = e.target.dataset.column;
	var currentY = e.target.dataset.row;
	if(placementStatus['lastClick'] == undefined) {
		placementStatus['lastClick'] = {};
		placementStatus['lastClick']['x'] = currentX;
		placementStatus['lastClick']['y'] = currentY;
	} else {
		var lastX = placementStatus['lastClick']['x'];
		var lastY = placementStatus['lastClick']['y'];
		var direction;
		if (lastX == currentX) {
			if (lastY > currentY) {
				direction = 0;
			} else if (lastY < currentY) {
				direction = 2;
			} else {
				setStatusMessage('Invalid location for vegetable.');
			}
		} else if (lastY == currentY) {
			if (lastX > currentX) {
				direction = 3;
			} else if (lastX < currentX) {
				direction = 1;
			} else {
				setStatusMessage('Invalid location for vegetable.');
			}
		} else {
			setStatusMessage('Invalid location for vegetable.');
		}
		var args = {
			'player': playerId,
			'length': placementStatus['currentShipLength'],
			'x': lastX,
			'y': lastY,
			'direction': direction
		}
		$.getJSON('/place', args, function(data) {
			if (data['success']) {
				drawVeggies(lastX, lastY, placementStatus['currentShipLength'], direction);
				if (placementStatus['currentShipLength'] > 2) {
					placementStatus['currentShipLength']--;
					placementStatus['lastClick'] = undefined;
					setStatusMessage('Please place your next vegetable');
				} else {
					setStatusMessage('Vegetables placed successfully. Waiting for other player.');
					waitForGameStart();
				}
			} else {
				setStatusMessage('Invalid vegetable location');
			}
		});
	}
}
function clearBoard(){
	$('td').css('background-image', '');
}
function waitForGameStart() {
	updateGameStatus();
	if (gameStatus['phase'] == 'play') {
		setStatusMessage(`Game started. It is player ${gameStatus['turn']}'s turn.`);
		clearBoard();
	} else {
		setTimeout(waitForGameStart, 1000);
	}
}
function randInt(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min +1)) + min;
}

function	drawHit(x, y, length){
	var imagePrefix;
	var randAngle;
	var randVeggie;

	if (length == 5){
		imagePrefix = "cuc";
	} else if (length == 4){
		imagePrefix = "cel";
	} else if (length == 3){
		imagePrefix = "car";
	} else if (length == 2){
		imagePrefix = "broccoli"
	}

	randAngle = randInt(0, 3) * 90;
	randVeggie = randInt(0, length-1);

	var url = `/static/img/${imagePrefix}${randVeggie}.png`;
	drawTile(x, y, randAngle, url);

}

function displayWin(){
	$('#win-banner').show();
	$("#status-message").hide();
	setInterval(function(){
		$('#main-game').toggle()
	},1000)
}

function drawTile(x, y, angle, url){
	var tile = $(`[data-column=${x}][data-row=${y}]`);
	tile.css('background-image', `url(${url})`);
	tile.css('background-size', 'contain');
	tile.css('transform', `rotate(${angle}deg)`);
	// tile.css('background-color', 'white')
}

function drawVeggies(x, y, length, direction){
	var imagePrefix;
	if (length == 5){
		imagePrefix = "cuc";
	} else if (length == 4){
		imagePrefix = "cel";
	} else if (length == 3){
		imagePrefix = "car";
	} else if (length == 2){
		imagePrefix = "broccoli"
	}


	for ( var i = 0;  i<length; i++){
		var url = `/static/img/${imagePrefix}${i}.png`;
		if (direction == 0){
			drawTile(x, y--, 270, url);
		} else if (direction == 1){
			drawTile(x++, y, 0, url);
		} else if (direction == 2){
			drawTile(x, y++, 90, url);
		} else if (direction == 3){
			drawTile(x--, y, 180, url);
		}
	}
}

function updateGameStatus() {
	$.getJSON('/game_status', function(data) {
		var lastPlayer = gameStatus['turn']
		gameStatus = data;
		if (gameStatus['turn'] != lastPlayer){
			setStatusMessage(`It is player ${gameStatus['turn']}'s turn.`);
		}
	});
}

function startGame() {
	$.getJSON('/start_game')
}

function joinGame(player) {
	playerId = player;
	$('#player-select').hide();
	$('#main-game').show();
	updateGameStatus();
	placementStatus['currentShipLength'] = '5';
	setStatusMessage('Please place your cucumber in the soup.');
}

function guess(e) {								//should I use this?
	//console.log(e);
	var pea = `/static/img/pea.png`
	var curx = e.target.dataset.column;
	var cury = e.target.dataset.row;

	var args = {
		'player': playerId,
		'x': curx,
		'y': cury,
	}
	if (gameStatus['turn']==playerId)
	{
		$.getJSON('/guess', args, function(data){
			if (data['hit'] == true){
				setStatusMessage('Thats a hit dawg');
				drawHit(curx, cury, data['length']);
				++hits;
				if (hits == 14){
					displayWin();
				}
			} else if (data['hit'] == false){
				drawTile(curx, cury, 180, pea);
				setStatusMessage('Yup thats a pea');
			}
			updateGameStatus();
		});
	}
	else{
		setStatusMessage('Not your turn buddy');
	}
}

$(function() {
	$('td').on('click', function(e) {
		if(gameStatus['phase'] == 'setup') {
			placeShip(e);
		} else {
			guess(e);
		}
	});
	setInterval(updateGameStatus, 1000);
});
