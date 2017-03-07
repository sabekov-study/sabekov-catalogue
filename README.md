# SABEKOV: Studie zu sicherheitsrelevanten Aspekten der Benutzerkontenverwaltung

This repo publishes a catalogue of security checklist questions or criteria
related to web account security.

## The Story behind the SABEKOV Catalogue

SABEKOV (its a German acronym) was an attempt of a comprehensive study on security aspects of user
accounts on the web.
We, that is Christian Burkert, Maximilian Blochberger and Dominik Herrmann, all three
at the time researchers at the University of Hamburg, Germany,
compiled a catalogue of security-related criteria, that should be (mostly)
manually evaluated.
Unfortunately, we overdid the comprehensiveness and as a result,
the our testers gave up and the study never really took off.

Now we hope that someone might find this catalogue useful.
If so, we would love to hear about it!


## The Catalogue

[Here](catalogue.md)

**Note:** At the moment, the catalogue exists only in German.
Translations are welcome.

## Some Scripts

Alongside the catalogue we provide our helper scripts to:

- convert the markdown catalogue in JSON, and
- serialize the hyper-linked sub-catalogues in a link-free list of criteria

```sh
    $ python3 scripts/catunwinder.py < catalogue/index.md
```

## Copyright and License

The catalogue of criteria is copyright of Christian Burkert, Maximilian Blochberger
and Dominik Herrmann.
It can be freely used under the terms of the [license CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
