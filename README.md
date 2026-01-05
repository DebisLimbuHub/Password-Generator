# Python Password Generator and Manager

A compact Python project that generates strong random passwords and demonstrates basic account handling. It focuses on safer password habits by reducing weak choices and password reuse.

## Features

- Generates random passwords using letters digits and punctuation.
- Creates accounts using hidden password input via `getpass`.
- Stores passwords as SHA-256 hashes rather than plain text.
- Provides a simple CLI menu to create an account or log in.

## What I learnt

- How to combine character sets to increase password entropy.
- Why hashing passwords is safer than storing them in plain text and how to use `hashlib`.
- How to capture sensitive input without echoing it to the terminal using `getpass`.
- Why `random.choice` is not cryptographically secure and when to use `secrets` for production.

## Cybersecurity relevance

Poor passwords remain a common attack vector. This project supports stronger password creation and introduces core secure handling concepts such as hashing and safer input. For real world use, rely on a trusted password manager and implement salted hashes plus cryptographically secure randomness.

## Running the project

You need Python 3. Clone the repository then run the scripts from the `src` folder.

```bash
git clone https://github.com/DebisLimbuHub/Password-Generator.git
cd Password-Generator/src
python PasswordGenerator.py
python PasswordManager.py
```

## Supporting Material Links

https://www.youtube.com/watch?v=tbhYxd2sfAE




