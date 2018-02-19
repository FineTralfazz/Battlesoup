var playerId;
var gameStatus = {};
var placementStatus = {};

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
				direction = 0;
			} else if (lastX < currentX) {
				direction = 2;
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
				if (placementStatus['currentShipLength'] > 2) {
					placementStatus['currentShipLength']--;
					placementStatus['lastClick'] = undefined;
					setStatusMessage('Please place your next vegetable');
				} else {
					setStatusMessage('Vegetables placed successfully.')
				}
			} else {
				setStatusMessage('Invalid vegetable location');
			}
		});
	}
}

function drawTile(x, y, angle, url){
	console.log(`drawing ${url} to ${x}, ${y}`)
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
			drawTile(--x, y, -90, url);
		} else if (direction == 1){
			drawTile(x, y++, 0, url);
		} else if (direction == 2){
			drawTile(++x, y, 180, url);
		} else if (direction == 3){
			drawTile(x, --y, 90, url);
		}
	}

	
}

function updateGameStatus() {
	$.getJSON('/game_status', function(data) {
		gameStatus = data;
	});
}

function startGame(player) {
	playerId = player;
	$.getJSON('/start_game', {'player': player}, function(data) {
		$('#player-select').hide();
		$('#main-game').show();
		updateGameStatus();
		placementStatus['currentShipLength'] = '5';
		setStatusMessage('Please place your cucumber on the board.');
	})
}

function guess(e) {
	console.log(e);
	var x = e.target.dataset.column;
	var y = e.target.dataset.row;
	
}

$(function() {
	$('td').on('click', function(e) {
		if(gameStatus['phase'] == 'setup') {
			placeShip(e);
		} else {
			guess(e);
		}
	});
	setStatusMessage('test');
});