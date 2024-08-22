document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll('.box');
    const resultInput = document.getElementById('result');

    let currentInput = '';

    // Handle button clicks
    buttons.forEach(button => {
        button.addEventListener('click', function () {
            handleInput(this.textContent);
        });
    });

    // Handle keyboard input
    document.addEventListener('keydown', function (event) {
        const key = event.key;
        
        if (isValidKey(key)) {
            handleInput(key);
        } else if (key === 'Enter') {
            handleInput('=');
        } else if (key === 'Escape') {
            handleInput('Clear');
        }
    });

    // Function to process the input
    function handleInput(value) {
        if (value === 'Clear') {
            // Clear the display
            currentInput = '';
            resultInput.value = '';
        } else if (value === '=') {
            // Evaluate the expression
            try {
                currentInput = eval(currentInput);
                resultInput.value = currentInput;
                resultInput.classList.remove('animateResult');
                void resultInput.offsetWidth;  // Trigger reflow
                resultInput.classList.add('animateResult');
            } catch (error) {
                resultInput.value = 'Error';
            }
        } else {
            // Append the button value to the current input
            currentInput += value;
            resultInput.value = currentInput;
            resultInput.classList.remove('animateResult');
            void resultInput.offsetWidth;  // Trigger reflow
            resultInput.classList.add('animateResult');
        }
    }

    // Function to validate keys that can be used in the calculator
    function isValidKey(key) {
        return ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '%'].includes(key);
    }
});
