# Move along

Nothing to see here (yet)

## Running

* Start the application via `hypnotoad xpnsr` using [Hypnotoad](https://mojolicious.org/perldoc/Mojo/Server/Hypnotoad) for hot deployment :)
* python-fints will be used as an initial bridge to be able to talk to bank :)

## Working on the python project

```
export WORKON_HOME=~/python3.6
source /home/foursixnine/.local/bin/virtualenvwrapper.sh
mkvirtualenv xpnsr
workon xpnsr
```

Adapt your `environment.conf` file, replace the necessary values that correspond with your bank account.
