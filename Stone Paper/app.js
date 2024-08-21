let userscore = 0;
let compscore = 0;

const choices = document.querySelectorAll('.choice');
const msg = document.querySelector('#msg');
const userpara = document.querySelector('#user-score');
const compara = document.querySelector('#comp-score');

const generate = () => {
    const options = ["rock", "paper", "scissors"];
    const rand = Math.floor(Math.random() * 3);
    return options[rand];
}

const gamedraw = () => {
    console.log("GAME DRAW");
    msg.innerText = "Game Draw";
    msg.style.backgroundColor = "#081b31";
}

const showwinner = (userwin,choiceId,compchoice) => {
    if (userwin) {
        userscore++;
        userpara.innerText = userscore;
        console.log("You win");
        msg.innerText = `You Win Your ${choiceId} beat ${compchoice}`;
        msg.style.backgroundColor = "green";
    }
    else {
        compscore++;
        compara.innerText = compscore;
        console.log("You Lose");
        msg.innerText = `You Lose Your ${choiceId} lost againts ${compchoice} move`;
        msg.style.backgroundColor = "red";
    }
}
const playgame = (choiceId) => {
    console.log("user Choice is " + choiceId);
    const compchoice = generate();
    console.log("computers choice is " + compchoice);

    if (choiceId == compchoice) {
        gamedraw();
    }
    else {
        let userwin = true;
        if (choiceId == "rock") {
            userwin = compchoice == "paper" ? false : true;
        } else if (choiceId == "paper") {
            userwin = compchoice == "scissors" ? false : true;
        }
        else {
            userwin = compchoice == "rock" ? false : true;
        }
        showwinner(userwin,choiceId,compchoice);
    }   
}

choices.forEach((choice) => {
    console.log(choice);
    choice.addEventListener("click", () => {
        const choiceId = choice.getAttribute("id");
        console.log(choiceId + " was clicked");
        playgame(choiceId);
    });
});