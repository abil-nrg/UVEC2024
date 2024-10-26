// const data = {
//     "cats": [
//         {"colour": "(0, 0, 255)", "direction": "r", "x": 1, "y": 1, "size": 20},
//         {"colour": "(0, 255, 0)", "direction": "d", "x": 5, "y": 1, "size": 20}
//     ],
//     "homes": [
//         {"colour": "(0, 0, 255)", "x": 10, "y": 1, "size": 40},
//         {"colour": "(0, 255, 255)", "x": 4, "y": 1, "size": 40}
//     ],
//     "intersections": [
//         {"x": 8, "y": 1, "possible_direction": ["r", "d"], "current_direction": "d", "user": "None", "size": 40}
//     ],
//     "tunnel": {"x": 1, "y": 1, "size": 50}, // Changed to object
//     "ticks_since_last_cat": 60,
//     "time": 50
// };

const data = {
    "cats": [
        {"colour": "(0, 0, 255)", "direction": "r", "x": 2, "y": 5},
    ],
    "homes": [
        {"colour": "(0, 0, 255)", "x": 7, "y": 1},
        {"colour": "(0, 255, 255)", "x": 7, "y": 10}
    ],
    "intersections": [
        {"x": 7, "y": 5, "possible_direction": ["u", "d"], "current_direction": "d", "user": "None"}
    ],
    "tunnel": {"x": 1, "y": 5},
    "ticks_since_last_cat": 0,
    "time": 0
};

// Grid dimensions
const n = 12;
const m = 15;

// Function to convert string to RGB array
function parseColor(colorString) {
    return colorString.replace(/[()]/g, '').split(',').map(Number);
}

// Create the grid and render items
function createGrid() {
    const gridContainer = document.getElementById('grid');

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
    drawItems();
    displayTime();
}

function drawItems() {
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
    tunnelCell.style.backgroundColor = 'purple'; // Set color for tunnel
    tunnelCell.textContent = "🕳️"; // Optional: Display a "T" for tunnel
}

function displayTime() {
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
    fetch('https://your-server-endpoint.com/click', { // Replace with your server endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(clickData)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:', data); // Handle success
    })
    .catch(error => {
        console.error('Error:', error); // Handle error
    });
}

// Initialize the grid
createGrid();
