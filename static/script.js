function startCamera() {
    fetch('/start_camera').then(() => {
        document.getElementById("video").src = "/video_feed";
        document.getElementById("status").innerText = "Status: Running";
    });
}

function stopCamera() {
    fetch('/stop_camera').then(() => {
        document.getElementById("video").src = "";
        document.getElementById("status").innerText = "Status: Stopped";
    });
}

// Fetch violations every 2 sec
setInterval(() => {
    fetch('/get_violations')
    .then(res => res.json())
    .then(data => {
        let table = document.getElementById("violationsTable");
        if (!table) return;

        table.innerHTML = "";

        data.forEach(row => {
            let tr = `<tr>
                <td>${row[0]}</td>
                <td>${row[1]}</td>
                <td>₹${row[2]}</td>
                <td>${row[3]}</td>
            </tr>`;
            table.innerHTML += tr;
        });
    });
}, 2000);