///////////////////////////////////////////////////
//           Constants & variables               //
///////////////////////////////////////////////////
let logoutButton = document.querySelector('.logout');
let message = document.querySelectorAll('.messageOut');
let num_form = document.querySelector('#frmIdentifier').value;
console.log("num_form: ", num_form);
let passRegister = document.querySelector('#password');
let confPassRegister = document.querySelector('#confpass');
let passLogin = document.querySelector('#logPass');
let showPassRegister = document.querySelector('#showPassRegister');
let showConfPassRegister = document.querySelector('#showConfPassRegister');
let showPassLogin = document.querySelector('#showPassLogin');
let skillSelected = document.querySelector('.skillSelected');

let iconLanguages = document.querySelector('.iconLanguages');
let count = 0
let updateForm = document.querySelector('#updateDeveloper');
let updateFormFrameworks = document.querySelector('#updateDevFrameworks');
let addFrmPositions = document.querySelector('#frmAddPosition');
let errorMessages = document.querySelectorAll('.errorMessages');
let progressBar = document.querySelector('.progress-bar');

//$('.progress-bar').attr('width', )
porcentaje=0
//progressBar.style.width = porcentaje+'%'
//progressBar.atrr('aria-valuenow', 0)


///////////////////////////////////////////////////
//       Asigning time out for flash messages    //
///////////////////////////////////////////////////

setTimeout(function () {
    $('.messageOut').attr('style', 'display:none;');
}, 5000);

////////////////////////////////////////////////////
//       Close session process/event              //
////////////////////////////////////////////////////

function closeSession(event) {

    let URL = '/logout';
    let settings = {
        method: 'GET'
    }

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json()
            }
        })
        .then(data => {
            console.log(data)
            window.location.href = '/';
        });
}



///////////////////////////////////////////////////
//       Toggle show/hide password               //
///////////////////////////////////////////////////


let togglePassRegister = (e) => {
    if (showPassRegister.textContent === 'Show') {
        showPassRegister.textContent = 'Hide';
        passRegister.setAttribute('type', 'text');
    } else {
        showPassRegister.textContent = "Show";
        passRegister.setAttribute('type', 'password');
    }
}

let toggleConfPassRegister = (e) => {
    if (showConfPassRegister.textContent === 'Show') {
        showConfPassRegister.textContent = 'Hide';
        confPassRegister.setAttribute('type', 'text');
    } else {
        showConfPassRegister.textContent = "Show";
        confPassRegister.setAttribute('type', 'password');
    }
}

let togglePassLogin = (e) => {
    if (showPassLogin.textContent === 'Show') {
        showPassLogin.textContent = 'Hide';
        passLogin.setAttribute('type', 'text');
    } else {
        showPassLogin.textContent = "Show";
        passLogin.setAttribute('type', 'password');
    }
}

function select(e) {

    if (count == 0) {
        skillSelected.innerHTML = ""
    }

    if (count < 5) {
        let iconSelected = iconLanguages.removeChild(e)
        skillSelected.appendChild(iconSelected)
        console.log("aqui", skillSelected)
        porcentaje+=20
        progressBar.style.width = porcentaje+'%'
        progressBar.innerHTML=porcentaje+'%'
        count++
    }

}

skillsRequired = []

function oncheck(e) {

    if (count < 5) {

        if (!(skillsRequired.includes(e.nextElementSibling.value))) {

            e.classList.add("iconSelected")
            count++;
            skillsRequired.push(e.nextElementSibling.value);
            console.log(skillsRequired);
            console.log("count: ",count)
            porcentaje+=10
            console.log(porcentaje)
            progressBar.style.width = porcentaje+'%'
            //progressBar.atrr('aria-valuenow', porcentaje)

           
        } else {

            e.classList.remove("iconSelected")
            count--;

            index = skillsRequired.indexOf(e.nextElementSibling.value)

            skillsRequired.splice(index, 1);
            console.log(skillsRequired);
            console.log("count: ",count)
            

        }

    }

}


function addPosition(event) {
    event.preventDefault();


    let data = {
        id_organization: event.target.idOrg.value,
        languages: skillsRequired,
        namePos: event.target.namePos.value,
        descriptionPos: event.target.descriptionPos.value

    };

    let URL = "http://127.0.0.1:5000/position/add";
    let settings = {
        method: 'POST',
        body: JSON.stringify(data)
    };

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
        })
        .then(result => {
            console.log(result);

            window.location.href = '/dashboard/organization';
            
        })
        .catch(error => {
            console.log(error)

        });
}





function updateDeveloper(event) {
    event.preventDefault();

    progressBar.setAttribute("style", "100%")
    progressBar.getAttribute('aria-valuenow', 100)

    tempLanguages = []
    let skillAct = document.querySelectorAll('.skillSelected .skill .langId')

    if (typeof skillAct[0] == "undefined") {
        temp1 = 99
    } else {
        tempLanguages.push(skillAct[0].getAttribute("value"))
    }

    if (typeof skillAct[1] == "undefined") {
        temp2 = 99
    } else {
        tempLanguages.push(skillAct[1].getAttribute("value"))
    }

    if (typeof skillAct[2] == "undefined") {
        temp3 = 99
    } else {
        tempLanguages.push(skillAct[2].getAttribute("value"))
    }

    if (typeof skillAct[3] == "undefined") {
        temp4 = 99
    } else {
        tempLanguages.push(skillAct[3].getAttribute("value"))
    }

    if (typeof skillAct[4] == "undefined") {
        temp5 = 99
    } else {
        tempLanguages.push(skillAct[4].getAttribute("value"))
    }



    let data = {
        id_developer: event.target.id_developer.value,
        languages: tempLanguages,
        biography: event.target.biography.value

    };

    let URL = "http://127.0.0.1:5000/developer/update";
    let settings = {
        method: 'PUT',
        body: JSON.stringify(data)
    };

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
        })
        .then(result => {
            console.log(result);
            window.location.href = '/developer/editFrame';
        })
        .catch(error => {
            console.log(error)
        });
}


function updateDevFrameworks(event) {
    event.preventDefault();

   

    tempFrameworks = []
    let skillAct = document.querySelectorAll('.skillSelected .skill .langId')

    if (typeof skillAct[0] == "undefined") {
        temp1 = 99
    } else {
        tempFrameworks.push(skillAct[0].getAttribute("value"))
    }

    if (typeof skillAct[1] == "undefined") {
        temp2 = 99
    } else {
        tempFrameworks.push(skillAct[1].getAttribute("value"))
    }

    if (typeof skillAct[2] == "undefined") {
        temp3 = 99
    } else {
        tempFrameworks.push(skillAct[2].getAttribute("value"))
    }

    if (typeof skillAct[3] == "undefined") {
        temp4 = 99
    } else {
        tempFrameworks.push(skillAct[3].getAttribute("value"))
    }

    if (typeof skillAct[4] == "undefined") {
        temp5 = 99
    } else {
        tempFrameworks.push(skillAct[4].getAttribute("value"))
    }



    let data = {
        id_developer: event.target.id_developer.value,
        frameworks: tempFrameworks,
    };

    let URL = "http://127.0.0.1:5000/developer/updateFrameworks";
    let settings = {
        method: 'PUT',
        body: JSON.stringify(data)
    };

    fetch(URL, settings)
        .then(response => {
            if (response.ok) {
                return response.json();
            }
        })
        .then(result => {
            console.log(result);
            window.location.href = '/dashboard/developer';
        })
        .catch(error => {
            console.log(error)
        });
}



///////////////////////////////////////////////////
//       Asigning events to buttons              //
///////////////////////////////////////////////////

if (num_form == 4) {
    updateForm.addEventListener('submit', updateDeveloper)
}

if (num_form == 8) {
    addFrmPositions.addEventListener('submit', addPosition)

}

if (num_form == 5) {
    updateFormFrameworks.addEventListener('submit', updateDevFrameworks)
}

if (num_form == 4 || num_form == 5 || num_form == 6 || num_form == 7 || num_form == 8) {
    logoutButton.addEventListener('click', closeSession);

}

if (num_form == 1 || num_form == 11) {

    showPassLogin.addEventListener('click', togglePassLogin);

}

if (num_form == 3 || num_form == 12) {
    showPassRegister.addEventListener('click', togglePassRegister);
    showConfPassRegister.addEventListener('click', toggleConfPassRegister);

}