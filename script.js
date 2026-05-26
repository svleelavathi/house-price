function predictPrice() {

    let size = document.getElementById("size").value;
    let bedrooms = document.getElementById("bedrooms").value;
    let age = document.getElementById("age").value;

    // Simple fake linear regression formula
    let price = (size * 200) + (bedrooms * 10000) - (age * 5000);

    document.getElementById("result").innerText =
        "Predicted Price: ₹ " + price;
}