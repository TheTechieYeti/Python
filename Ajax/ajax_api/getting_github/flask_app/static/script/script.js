// fetch("https://api.github.com/users/TheTechieYeti")
//     .then(response => response.json() )
//     .then(coderData => {
//     console.log(coderData) 
//     let coderName = coderData['name']
//     let coderFollowers = " has " + coderData['followers'] + " followers"
//     let coderAvatar = coderData['avatar_url']
//     console.log(coderName)
//     let ptag = document.querySelector('#name')
//     let img = document.querySelector('#avatar')
//     ptag.innerHTML = coderName + coderFollowers
//     img.src = coderAvatar
//     })
//     .catch(err => console.log(err) )


// async function getCoderData() {
//         // The await keyword lets js know that it needs to wait until it gets a response back to continue.
//         var response = await fetch("https://api.github.com/users/TheTechieYeti");
//         // We then need to convert the data into JSON format.
//         var coderData = await response.json();
//         return coderData;
//     }
//     // console.log(getCoderData());
function getuserinfo(){
    fetch("https://api.github.com/users/Michael-Choi")
    .then(response => response.json() )
    .then(coderData => {
    console.log(coderData) 
    let coderName = coderData['name']
    let coderFollowers = " has " + coderData['followers'] + " followers"
    let coderAvatar = coderData['avatar_url']
    console.log(coderName)
    let ptag = document.querySelector('#name')
    let img = document.querySelector('#avatar')
    ptag.innerHTML = coderName + coderFollowers
    img.src = coderAvatar
    })
    .catch(err => console.log(err) )
}
function search(){
    let user_input = document.querySelector('#input')
    let search_data = user_input.value
    console.log(search_data)
    fetch(`https://api.github.com/users/${search_data}`)
    .then(response => response.json() )
    .then(coderData => {
    console.log(coderData) 
    let coderName = coderData['name']
    let coderFollowers = " has " + coderData['followers'] + " followers"
    let coderAvatar = coderData['avatar_url']
    console.log(coderName)
    let ptag = document.querySelector('#name')
    let img = document.querySelector('#avatar')
    ptag.innerHTML = coderName + coderFollowers
    img.src = coderAvatar
    })
    .catch(err => console.log(err) )
}

    