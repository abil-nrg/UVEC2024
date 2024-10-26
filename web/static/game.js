console.log(game_id)


async function fetch_board() {
    const response = await fetch("fetch_board_data_by_game_id/" + game_id);
    return response.json();
}


// Grid dimensions
const n = 12;
const m = 15;

// Function to convert string to RGB array
function parseColor(colorString) {
    return colorString.replace(/[()]/g, '').split(',').map(Number);
}

// Create the grid and render items
function createGrid(data) {
    const gridContainer = document.getElementById('grid');
    gridContainer.innerHTML = '';
    for (let row = 0; row < n; row++) {
        for (let col = 0; col < m; col++) {
            const cell = document.createElement('div');
            cell.className = 'cell';
            cell.setAttribute('data-x', col); // Set x coordinate
            cell.setAttribute('data-y', row); // Set y coordinate
            cell.addEventListener('click', handleCellClick); // Add click event listener
            gridContainer.appendChild(cell);
        }
    }

    // Draw items on the grid
    drawItems(data);
    displayTime(data);
}

function drawItems(data) {
    const cells = document.querySelectorAll('.cell');

    const direction_to_arrow = {
        "u": "⇧",
        "d": "⇩",
        "l": "⇦",
        "r": "⇨"
    }

        // Draw cats
        data.cats.forEach(cat => {
            const index = cat.y * m + cat.x; // Calculate index for grid
            const cell = cells[index];
            const [r, g, b] = parseColor(cat.colour);
            cell.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
            cell.textContent = "🐱" + direction_to_arrow[cat.direction];
        });
    
        // Draw homes
        data.homes.forEach(home => {
            const index = home.y * m + home.x; // Calculate index for grid
            const cell = cells[index];
            const [r, g, b] = parseColor(home.colour);
            cell.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
            cell.textContent = "🏠";
        });
    
        // Draw intersections
        data.intersections.forEach(intersection => {
            const index = intersection.y * m + intersection.x; // Calculate index for grid
            const cell = cells[index];
            cell.style.backgroundColor = 'yellow'; // Set color for intersections
            cell.textContent = direction_to_arrow[intersection.current_direction];
        });
    
        // Draw tunnel
        const tunnel = data.tunnel; // Already an object
        const tunnelIndex = tunnel.y * m + tunnel.x; // Calculate index for grid
        const tunnelCell = cells[tunnelIndex];
        tunnelCell.style.backgroundColor = 'white'; // Set color for tunnel
        tunnelCell.textContent = "🕳️"; 
    }

function displayTime(data) {
    const timeDisplay = document.getElementById('timeDisplay');
    timeDisplay.textContent = `Time: ${data.time}`; // Display the time
}

function handleCellClick(event) {
    console.log('Cell Clicked');

    const x = event.target.getAttribute('data-x');
    const y = event.target.getAttribute('data-y');

    const clickData = {
        x: parseInt(x, 10),
        y: parseInt(y, 10),
    };

    console.log('Clicked: ', x, ', ', y);

    // Send data to the server
    fetch('', {

    })
    .then(response => {

        return response.json();
    })
    .then(data => {
        console.log('Success:', data); 
    })
    .catch(error => {
        console.error('Error:', error); 
    });
}



async function initializeBoard() {
    const data = await fetch_board();
    console.log(data);
    createGrid(data); 
    setTimeout(() => {
        initializeBoard();
    }, 1000);
}

initializeBoard();