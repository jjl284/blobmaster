# Python 3 Joueur Client

This is the client for the [Cadre AI framework][cadre]. It can play multiple different games, though you will probably only be interested in one at a time.

In general, try to stay out of the `joueur/` folder, it does most of the heavy lifting to play on our game servers. Your AI, and the game objects it manipulates are all in `games/game_name/`, with your very own AI living in `Games/game_name/ai.py` for you to make smarter.

## How to Run

This client has been tested and confirmed to work on Debian 9 machines, but it can work on your own Windows/Linux/Mac machines if you desire.

### Linux

```
./testRun MyOwnGameSession
```

For Linux, a recent version of `python3` should work. It has been tested on 3.4.3 extensively, but should work with >= 3.2. The normal 'python' usually refers to Python 2.7.X, so make sure you have the python**3** installed.

### Windows

On Windows you'll need some version of Python 3. As with the Linux version, [3.4.3][343] has been tested against extensively, however there's no known reason why it would not work on newer versions. Install that and ensure that python is set up in your Environmental Variables as 'python3', then

```
python3 main.py blobmaster -s game.codegames.ai -r MyOwnGameSession
```

## Make

There is a `Makefile` provided. Although Python is an interpreted language, we have added some useful default steps. By default it installs all pip packges you add to `requirements.txt`, and then runs the Python compiler on all .py files to make sure they are syntactically correct.

## Other Notes

### Modifying Our Game Files

The only file you should ever modify to create your AI is the `ai.py` file. All the other files are needed for the game to work. In addition, you should never be creating your own instances of the Game's classes, nor should you ever try to modify their variables. Instead, treat the Game and its members as a read only structure that represents the game state on the game server. You interact with it by calling the game functions.

### Importing new files for your AI

Because your AI lives in the `games/blobmaster/` directory, if you add new files in that directory, then you must import them relative to the root of this directory. For example, this means if you add a new file `games/blobmaster/foo.py`, then you must import it via the python code:

```py
import games.blobmaster.foo
```

Please do not try to import it via `import foo`, that will not work. (unless you add it to the root of this repo, then it will but that seems a bit strange).

[cadre]: https://github.com/siggame/Cadre
[343]: https://www.python.org/downloads/release/python-343/
[winscp]: https://winscp.net/eng/download.php
[vagrant]: https://www.vagrantup.com/downloads.html
[virtualbox]: https://www.virtualbox.org/wiki/Downloads
[vagrant-guide]: https://www.vagrantup.com/docs/getting-started/up.html
[virtualbox]: https://www.virtualbox.org/wiki/Downloads
[gitbash]: https://git-scm.com/downloads

