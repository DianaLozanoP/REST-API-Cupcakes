const BASE_URL = `http://127.0.0.1:5000/api/cupcakes`
const cupcakes_ul = $("#cupcakes_ul")

$("button").click(ShowAllCupcakes)

async function ShowAllCupcakes() {
    response = await axios.get(BASE_URL)
    console.log(response.data)
    let array_cup = response.data.cupcakes
    for (let eachcup in array_cup) {
        console.log(array_cup[eachcup].flavor)
        cupcakes_ul.append(`<li class="list-group-item d-flex justify-content-between align-items-center">Flavor: ${array_cup[eachcup].flavor}, Size: ${array_cup[eachcup].size}, Rating: ${array_cup[eachcup].rating}. </li>`)
        cupcakes_ul.append(`<div class="image-parent">
        <img src="${array_cup[eachcup].image}" class="list-group-item d-flex justify-content-between align-items-center"> </img>
        </div><br>`)
    }
}

$("#cupcake-form").on("submit", HandleForm)

async function HandleForm(evt) {
    evt.preventDefault()
    let form = $("#cupcake-form")
    let input = $("input")
    console.log(input[1].value, input[2].value, input[3].value, input[4].value)
    let flavor = input[1].value
    let size = input[2].value
    let rating = input[3].value
    let image = input[4].value
    response = await axios.post(BASE_URL, {
        "flavor": flavor, "size": size,
        "rating": rating, "image": image
    })
    form[0].reset()
}