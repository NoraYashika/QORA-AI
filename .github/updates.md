<h1> - Version 1.0.0 - </h1>
<h3> Release: 19.12.2023 </h3>
<ul>
    <li>Creation of the repository</li>
        <ul>
            <li>Creation of directories and files</li>
        </ul>
</ul>

<h1> - Version 1.1.0 - </h1>
<h3> Release: 22.12.2023 </h3>
<ul>
    <li>New features:</li>
        <ul>
            <li><a href = "#exec_params">Adding execution parameters to training.py</a></li>
            <li><a href = "#avg_acc">Adding calculation of average accuracy</a>
        </ul>
</ul>

<div id = "exec_params">
    <h2>Execution Parameters</h2>
    <p>
        For more details see the <a href = "./guide.md">guide</a>.<br>
        Execution parameters are used in the shell, when starting the program. To see the available parameters, the definitions are documented there.
    </p>
</div>

<div id = "avg_acc">
    <h2>Average accuracy</h2>
    <p>
        Calculation of the average accuracy by getting the accuracy of every epoch and dividing it by the amounts of epochs. So the calculation looks like this:<br><br>
        accuracy<sub>total</sub> = accuracy<sub>epoch_1</sub> + ... + accuracy<sub>epoch_n</sub><br><br>
        accuracy<sub>average</sub> = accuracy<sub>total</sub> / amount of epochs<br><br>
        accuracy<sub>average</sub> / 100 = accuracy<sub>average in percent</sub>
    </p>
</div>

<h1>- Version 1.1.1 -</h1>
Fixed Percent calculation mistake.<br>
The corrected calculation:<br>
accuracy<sub>total</sub> = accuracy<sub>epoch_1</sub> + ... + accuracy<sub>epoch_n</sub><br><br>
accuracy<sub>average</sub> = accuracy<sub>total</sub> / amount of epochs<br><br>
accuracy<sub>average</sub> <ins>*</ins> 100 = accuracy<sub>average in percent</sub>