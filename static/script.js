document.getElementById('allocateForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const size = e.target.elements.size.value;

    fetch('/allocate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `size=${size}`
    })
    .then(response => response.json())
    .then(data => updateVisualization(data.blocks));
});

document.getElementById('freeForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const size = e.target.elements.size.value;

    fetch('/free', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: `size=${size}`
    })
    .then(response => response.json())
    .then(data => updateVisualization(data.blocks));
});

function updateVisualization(blocks) {
    const linkedListDiv = document.getElementById('linkedList');
    linkedListDiv.innerHTML = '';

    blocks.forEach((block, index) => {
        const blockDiv = document.createElement('div');
        blockDiv.className = `block ${block.is_free ? 'free' : 'allocated'}`;
        blockDiv.textContent = block.size;
        linkedListDiv.appendChild(blockDiv);

        if (index < blocks.length - 1) {
            const arrowDiv = document.createElement('div');
            arrowDiv.className = 'arrow';
            linkedListDiv.appendChild(arrowDiv);
        }
    });
}
