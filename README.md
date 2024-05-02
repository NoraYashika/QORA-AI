# QORA AI

## Announcement:
## Updates will be paused for an unknown time (possibly until Feburary 2024)

<div id = "div_data">
    <h2>Data</h2>
    <p>
        Current Version: 1.2.0 <a href = "./.github/updates.md">(update logs)</a><br>
        Start of project: around 06/2021<br>
        Recommended OS: Windows, may work on linux too, but with limited functionality
        You can find a guide <a href = "./.github/guide.md">here</a>.<br>
    </p>
</div>
 
# Planning
## General Planning
- [x] Making a usage guide 📖
- [x] Adding execution parameters 🧰🔧
- [ ] Making a GUI 🖥
- [ ] Making it cross-compatible with all operating systems, capable of using python ⚙
- [ ] <strong>possibly</strong> rewriting the System in an other language 🧰
- [ ] User Settings for more customizability (first with .ini file, later with GUI >> see in GUI update)

## Making importable Modules 🧩
- [x] a time module, to tell the current time and date. ⏲📅
- [ ] a translation plugin, to make it able to communicate with the user in a set language 🅰➡🅱
- [ ] a translator module, to make it able to translate from one language into another set language 🅰➡🅱
- [ ] a module to evaluate data and make rough predictions 💭
- [ ] a tts module 🗣

## Planning regarding the neural network 
- [ ] Fixing the non-fatal errors on execution of training.py 🛠
- [x] Adding calculation of average accuracy 📊
- [ ] making it learn from user input and mistakes 👍👎
- [ ] a way to take out any bias out of the network 🧠
- [ ] increasing the accurracy and taking out interpretation errors ❌

The file "intents.json" is constantly being updated to increase the vocabulary of the neural network and I <strong>try</strong> to release Updates for it on a bi-weekly basis. 🔄

if you have any requests or ideas, open an issue, I am all ears!! 😀

## About
This project started in 2021, originally as a way to learn about <a href = "https://www.tensorflow.org/">Tensorflow</a> and AI/Machine Learning in general. Later on I started to expanding it and after a year I rediscovered it and thought to myself "Why do I not work on it again, since it was so much fun when I last did it?". So, here I am.

## What do the version numbers mean, in this repo?
<p>
    The number is composed of three digits:
    <ol>
        <li> the first digit is the counter of major updates, like important implementations etc
        <li> the second digit is the number, displaying how many minor updates were done, during the period of the current major update</li>
        <li> the last digit show the bug fixes and basically unnecessary updates, like design etc</li>
    </ol>
    <h3> Example:</h3>
    <p>
        Version 1.12.56<br><br>
        This is quite the extreme example, but this means that the program is in the period of major update 1, minor update 12 and the newest version is the 56th bugfix.
    </p>
    <h3>Where do I find the current Version?</h3>
    <p> It is at the very top under the section <a href = "#div_data">Data</a>.
    <h3>What does it mean, when there is something behind the version?</h3>
    <p>
        That is something rare and will only appear in certain cases. I'll explain it with the previous version example (1.12.56):
        <ul>
            <li>1.12.56: nothing means, it is a stable release and there are no expected bugs.</li>
            <li>1.12.56<strong><em>t</em></strong>: '<strong><em>t</em></strong>' stands for "testing" and is not a stable release, until it is removed.</li>
            <li>1.12.56<strong><em>d</em></strong>: '<strong><em>d</em></strong>' stands for "discontinued" and there won't be a bugfix until the next minor/major update</li>
            <li>1.12.56<strong><em>a</em></strong>: '<strong><em>a</em></strong>' stands for "alpha" and with that it means, it is a candidate for becoming a stable release, but bugs are expected and to be reported as a thread.
        </ul>
    </p>
</p>
