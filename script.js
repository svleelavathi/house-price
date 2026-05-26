function predictPrice() {

    let size = document.getElementById("size").value;
    let bedrooms = document.getElementById("bedrooms").value;
    let age = document.getElementById("age").value;

    let price = (size * 180) + (bedrooms * 12000) - (age * 4000);

    document.getElementById("result").innerText =
        "🏠 Estimated Price: ₹ " + price;
}
