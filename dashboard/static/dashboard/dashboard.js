function toggleTable() {
    const table = document.getElementById("usersTable");
        
    if (table.style.display === "none") {
                table.style.display = "block";
    } else {
                table.style.display = "none";
    }
}