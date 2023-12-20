<h1>Usage Guide for QORA</h1>
<h2>Contents:</h2>
<ul>
    <li><a href = "#div_introduction">Introduction and explanation</a></li>
    <li><a href = "#div_quickstart">A guide to a quick start</a></li>
    <li><a href = "#div_setup">The guide to a less quicker start</a></li>
</ul>

<div id = "div_introduction">
    <h2>Introduction and explanation</h2>
    <h3>On execution of training.py...</h3>
    <p>
        ...the program creates a file, storing the words and classes in it as .pkl files (from the python module 'pickle')...<br>
        ...trains the neural network and stores it in a .keras file, since the AI uses a module called Keras from Tensorflow...<br>
        ...and stores them in the folder "network", which is empty on download, except the file .placeholder, which is there, otherwise it would not be included and that basically destroys the program.
    </p>
    <h3>On execution of QORA.py...</h3>
    <p>
        ...the program reads out the files in the "network" folder...<br>
        ...it initializes and infinite loop, taking the user input and if one was entered, it runs the input through the neural network...<br>
        ...and outputs the result.
    </p>
</div>

<div id = "div_quickstart">
    <h2>A guide to a quick start</h2>
    <ol>
        <li> Execute training.py with a double click and wait</li>
        <li> Execute QORA.py and start chatting </li>
    </ol>
</div>

<div id = "div_setup">
    <h2>The real guide with setup and the less quicker approach</h2>
    <ol>
        <li> open a cmd/terminal in the root folder, where the ai is located.</li>
        <li> Execute training.py with the following command:<br>
             `python training.py -epochs [amount of epochs, by default 100]` [execution parameters will be added in 1.2.0]
        </li>
        <li> Execute QORA.py with the command `python QORA.py`
    </ol>
</div>
